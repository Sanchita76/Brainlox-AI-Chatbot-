import os
import re
from fpdf import FPDF
from query_engine import search_query
from extract_data import extract_courses

PDF_DIR = "pdf_reports"
os.makedirs(PDF_DIR, exist_ok=True)

def sanitize_filename(text):
    return re.sub(r'[\/:*?"<>|]', '', text)  # Remove invalid filename characters

def generate_pdf(user_query=""):  # Default query to empty string
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=10)
    pdf.add_page()

    # **Fix: Use DejaVuSans Unicode font**
    font_path = "DejaVuSans.ttf"  # Place this file in the same directory
    if not os.path.exists(font_path):
        raise FileNotFoundError("DejaVuSans.ttf not found. Please download and place it in the project directory.")

    pdf.add_font("DejaVu", "", font_path, uni=True)
    pdf.set_font("DejaVu", "", 12)

    pdf.cell(200, 10, "Brainlox Course Information Report", ln=True, align="C")
    pdf.ln(10)

    # Extract and Add Course Data
    courses = extract_courses()
    pdf.set_font("DejaVu", "", 10)
    pdf.cell(200, 10, "Extracted Courses", ln=True, align="L")
    pdf.ln(5)

    for course in courses:
        pdf.multi_cell(0, 8, f"Title: {course['title']}\nDescription: {course['description']}\nLink: {course['link']}\n")
        pdf.ln(3)

    # User Query and Answers (Only if query is provided)
    if user_query:
        pdf.set_font("DejaVu", "", 10)
        pdf.cell(200, 10, "User Query & Relevant Answers", ln=True, align="L")
        pdf.ln(5)

        results = search_query(user_query)
        if results:
            for result in results:
                pdf.multi_cell(0, 8, f"Answer: {result['content']}\n")
                pdf.ln(3)
        else:
            pdf.cell(200, 8, "No relevant answers found.", ln=True, align="L")

    # Save PDF
    # **Fix: Sanitize the filename**
    safe_query = sanitize_filename(user_query) if user_query else "courses"
    pdf_filename = os.path.join(PDF_DIR, f"report_{safe_query}.pdf")
    pdf.output(pdf_filename, "F")

    return pdf_filename
