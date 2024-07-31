import pandas as pd
from fpdf import FPDF
from Footer import footer

PDF_NAME = "dummy.pdf"


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)


data = pd.read_csv("topics.csv")
pdf.set_text_color(50, 50, 50)

num_page = 0
for index, row in data.iterrows():
    pdf.add_page()
    num_page += 1
    # Title
    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=0, h=0, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 15, 200, 15)
    # Footer
    footer(pdf, str(num_page))

    # Add pages
    for page in range(row["Pages"] - 1):
        pdf.add_page()
        num_page += 1
        # Footer
        footer(pdf, str(num_page))
    

pdf.output(PDF_NAME)