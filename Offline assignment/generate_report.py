from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
import os
import fitz

STUDENT_ID = "00724205101098"
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), f"{STUDENT_ID}_Offline1.pdf")

cpp_filepath = os.path.join(os.path.dirname(__file__), f"{STUDENT_ID}_Offline1.cpp")
if os.path.exists(cpp_filepath):
    with open(cpp_filepath, "r", encoding="utf-8") as f:
        CODE = f.read()
else:
    CODE = "// C++ Code file not found"

def build_pdf():
    # File paths for intermediate steps
    cover_filled_path = os.path.join(os.path.dirname(__file__), "cover_filled_temp.pdf")
    report_only_path = os.path.join(os.path.dirname(__file__), "report_only_temp.pdf")

    # 1. Fill the Cover Page
    doc_cover = fitz.open(os.path.join(os.path.dirname(__file__), 'Cover page sample.pdf'))
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
    page_cover.insert_text(fitz.Point(sub_rect.x1 + 5, sub_rect.y1 - 2), '29/06/2026', fontsize=15.0, fontfile=font_path, fontname='Cambria')
    page_cover.insert_text(fitz.Point(sec_rect.x1 + 5, sec_rect.y1 - 2), 'B2', fontsize=15.0, fontfile=font_path, fontname='Cambria')
    page_cover.insert_text(fitz.Point(spring_rect.x0, spring_rect.y1 - 2), 'Fall 2025', fontsize=15.0, fontfile=font_path, fontname='Cambria')

    doc_cover.save(cover_filled_path)
    doc_cover.close()

    # 2. Build Report Body (without the cover information/headers)
    doc_report = SimpleDocTemplate(
        report_only_path,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm,
    )

    styles = getSampleStyleSheet()

    # Custom styles
    report_title_style = ParagraphStyle(
        "ReportTitle",
        parent=styles["Title"],
        fontSize=16,
        textColor=colors.black,
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName="Helvetica-Bold",
    )
    section_style = ParagraphStyle(
        "Section",
        parent=styles["Heading2"],
        fontSize=12,
        textColor=colors.black,
        fontName="Helvetica-Bold",
        spaceBefore=14,
        spaceAfter=6,
        borderPad=4,
    )
    body_style = ParagraphStyle(
        "Body",
        parent=styles["Normal"],
        fontSize=10.5,
        leading=16,
        alignment=TA_JUSTIFY,
        spaceAfter=6,
    )
    bullet_style = ParagraphStyle(
        "Bullet",
        parent=styles["Normal"],
        fontSize=10.5,
        leading=16,
        leftIndent=20,
        spaceAfter=3,
    )

    story = []

    # Report Title
    story.append(Paragraph("<u><b>CSE2104 Offline-1</b></u>", report_title_style))
    story.append(Spacer(1, 0.4*cm))

    # Problem Statement (Copy-pasted)
    story.append(Paragraph(
        "A bookstore maintains a sorted list of unique book IDs to quickly identify whether a book is "
        "available in stock. You are required to write a C++ program that uses <b>Binary Search</b> to "
        "determine if a specific book ID is present in the list. Additionally, the store often needs to "
        "find the first book ID that is not smaller than a given value (lower bound) and the first book ID "
        "that is greater than a given value (upper bound) in order to manage restocking and categorization. "
        "Given a sorted array of book IDs and a query book ID, your program should output whether the book "
        "exists in the list, the lower bound position and the upper bound position corresponding to the query.",
        body_style
    ))

    # Tasks (Exactly copied)
    story.append(Paragraph("<b>Tasks</b>", ParagraphStyle("TasksHeader", parent=styles["Normal"], fontSize=11, fontName="Helvetica-Bold", spaceBefore=12, spaceAfter=6)))
    tasks = [
        "Read the number of book IDs and then read the sorted list of unique book IDs.",
        "Read the query book ID to be searched.",
        "Implement <b>Binary Search</b> to check if the book ID exists.",
        "Implement logic to find the <b>lower bound</b> of the query.",
        "Implement logic to find the <b>upper bound</b> of the query.",
        "Display the search result along with the lower and upper bound indices."
    ]
    for i, task in enumerate(tasks, 1):
        story.append(Paragraph(f"{i}. &nbsp; {task}", bullet_style))

    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        "You should write user defined functions for Binary Search, Lower Bound and Upper Bound. "
        "Input should be taken inside the main function. All user defined functions must be called "
        "from the main function.",
        body_style
    ))

    # Algorithm
    story.append(Paragraph("Algorithm", section_style))
    algo_steps = [
        "Read the number of book IDs (N).",
        "Read all the book IDs into a vector.",
        "Sort the vector in ascending order using the sort() function.",
        "Read the query book ID.",
        "Use the Binary Search function to check whether the book ID exists.",
        "Use the Lower Bound function to find the first index whose value is greater than or equal to the query.",
        "Use the Upper Bound function to find the first index whose value is strictly greater than the query.",
        "Display \"Book Found\" if the book exists; otherwise display \"Book Not Found\".",
        "Display the Lower Bound index.",
        "Display the Upper Bound index."
    ]
    for i, step in enumerate(algo_steps, 1):
        story.append(Paragraph(f"{i}. {step}", bullet_style))
        story.append(Spacer(1, 0.05*cm))

    # Code
    story.append(PageBreak())
    story.append(Paragraph("Source Code (C++)", section_style))

    code_line_style = ParagraphStyle(
        "CodeLine",
        parent=styles["Normal"],
        fontName="Courier-Bold",
        fontSize=9.0,
        leading=13,
        leftIndent=12,
        rightIndent=12,
        textColor=colors.HexColor("#000000"),
        backColor=colors.HexColor("#ffffff"),
        spaceAfter=0,
        spaceBefore=0,
    )
    code_lines = CODE.split("\n")
    for idx, line in enumerate(code_lines):
        escaped_line = (line
                        .replace("&", "&amp;")
                        .replace("<", "&lt;")
                        .replace(">", "&gt;")
                        .replace("    ", "&nbsp;&nbsp;&nbsp;&nbsp;"))
        extra = {}
        if idx == 0:
            extra["spaceBefore"] = 8
        if idx == len(code_lines) - 1:
            extra["spaceAfter"] = 8
        style = code_line_style if not extra else ParagraphStyle(
            f"CodeLine_{idx}", parent=code_line_style, **extra)
        story.append(Paragraph(escaped_line if escaped_line.strip() else "&nbsp;", style))

    # Sample I/O
    story.append(Spacer(1, 0.4*cm))
    
    # Header row (no borders)
    titles_data = [
        [Paragraph("<b>Sample Input</b>", ParagraphStyle("title_left", parent=styles["Normal"], fontSize=11, fontName="Helvetica-Bold", alignment=TA_LEFT)),
         Paragraph("<b>Sample Output</b>", ParagraphStyle("title_right", parent=styles["Normal"], fontSize=11, fontName="Helvetica-Bold", alignment=TA_LEFT))]
    ]
    titles_table = Table(titles_data, colWidths=[8.5*cm, 8.5*cm])
    titles_table.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "BOTTOM"),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING", (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
    ]))
    story.append(titles_table)

    # Box content (plain borders, white bg)
    io_data = [
        [Paragraph("7<br/>10 20 30 40 50 60 70<br/>40",
                   ParagraphStyle("io_in", parent=styles["Normal"], fontName="Helvetica", fontSize=9.5, leading=15)),
         Paragraph("Book Found<br/>Lower Bound Index: 3<br/>Upper Bound Index: 4",
                   ParagraphStyle("io_out", parent=styles["Normal"], fontName="Helvetica", fontSize=9.5, leading=15))]
    ]
    io_table = Table(io_data, colWidths=[8.5*cm, 8.5*cm])
    io_table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), colors.white),
        ("BOX",        (0,0), (-1,-1), 1,   colors.black),
        ("LINEBEFORE", (1,0), (1,-1), 1,   colors.black), # middle vertical divider
        ("VALIGN",     (0,0), (-1,-1), "TOP"),
        ("TOPPADDING",    (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LEFTPADDING",   (0,0), (-1,-1), 8),
        ("RIGHTPADDING",  (0,0), (-1,-1), 8),
    ]))
    story.append(io_table)

    doc_report.build(story)

    # 3. Merge cover page and report
    output_pdf = fitz.open()
    
    cover_pdf = fitz.open(cover_filled_path)
    output_pdf.insert_pdf(cover_pdf)
    
    report_pdf = fitz.open(report_only_path)
    output_pdf.insert_pdf(report_pdf)
    
    output_pdf.save(OUTPUT_FILE)
    
    # Close docs
    cover_pdf.close()
    report_pdf.close()
    output_pdf.close()
    
    # Cleanup temp files
    os.remove(cover_filled_path)
    os.remove(report_only_path)
    print(f"PDF generated successfully: {OUTPUT_FILE}")

if __name__ == "__main__":
    build_pdf()
