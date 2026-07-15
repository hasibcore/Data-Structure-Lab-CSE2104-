from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
import os
import fitz

STUDENT_ID = "00724205101098"
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), f"{STUDENT_ID}_Offline3.pdf")

TASKS = [
    {
        "num": 1,
        "title": "Quick Sort Comparison Count",
        "problem": "Given an array of N integers, simulate Quick Sort using the last element as pivot and count the number of comparisons performed during the sorting process.",
        "input": "6<br/>12 7 15 5 10 8",
        "output": "5 7 8 10 12 15<br/>22",
        "file": "00724205101098_Offline3_Task1.cpp"
    },
    {
        "num": 2,
        "title": "Partitioning Array around Pivot",
        "problem": "Given an array and a pivot, rearrange the array such that elements less than pivot come before it and greater come after.",
        "input": "6<br/>12 7 15 5 10 8<br/>10",
        "output": "8 7 5 10 12 15",
        "file": "00724205101098_Offline3_Task2.cpp"
    },
    {
        "num": 3,
        "title": "Quick Sort Swap Count",
        "problem": "Count the number of swaps required to sort an array using quick sort.",
        "input": "6<br/>12 7 15 5 10 8",
        "output": "5 7 8 10 12 15<br/>5",
        "file": "00724205101098_Offline3_Task3.cpp"
    },
    {
        "num": 4,
        "title": "Output Chosen Pivot at Each Recursion",
        "problem": "Output the pivot chosen at each recursive call in quick sort (always pick the last element as pivot).",
        "input": "6<br/>12 7 15 5 10 8",
        "output": "Pivot: 8<br/>Pivot: 7<br/>Pivot: 15<br/>Pivot: 10<br/>5 7 8 10 12 15",
        "file": "00724205101098_Offline3_Task4.cpp"
    },
    {
        "num": 5,
        "title": "Output Pivot Placement Index",
        "problem": "For each recursive quick sort call, output the final index where pivot is placed.",
        "input": "6<br/>12 7 15 5 10 8",
        "output": "Pivot Index: 2<br/>Pivot Index: 1<br/>Pivot Index: 5<br/>Pivot Index: 3<br/>5 7 8 10 12 15",
        "file": "00724205101098_Offline3_Task5.cpp"
    },
    {
        "num": 6,
        "title": "Count Elements Less Than Pivot",
        "problem": "For each pivot selected in quick sort (last element as pivot), count how many elements are less than the pivot at that step.",
        "input": "6<br/>12 7 15 5 10 8",
        "output": "Element less than pivot 8: 2<br/>Element less than pivot 7: 1<br/>Element less than pivot 15: 5<br/>Element less than pivot 10: 3<br/>5 7 8 10 12 15",
        "file": "00724205101098_Offline3_Task6.cpp"
    },
    {
        "num": 7,
        "title": "Merge Sort Combined Median",
        "problem": "Given two sorted arrays, find the median of the combined sorted array using merge sort. Also print the merged array.",
        "input": "4 3<br/>1 3 5 7<br/>2 4 6",
        "output": "Merged Array: 1 2 3 4 5 6 7<br/>Median: 4",
        "file": "00724205101098_Offline3_Task7.cpp"
    },
    {
        "num": 8,
        "title": "Merge Sort Comparison Count",
        "problem": "Calculate the total number of comparisons made during merge sort.",
        "input": "6<br/>12 7 15 5 10 8",
        "output": "5 7 8 10 12 15<br/>15",
        "file": "00724205101098_Offline3_Task8.cpp"
    },
    {
        "num": 9,
        "title": "Count Merge Operations",
        "problem": "Count the total number of merge operations performed when sorting an array using merge sort.",
        "input": "6<br/>12 7 15 5 10 8",
        "output": "5 7 8 10 12 15<br/>5",
        "file": "00724205101098_Offline3_Task9.cpp"
    },
    {
        "num": 10,
        "title": "Count Merge Sort Recursive Calls",
        "problem": "Determine the total number of recursive calls merge sort makes for a given array.",
        "input": "6<br/>12 7 15 5 10 8",
        "output": "5 7 8 10 12 15<br/>11",
        "file": "00724205101098_Offline3_Task10.cpp"
    }
]

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
    page_cover.insert_text(fitz.Point(sub_rect.x1 + 5, sub_rect.y1 - 2), '15/07/2026', fontsize=15.0, fontfile=font_path, fontname='Cambria')
    page_cover.insert_text(fitz.Point(sec_rect.x1 + 5, sec_rect.y1 - 2), 'B2', fontsize=15.0, fontfile=font_path, fontname='Cambria')
    page_cover.insert_text(fitz.Point(spring_rect.x0, spring_rect.y1 - 2), 'Fall 2025', fontsize=15.0, fontfile=font_path, fontname='Cambria')

    # Update Assignment No field - search for "01" near assignment area and replace with "03"
    assign_rects = page_cover.search_for('Assignment No:')
    if assign_rects:
        assign_rect = assign_rects[0]
        assign_no_rects = page_cover.search_for('01')
        for r in assign_no_rects:
            if abs(r.y0 - assign_rect.y0) < 20:
                page_cover.add_redact_annot(r, fill=(1,1,1))
                page_cover.apply_redactions()
                page_cover.insert_text(fitz.Point(r.x0, r.y1 - 2), '03', fontsize=15.0, fontfile=font_path, fontname='Cambria')
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
    code_line_style = ParagraphStyle(
        "CodeLine",
        parent=styles["Normal"],
        fontName="Courier-Bold",
        fontSize=10.5,
        leading=14,
        leftIndent=12,
        rightIndent=12,
        textColor=colors.HexColor("#000000"),
        backColor=colors.HexColor("#ffffff"),
        spaceAfter=0,
        spaceBefore=0,
    )

    story = []

    # Report Title page header
    story.append(Paragraph("<u><b>CSE2104 Offline-3 Report</b></u>", report_title_style))
    story.append(Spacer(1, 0.4*cm))

    # Introduction or Overview
    story.append(Paragraph(
        "This report contains the solutions, source code, and sample runs for the 10 tasks in Data Structure Lab (CSE2104) Offline Assignment 3. "
        "The first 6 tasks cover quick sort implementations, variations, and metrics. "
        "Tasks 7 to 10 cover merge sort applications, comparisons count, merge operations, and recursion calls.",
        body_style
    ))
    story.append(Spacer(1, 0.5*cm))

    for idx, t in enumerate(TASKS):
        if idx > 0:
            story.append(PageBreak())

        # Task Heading
        story.append(Paragraph(f"<b>Task {t['num']}: {t['title']}</b>", section_style))
        story.append(Spacer(1, 0.2*cm))

        # Problem Statement
        story.append(Paragraph(f"<b>Problem Statement:</b> {t['problem']}", body_style))
        story.append(Spacer(1, 0.2*cm))

        # Source Code Heading
        story.append(Paragraph("<b>Source Code (C++):</b>", ParagraphStyle("CodeHeader", parent=styles["Normal"], fontSize=10.5, fontName="Helvetica-Bold", spaceAfter=4)))

        # Read C++ Code
        cpp_path = os.path.join(os.path.dirname(__file__), t["file"])
        if os.path.exists(cpp_path):
            with open(cpp_path, "r", encoding="utf-8") as f:
                code_content = f.read()
        else:
            code_content = f"// Source file {t['file']} not found."

        code_lines = code_content.split("\n")
        for l_idx, line in enumerate(code_lines):
            line = line.rstrip('\r')
            escaped_line = (line
                            .replace("&", "&amp;")
                            .replace("<", "&lt;")
                            .replace(">", "&gt;")
                            .replace("    ", "&nbsp;&nbsp;&nbsp;&nbsp;"))
            extra = {}
            if l_idx == 0:
                extra["spaceBefore"] = 4
            if l_idx == len(code_lines) - 1:
                extra["spaceAfter"] = 4
            style = code_line_style if not extra else ParagraphStyle(
                f"CodeLine_{t['num']}_{l_idx}", parent=code_line_style, **extra)
            story.append(Paragraph(escaped_line if escaped_line.strip() else "&nbsp;", style))

        story.append(Spacer(1, 0.4*cm))

        # Sample I/O
        titles_data = [
            [Paragraph("<b>Sample Input</b>", ParagraphStyle("title_left", parent=styles["Normal"], fontSize=10, fontName="Helvetica-Bold", alignment=TA_LEFT)),
             Paragraph("<b>Sample Output</b>", ParagraphStyle("title_right", parent=styles["Normal"], fontSize=10, fontName="Helvetica-Bold", alignment=TA_LEFT))]
        ]
        titles_table = Table(titles_data, colWidths=[8.5*cm, 8.5*cm])
        titles_table.setStyle(TableStyle([
            ("VALIGN", (0,0), (-1,-1), "BOTTOM"),
            ("BOTTOMPADDING", (0,0), (-1,-1), 4),
            ("LEFTPADDING", (0,0), (-1,-1), 0),
            ("RIGHTPADDING", (0,0), (-1,-1), 0),
        ]))
        story.append(titles_table)

        io_data = [
            [Paragraph(t["input"], ParagraphStyle("io_in", parent=styles["Normal"], fontName="Helvetica", fontSize=9, leading=13)),
             Paragraph(t["output"], ParagraphStyle("io_out", parent=styles["Normal"], fontName="Helvetica", fontSize=9, leading=13))]
        ]
        io_table = Table(io_data, colWidths=[8.5*cm, 8.5*cm])
        io_table.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,-1), colors.white),
            ("BOX",        (0,0), (-1,-1), 1,   colors.black),
            ("LINEBEFORE", (1,0), (1,-1), 1,   colors.black),  # middle vertical divider
            ("VALIGN",     (0,0), (-1,-1), "TOP"),
            ("TOPPADDING",    (0,0), (-1,-1), 6),
            ("BOTTOMPADDING", (0,0), (-1,-1), 6),
            ("LEFTPADDING",   (0,0), (-1,-1), 6),
            ("RIGHTPADDING",  (0,0), (-1,-1), 6),
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

    cover_pdf.close()
    report_pdf.close()
    output_pdf.close()

    # Cleanup temp files
    os.remove(cover_filled_path)
    os.remove(report_only_path)
    print(f"PDF generated successfully: {OUTPUT_FILE}")

if __name__ == "__main__":
    build_pdf()
