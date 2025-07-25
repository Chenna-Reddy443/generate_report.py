from fpdf import FPDF

def create_pdf(data):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Weather Report", ln=True, align='C')
    pdf.ln(10)

    for key, value in data.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

    pdf.image("weather_chart.png", x=30, y=60, w=150)
    pdf.output("Weather_Report.pdf")
