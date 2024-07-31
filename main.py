import pandas as pd
from fpdf import FPDF

PDF_NAME = "dummy.pdf"


pdf = FPDF(orientation="P", 
           unit="mm",
           format="A4")

data = pd.read_csv("topics.csv")
pdf.set_font(family="Times", style="B", size=24)
pdf.set_text_color(50, 50, 50)
for index, row in data.iterrows():
    pdf.add_page()
    pdf.cell(w=0, h=0,
             txt=row["Topic"],
             align="L", ln=1)
    pdf.line(10, 15, 200, 15)
    # Add pages
    for page in range(row["Pages"] - 1):
        pdf.add_page()


pdf.output(PDF_NAME)