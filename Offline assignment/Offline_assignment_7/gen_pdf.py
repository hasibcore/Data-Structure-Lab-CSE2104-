from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image as RLImage
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
import os
import fitz

STUDENT_ID = "00724205101098"
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), f"{STUDENT_ID}_Offline7.pdf")
BFS_CPP_FILE = os.path.join(os.path.dirname(__file__), f"{STUDENT_ID}_Offline7_BFS.cpp")
DFS_CPP_FILE = os.path.join(os.path.dirname(__file__), f"{STUDENT_ID}_Offline7_DFS.cpp")
BFS_IMG_FILE = os.path.join(os.path.dirname(__file__), "bfs_output.png")
DFS_IMG_FILE = os.path.join(os.path.dirname(__file__), "dfs_output.png")

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
    page_cover.insert_text(fitz.Point(sub_rect.x1 + 5, sub_rect.y1 - 2), '02/09/2026', fontsize=15.0, fontfile=font_path, fontname='Cambria')
    page_cover.insert_text(fitz.Point(sec_rect.x1 + 5, sec_rect.y1 - 2), 'B2', fontsize=15.0, fontfile=font_path, fontname='Cambria')
    page_cover.insert_text(fitz.Point(spring_rect.x0, spring_rect.y1 - 2), 'Fall 2025', fontsize=15.0, fontfile=font_path, fontname='Cambria')

    # Update Assignment No field - search for "01" near assignment area and replace with "07"
    assign_rects = page_cover.search_for('Assignment No:')
    if assign_rects:
        assign_rect = assign_rects[0]
        assign_no_rects = page_cover.search_for('01')
        for r in assign_no_rects:
            if abs(r.y0 - assign_rect.y0) < 20:
                page_cover.add_redact_annot(r, fill=(1,1,1))
                page_cover.apply_redactions()
                page_cover.insert_text(fitz.Point(r.x0, r.y1 - 2), '07', fontsize=15.0, fontfile=font_path, fontname='Cambria')
                break

    doc_cover.save(cover_filled_path)
    doc_cover.close()

    # 2. Build Report Body
    doc_report = SimpleDocTemplate(
        report_only_path,
        pagesize=A4,
        rightMargin=1.2*cm,
        leftMargin=1.2*cm,
        topMargin=1.0*cm,
        bottomMargin=1.0*cm,
    )

    styles = getSampleStyleSheet()

    report_title_style = ParagraphStyle(
        "ReportTitle",
        parent=styles["Title"],
        fontSize=17,
        textColor=colors.black,
        spaceAfter=6,
        alignment=TA_CENTER,
        fontName="Helvetica-Bold",
    )
    section_header_style = ParagraphStyle(
        "SectionHeader",
        parent=styles["Normal"],
        fontSize=12.0,
        fontName="Helvetica-Bold",
        textColor=colors.black,
        spaceBefore=6,
        spaceAfter=4,
    )
    sub_section_style = ParagraphStyle(
        "SubSectionHeader",
        parent=styles["Normal"],
        fontSize=11.5,
        fontName="Helvetica-Bold",
        textColor=colors.HexColor("#1a365d"),
        spaceBefore=8,
        spaceAfter=5,
    )
    task_desc_style = ParagraphStyle(
        "TaskDesc",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10.5,
        leading=14.5,
        spaceAfter=3,
    )
    code_line_style = ParagraphStyle(
        "CodeLine",
        parent=styles["Normal"],
        fontName="Courier-Bold",
        fontSize=10.0,
        leading=13.5,
        leftIndent=8,
        rightIndent=8,
        textColor=colors.HexColor("#000000"),
        backColor=colors.HexColor("#ffffff"),
        spaceAfter=0,
        spaceBefore=0,
    )

    story = []

    # Report Title page header
    story.append(Paragraph("<u><b>CSE2104 Offline-7 Report</b></u>", report_title_style))
    story.append(Spacer(1, 0.1*cm))

    # Questions / Problem Statement
    story.append(Paragraph("<b>Problem Statement / Tasks:</b>", section_header_style))
    
    tasks_text = "Implement <b>BFS</b> and <b>DFS</b> in two separate .cpp files."
    story.append(Paragraph(tasks_text, task_desc_style))

    story.append(Spacer(1, 0.15*cm))

    # Function to render code cleanly
    def append_code(file_path, header_title, font_size=9.8, leading=12.6):
        story.append(Paragraph(f"<b>Source Code ({header_title}):</b>", section_header_style))
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                code_content = f.read()
        else:
            code_content = f"// File {file_path} not found."

        custom_code_style = ParagraphStyle(
            f"CodeStyle_{header_title}",
            parent=code_line_style,
            fontSize=font_size,
            leading=leading
        )

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
                extra["spaceBefore"] = 1
            if l_idx == len(code_lines) - 1:
                extra["spaceAfter"] = 1
            style = custom_code_style if not extra else ParagraphStyle(
                f"CodeLine_{header_title}_{l_idx}", parent=custom_code_style, **extra)
            story.append(Paragraph(escaped_line if escaped_line.strip() else "&nbsp;", style))

    # Add Task 1 (BFS Code)
    append_code(BFS_CPP_FILE, "Task 1: Breadth-First Search (BFS)", font_size=9.6, leading=12.5)

    story.append(PageBreak())

    # Add Task 2 (DFS Code)
    append_code(DFS_CPP_FILE, "Task 2: Depth-First Search (DFS)", font_size=11.0, leading=15.5)

    story.append(PageBreak())

    # Execution Trace Section
    story.append(Paragraph("<b>Execution Trace (Input &amp; Output):</b>", ParagraphStyle("TraceHeader", parent=styles["Normal"], fontSize=13.5, fontName="Helvetica-Bold", spaceAfter=10, spaceBefore=2)))

    # BFS Output Screenshot
    story.append(Paragraph("<b>1. Breadth-First Search (BFS) Output:</b>", sub_section_style))
    if os.path.exists(BFS_IMG_FILE):
        bfs_width = 16.0 * cm
        bfs_height = 16.0 * (322.0 / 667.0) * cm
        story.append(RLImage(BFS_IMG_FILE, width=bfs_width, height=bfs_height))
    
    story.append(Spacer(1, 0.5*cm))

    # DFS Output Screenshot
    story.append(Paragraph("<b>2. Depth-First Search (DFS) Output:</b>", sub_section_style))
    if os.path.exists(DFS_IMG_FILE):
        dfs_width = 16.0 * cm
        dfs_height = 16.0 * (247.0 / 727.0) * cm
        story.append(RLImage(DFS_IMG_FILE, width=dfs_width, height=dfs_height))

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
