
def footer(pdf, footer_text:str):
    pdf.ln(278)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.cell(w=0, h=10, txt=footer_text, align="R")