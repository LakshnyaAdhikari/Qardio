from fpdf import FPDF

def generate_pdf(result, probability, user_data, filename="Qardio_Report.pdf"):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 18)
    pdf.cell(200, 10, "Qardio Health Report", ln=True, align="C")

    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 10, f"Prediction Result: {result}", ln=True)
    pdf.cell(200, 10, f"Risk Probability: {probability:.2f}%", ln=True)

    pdf.ln(5)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, "User Input Data:", ln=True)

    pdf.set_font("Arial", "", 12)
    for key, value in user_data.items():
        pdf.cell(200, 8, f"{key}: {value}", ln=True)

    pdf.output(filename)
    return filename
