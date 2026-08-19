from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
import os
import fitz

STUDENT_ID = "00724205101098"
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), f"{STUDENT_ID}_Offline5.pdf")
CPP_FILE = os.path.join(os.path.dirname(__file__), f"{STUDENT_ID}_Offline5.cpp")

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
    page_cover.insert_text(fitz.Point(sub_rect.x1 + 5, sub_rect.y1 - 2), '19/08/2026', fontsize=15.0, fontfile=font_path, fontname='Cambria')
    page_cover.insert_text(fitz.Point(sec_rect.x1 + 5, sec_rect.y1 - 2), 'B2', fontsize=15.0, fontfile=font_path, fontname='Cambria')
    page_cover.insert_text(fitz.Point(spring_rect.x0, spring_rect.y1 - 2), 'Fall 2025', fontsize=15.0, fontfile=font_path, fontname='Cambria')

    # Update Assignment No field - search for "01" near assignment area and replace with "05"
    assign_rects = page_cover.search_for('Assignment No:')
    if assign_rects:
        assign_rect = assign_rects[0]
        assign_no_rects = page_cover.search_for('01')
        for r in assign_no_rects:
            if abs(r.y0 - assign_rect.y0) < 20:
                page_cover.add_redact_annot(r, fill=(1,1,1))
                page_cover.apply_redactions()
                page_cover.insert_text(fitz.Point(r.x0, r.y1 - 2), '05', fontsize=15.0, fontfile=font_path, fontname='Cambria')
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
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName="Helvetica-Bold",
    )
    code_line_style = ParagraphStyle(
        "CodeLine",
        parent=styles["Normal"],
        fontName="Courier-Bold",
        fontSize=10.5,
        leading=14.5,
        leftIndent=12,
        rightIndent=12,
        textColor=colors.HexColor("#000000"),
        backColor=colors.HexColor("#ffffff"),
        spaceAfter=0,
        spaceBefore=0,
    )

    story = []

    # Report Title page header
    story.append(Paragraph("<u><b>CSE2104 Offline-5 Report</b></u>", report_title_style))
    story.append(Spacer(1, 0.4*cm))

    # Questions section
    story.append(Paragraph("<b>Tasks / Questions:</b>", ParagraphStyle("TaskHeader", parent=styles["Normal"], fontSize=11, fontName="Helvetica-Bold", spaceAfter=6)))
    
    tasks_text = (
        "Implement the below functions of doubly linked list in a single .cpp file.<br/>"
        "(1) insert first<br/>"
        "(2) insert last<br/>"
        "(3) insert anywhere between two nodes (by position, by value)<br/>"
        "(4) delete first<br/>"
        "(5) delete last<br/>"
        "(6) delete from anywhere between two nodes (by position, by value)<br/>"
        "(7) printingF() and printingB() -&gt; functions to print the linked list<br/>"
        "(8) searching() -&gt; function to search a value in the linked list<br/>"
        "(9) last_node() -&gt; function to print the value of the last node<br/>"
        "(10) previous_of_last_node()  -&gt; function to print the value of the previous node of last node<br/>"
        "(11) list_size()  -&gt; function to print the size of the linked list<br/>"
        "(12) reversePrint()  -&gt; function to print the linked list in reverse order<br/>"
        "(13) main function -&gt; no manual node creation/connection is allowed"
    )
    
    for line in tasks_text.split("<br/>"):
        p_style = ParagraphStyle("task_text", parent=styles["Normal"], fontName="Helvetica", fontSize=9.5, leading=14, spaceAfter=2)
        story.append(Paragraph(line if line else "&nbsp;", p_style))
        
    story.append(Spacer(1, 0.5*cm))

    # Read C++ Code
    if os.path.exists(CPP_FILE):
        with open(CPP_FILE, "r", encoding="utf-8") as f:
            code_content = f.read()
    else:
        code_content = "// C++ Code file not found"

    story.append(Paragraph("<b>Source Code (C++):</b>", ParagraphStyle("CodeHeader", parent=styles["Normal"], fontSize=10.5, fontName="Helvetica-Bold", spaceAfter=4)))

    code_lines = code_content.split("\n")
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
            extra["spaceBefore"] = 3
        if l_idx == len(code_lines) - 1:
            extra["spaceAfter"] = 3
        style = code_line_style if not extra else ParagraphStyle(
            f"CodeLine_{l_idx}", parent=code_line_style, **extra)
        story.append(Paragraph(escaped_line if escaped_line.strip() else "&nbsp;", style))

    story.append(PageBreak())

    # Execution Trace
    sample_trace = (
        "Enter the number of elements that insert at first : <b><font color='blue'>2</font></b><br/>"
        "Enter the elements<br/>"
        "<b><font color='blue'>10 20</font></b><br/>"
        "The elements in the forward direction are<br/>"
        "20 10<br/>"
        "The elements in the backward direction are<br/>"
        "10 20<br/>"
        "<br/>"
        "Enter the number of elements to insert at last<br/>"
        "<b><font color='blue'>2</font></b><br/>"
        "Enter the elements<br/>"
        "<b><font color='blue'>30 40</font></b><br/>"
        "After insert at last the elements in the forward direction are<br/>"
        "20 10 30 40<br/>"
        "After insert at last the elements in the backward direction are<br/>"
        "40 30 10 20<br/>"
        "<br/>"
        "Enter a position that insert : <b><font color='blue'>2</font></b><br/>"
        "Enter the value : <b><font color='blue'>25</font></b><br/>"
        "After insert at position the elements in the forward direction are<br/>"
        "20 25 10 30 40<br/>"
        "After insert at position the elements in the backward direction are<br/>"
        "40 30 10 25 20<br/>"
        "<br/>"
        "The elements in the forward direction after deleting the first element are<br/>"
        "25 10 30 40<br/>"
        "The elements in the backward direction after deleting the first element are<br/>"
        "40 30 10 25<br/>"
        "<br/>"
        "The elements in the forward direction after deleting the last element are<br/>"
        "25 10 30<br/>"
        "The elements in the backward direction after deleting the last element are<br/>"
        "30 10 25<br/>"
        "<br/>"
        "Enter the position to delete<br/>"
        "<b><font color='blue'>2</font></b><br/>"
        "The elements in the forward direction after deleting the element at position 2 are<br/>"
        "25 30<br/>"
        "The elements in the backward direction after deleting the element at position 2 are<br/>"
        "30 25<br/>"
        "<br/>"
        "Enter the value to delete<br/>"
        "<b><font color='blue'>30</font></b><br/>"
        "The elements in the forward direction after deleting the element with value 30 are<br/>"
        "25<br/>"
        "The elements in the backward direction after deleting the element with value 30 are<br/>"
        "25<br/>"
        "<br/>"
        "Searching value : <b><font color='blue'>25</font></b><br/>"
        "The searching value found : 25<br/>"
        "The last node value : 25<br/>"
        "List size : 1<br/>"
        "Reverse print of list : 25"
    )

    story.append(Paragraph("<b>Execution Trace (Input &amp; Output):</b> <i><font size=9.5>(User input is highlighted in </font><font color='blue' size=9.5><b>bold blue</b></font><font size=9.5>)</font></i>", ParagraphStyle("TraceHeader", parent=styles["Normal"], fontSize=11, fontName="Helvetica-Bold", spaceAfter=6, spaceBefore=4)))
    
    for line in sample_trace.split("<br/>"):
        p_style = ParagraphStyle("io_out", parent=styles["Normal"], fontName="Helvetica", fontSize=8.5, leading=11.5, spaceAfter=1.5)
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
