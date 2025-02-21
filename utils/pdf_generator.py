from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def generate_pdf(file_path: str, title: str, content: str):
    """
    Gera um PDF com um template simples contendo elementos temáticos de anime.
    """
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    # Cabeçalho com o título
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2, height - 50, title)
    
    # Corpo do PDF com o conteúdo
    c.setFont("Helvetica", 12)
    text_object = c.beginText(50, height - 100)
    text_object.textLines(content)
    c.drawText(text_object)
    
    # Rodapé temático
    c.setFont("Helvetica-Oblique", 10)
    c.drawCentredString(width / 2, 30, "Anime Productivity - Gerado com ReportLab")
    
    c.showPage()
    c.save()