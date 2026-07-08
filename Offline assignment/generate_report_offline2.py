from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
import os
import fitz

STUDENT_ID = "00724205101098"
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), f"{STUDENT_ID}_Offline2.pdf")

cpp_filepath = os.path.join(os.path.dirname(__file__), f"{STUDENT_ID}_Offline2.cpp")
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
    page_cover.insert_text(fitz.Point(sub_rect.x1 + 5, sub_rect.y1 - 2), '08/07/2026', fontsize=15.0, fontfile=font_path, fontname='Cambria')
    page_cover.insert_text(fitz.Point(sec_rect.x1 + 5, sec_rect.y1 - 2), 'B2', fontsize=15.0, fontfile=font_path, fontname='Cambria')
    page_cover.insert_text(fitz.Point(spring_rect.x0, spring_rect.y1 - 2), 'Fall 2025', fontsize=15.0, fontfile=font_path, fontname='Cambria')

    # Update Assignment No field - search for "01" near assignment area and replace with "02"
    assign_rects = page_cover.search_for('Assignment No:')
    if assign_rects:
        assign_rect = assign_rects[0]
        # The "01" text is right after "Assignment No:" on the same or next position
        assign_no_rects = page_cover.search_for('01')
        for r in assign_no_rects:
            # Find the one that's near the Assignment No label (within 200 units)
            if abs(r.y0 - assign_rect.y0) < 20:
                page_cover.add_redact_annot(r, fill=(1,1,1))
                page_cover.apply_redactions()
                page_cover.insert_text(fitz.Point(r.x0, r.y1 - 2), '02', fontsize=15.0, fontfile=font_path, fontname='Cambria')
                break

    doc_cover.save(cover_filled_path)
    doc_cover.close()

    # 2. Build Report Body
    doc_report = SimpleDocTemplate(
        report_only_path,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm,
    )

    styles = getSampleStyleSheet()

    # Custom styles (same as Offline-1 theme)
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
    sub_bullet_style = ParagraphStyle(
        "SubBullet",
        parent=styles["Normal"],
        fontSize=10.5,
        leading=16,
        leftIndent=40,
        spaceAfter=2,
    )

    story = []

    # Report Title
    story.append(Paragraph("<u><b>CSE2104 Offline-2</b></u>", report_title_style))
    story.append(Spacer(1, 0.4*cm))

    # Problem Statement
    story.append(Paragraph(
        "You are given a list of books, each with a title, author and publication year. Your task is to sort "
        "the books by the publication year in <b>descending order</b> (most recent first) and if two books have "
        "the same publication year, sort them lexicographically by author in <b>ascending order</b>. If both the "
        "publication year and author are the same, sort the books lexicographically by title in <b>ascending "
        "order</b>. Implement this sorting using the <b>Selection Sort</b> algorithm. The input consists of an integer "
        "N (the number of books), followed by N lines of book details, where each line contains the title, "
        "author and publication year. Output the books in the sorted order, each on a new line in the "
        "format: \"Title, Author, Publication Year\".",
        body_style
    ))

    # Input Format
    story.append(Paragraph("<b>Input Format</b>", ParagraphStyle("TasksHeader", parent=styles["Normal"], fontSize=11, fontName="Helvetica-Bold", spaceBefore=12, spaceAfter=6)))
    story.append(Paragraph("&#8226; &nbsp; The first line contains an integer N, the number of books (1 \u2264 N \u2264 1000).", bullet_style))
    story.append(Paragraph("&#8226; &nbsp; Each of the next N lines contains a book's information in the format:", bullet_style))
    story.append(Paragraph("- Title, Author, Publication Year", sub_bullet_style))
    story.append(Paragraph("- The Title is a string (1 \u2264 length of title \u2264 100)", sub_bullet_style))
    story.append(Paragraph("- The Author is a string (1 \u2264 length of author name \u2264 100)", sub_bullet_style))
    story.append(Paragraph("- The Publication Year is an integer (1900 \u2264 year \u2264 2025)", sub_bullet_style))

    # Output Format
    story.append(Paragraph("<b>Output Format</b>", ParagraphStyle("OutputHeader", parent=styles["Normal"], fontSize=11, fontName="Helvetica-Bold", spaceBefore=12, spaceAfter=6)))
    story.append(Paragraph(
        "Print the books in sorted order based on the criteria above, one book per line in the following format:",
        body_style
    ))
    story.append(Paragraph("&#8226; &nbsp; Title, Author, Publication Year", bullet_style))

    # Algorithm
    story.append(Paragraph("Algorithm", section_style))
    algo_steps = [
        "Read the integer N (number of books).",
        "For each of the N books, read a line and parse the Title, Author, and Publication Year separated by commas.",
        "Store each book as a struct with fields: bName (title), author, and y (publication year).",
        "Apply <b>Selection Sort</b> on the list of books using the following multi-key comparison:",
        [
            "Primary key: Publication Year in <b>descending</b> order (larger year comes first).",
            "Secondary key: Author name in <b>ascending</b> lexicographic order (if years are equal).",
            "Tertiary key: Book title in <b>ascending</b> lexicographic order (if year and author are equal).",
        ],
        "In each pass of Selection Sort, find the maximum element (per the above criteria) from the unsorted portion and swap it to its correct position.",
        "After sorting, print each book on a new line in the format: Title, Author, Publication Year.",
    ]

    step_num = 1
    for step in algo_steps:
        if isinstance(step, list):
            for sub in step:
                story.append(Paragraph(f"&nbsp;&nbsp;&nbsp;&nbsp;- {sub}", sub_bullet_style))
        else:
            story.append(Paragraph(f"{step_num}. {step}", bullet_style))
            story.append(Spacer(1, 0.05*cm))
            step_num += 1

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
        # Strip Windows carriage return
        line = line.rstrip('\r')
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

    sample_input = (
        "5<br/>"
        "Sapiens, Yuval Noah Harari, 2011<br/>"
        "21 Lessons for the 21st Century, Yuval Noah Harari, 2018<br/>"
        "Educated, Tara Westover, 2018<br/>"
        "Becoming, Michelle Obama, 2018<br/>"
        "Money: Vintage Minis, Yuval Noah Harari, 2018"
    )
    sample_output = (
        "Becoming, Michelle Obama, 2018<br/>"
        "Educated, Tara Westover, 2018<br/>"
        "21 Lessons for the 21st Century, Yuval Noah Harari, 2018<br/>"
        "Money: Vintage Minis, Yuval Noah Harari, 2018<br/>"
        "Sapiens, Yuval Noah Harari, 2011"
    )

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
        [Paragraph(sample_input,
                   ParagraphStyle("io_in", parent=styles["Normal"], fontName="Helvetica", fontSize=9.5, leading=15)),
         Paragraph(sample_output,
                   ParagraphStyle("io_out", parent=styles["Normal"], fontName="Helvetica", fontSize=9.5, leading=15))]
    ]
    io_table = Table(io_data, colWidths=[8.5*cm, 8.5*cm])
    io_table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), colors.white),
        ("BOX",        (0,0), (-1,-1), 1,   colors.black),
        ("LINEBEFORE", (1,0), (1,-1), 1,   colors.black),  # middle vertical divider
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
