from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image as RLImage
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
import os
import fitz

STUDENT_ID = "00724205101098"
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), f"{STUDENT_ID}_Offline6.pdf")
CPP_FILE = os.path.join(os.path.dirname(__file__), f"{STUDENT_ID}_Offline6.cpp")
IMG_FILE = os.path.join(os.path.dirname(__file__), "input_output.png")

def build_pdf():
    # File paths for intermediate steps
    cover_filled_path = os.path.join(os.path.dirname(__file__), "cover_filled_temp.pdf")
    report_only_path = os.path.join(os.path.dirname(__file__), "report_only_temp.pdf")

    # 1. Fill the Cover Page
    cover_template_path = os.path.join(os.path.dirname(__file__), "..", "Cover page sample.pdf")
    if not os.path.exists(cover_template_path):
        print(f"Error: Cover page template not found at {cover_template_path}")
        return

    doc_cover = fitz.open(cover_template_path)
    page_cover = doc_cover[0]

    # Search coordinates of placeholders
    xyz_rect = page_cover.search_for('XYZ')[0]
    id_rect = page_cover.search_for('140204104')[0]
    course_rect = page_cover.search_for('CSE 2103')[0]
    sub_rect = page_cover.search_for('Date of Submission:')[0]
    sec_rect = page_cover.search_for('Lab Section:')[0]
    spring_rect = page_cover.search_for('Spring 2025')[0]

    # Add redacts to clear the placeholders
    page_cover.add_redact_annot(xyz_rect, fill=(1,1,1))
    page_cover.add_redact_annot(id_rect, fill=(1,1,1))
    page_cover.add_redact_annot(course_rect, fill=(1,1,1))
    page_cover.add_redact_annot(spring_rect, fill=(1,1,1))
    page_cover.apply_redactions()

    # Insert new text
    font_path = 'C:/Windows/Fonts/cambria.ttc'
    page_cover.insert_text(fitz.Point(xyz_rect.x0, xyz_rect.y1 - 2), 'Hasibul Hasan', fontsize=15.0, fontfile=font_path, fontname='Cambria')
    page_cover.insert_text(fitz.Point(id_rect.x0, id_rect.y1 - 2), STUDENT_ID, fontsize=15.0, fontfile=font_path, fontname='Cambria')
    page_cover.insert_text(fitz.Point(course_rect.x0, course_rect.y1 - 2), 'CSE 2104', fontsize=15.0, fontfile=font_path, fontname='Cambria')
    page_cover.insert_text(fitz.Point(sub_rect.x1 + 5, sub_rect.y1 - 2), '26/08/2026', fontsize=15.0, fontfile=font_path, fontname='Cambria')
    page_cover.insert_text(fitz.Point(sec_rect.x1 + 5, sec_rect.y1 - 2), 'B2', fontsize=15.0, fontfile=font_path, fontname='Cambria')
    page_cover.insert_text(fitz.Point(spring_rect.x0, spring_rect.y1 - 2), 'Fall 2025', fontsize=15.0, fontfile=font_path, fontname='Cambria')

    # Update Assignment No field - search for "01" near assignment area and replace with "06"
    assign_rects = page_cover.search_for('Assignment No:')
    if assign_rects:
        assign_rect = assign_rects[0]
        assign_no_rects = page_cover.search_for('01')
        for r in assign_no_rects:
            if abs(r.y0 - assign_rect.y0) < 20:
                page_cover.add_redact_annot(r, fill=(1,1,1))
                page_cover.apply_redactions()
                page_cover.insert_text(fitz.Point(r.x0, r.y1 - 2), '06', fontsize=15.0, fontfile=font_path, fontname='Cambria')
                break

    doc_cover.save(cover_filled_path)
    doc_cover.close()

    # 2. Build Report Body
    doc_report = SimpleDocTemplate(
        report_only_path,
        pagesize=A4,
        rightMargin=1.5*cm,
        leftMargin=1.5*cm,
        topMargin=1.5*cm,
        bottomMargin=1.5*cm,
    )

    styles = getSampleStyleSheet()

    report_title_style = ParagraphStyle(
        "ReportTitle",
        parent=styles["Title"],
        fontSize=16,
        textColor=colors.black,
        spaceAfter=10,
        alignment=TA_CENTER,
        fontName="Helvetica-Bold",
    )
    code_line_style = ParagraphStyle(
        "CodeLine",
        parent=styles["Normal"],
        fontName="Courier-Bold",
        fontSize=11.5,
        leading=15.5,
        leftIndent=12,
        rightIndent=12,
        textColor=colors.HexColor("#000000"),
        backColor=colors.HexColor("#ffffff"),
        spaceAfter=0,
        spaceBefore=0,
    )

    story = []

    # Report Title page header
    story.append(Paragraph("<u><b>CSE2104 Offline-6 Report</b></u>", report_title_style))
    story.append(Spacer(1, 0.2*cm))

    # Questions section
    story.append(Paragraph("<b>Problem Statement / Task:</b>", ParagraphStyle("TaskHeader", parent=styles["Normal"], fontSize=11.5, fontName="Helvetica-Bold", spaceAfter=6)))
    
    tasks_text = (
        "Write a program to support multi-digit numbers in the conversion of an infix expression to postfix notation and the evaluation of the resulting postfix expression.<br/>"
        "For example, your code should convert this infix expression to its appropriate postfix notation: <b>(12 + 34) * 56 - 78 / 9</b>.<br/>"
        "Then evaluate the result of this expression from the postfix notation."
    )
    
    for line in tasks_text.split("<br/>"):
        p_style = ParagraphStyle("task_text", parent=styles["Normal"], fontName="Helvetica", fontSize=10, leading=14, spaceAfter=2)
        story.append(Paragraph(line if line else "&nbsp;", p_style))
        
    story.append(Spacer(1, 0.4*cm))

    # Read C++ Code
    if os.path.exists(CPP_FILE):
        with open(CPP_FILE, "r", encoding="utf-8") as f:
            code_content = f.read()
    else:
        code_content = "// C++ Code file not found"

    story.append(Paragraph("<b>Source Code (C++):</b>", ParagraphStyle("CodeHeader", parent=styles["Normal"], fontSize=11.5, fontName="Helvetica-Bold", spaceAfter=6)))

    code_lines = code_content.strip().split("\n")
    for l_idx, line in enumerate(code_lines):
        line = line.rstrip('\r')
        escaped_line = (line
                        .replace("&", "&amp;")
                        .replace("<", "&lt;")
                        .replace(">", "&gt;")
                        .replace("    ", "&nbsp;&nbsp;&nbsp;&nbsp;")
                        .replace("  ", "&nbsp;&nbsp;"))
        extra = {}
        if l_idx == 0:
            extra["spaceBefore"] = 2
        if l_idx == len(code_lines) - 1:
            extra["spaceAfter"] = 2
        style = code_line_style if not extra else ParagraphStyle(
            f"CodeLine_{l_idx}", parent=code_line_style, **extra)
        story.append(Paragraph(escaped_line if escaped_line.strip() else "&nbsp;", style))

    story.append(PageBreak())

    # Execution Trace / Input Output Header
    story.append(Paragraph("<b>Execution Trace (Input &amp; Output):</b>", ParagraphStyle("TraceHeader", parent=styles["Normal"], fontSize=12, fontName="Helvetica-Bold", spaceAfter=10, spaceBefore=4)))

    # Embed User Output Screenshot Image if exists
    if os.path.exists(IMG_FILE):
        story.append(Paragraph("<b>Console Output Screenshot:</b>", ParagraphStyle("SubHeader", parent=styles["Normal"], fontSize=11, fontName="Helvetica-Bold", spaceAfter=8)))
        img_width = 16.5 * cm
        img_height = 16.5 * (127.0 / 687.0) * cm
        img_flowable = RLImage(IMG_FILE, width=img_width, height=img_height)
        story.append(img_flowable)
        story.append(Spacer(1, 0.8*cm))

    # Text Breakdown of Execution Traces
    sample_trace = (
        "<b><u>Execution Output Details:</u></b><br/>"
        "Enter the infix expression: <b><font color='blue'>(12+34)*56-78/9</font></b><br/>"
        "Postfix expression: 12 34 + 56 * 78 9 / - <br/>"
        "Evaluation result : 2568"
    )

    for line in sample_trace.split("<br/>"):
        p_style = ParagraphStyle("io_out", parent=styles["Normal"], fontName="Courier-Bold", fontSize=10.5, leading=15, spaceAfter=2)
        story.append(Paragraph(line if line else "&nbsp;", p_style))

    doc_report.build(story)

    # 3. Merge cover page and report
    output_pdf = fitz.open()

    cover_pdf = fitz.open(cover_filled_path)
    output_pdf.insert_pdf(cover_pdf)

    report_pdf = fitz.open(report_only_path)
    output_pdf.insert_pdf(report_pdf)

    output_pdf.save(OUTPUT_FILE)

    cover_pdf.close()
    report_pdf.close()
    output_pdf.close()

    # Cleanup temp files
    os.remove(cover_filled_path)
    os.remove(report_only_path)
    print(f"PDF generated successfully: {OUTPUT_FILE}")

if __name__ == "__main__":
    build_pdf()
