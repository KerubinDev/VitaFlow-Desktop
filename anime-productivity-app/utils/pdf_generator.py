from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def generate_pdf(report_data, filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 24)
    c.drawString(100, height - 50, "Relatório de Produtividade")

    # Draw a line
    c.setStrokeColor(colors.black)
    c.line(50, height - 60, width - 50, height - 60)

    # Add report data
    c.setFont("Helvetica", 12)
    y_position = height - 80
    for key, value in report_data.items():
        c.drawString(100, y_position, f"{key}: {value}")
        y_position -= 20

    # Save the PDF
    c.save()