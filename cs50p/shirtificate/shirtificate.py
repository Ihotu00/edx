from fpdf import FPDF

name = input("Name: ")
pdf = FPDF()
pdf.add_page()
pdf.image("shirtificate.png", 10, 50, 180)
pdf.set_font("Courier", "B", 30)
pdf.cell(190, 10, "CS50 Shirtificate", new_x ="LMARGIN", new_y="NEXT", align="C")
pdf.set_text_color(255, 255, 255)
pdf.cell(190, 150, name + " took CS50", new_x ="LMARGIN", new_y="NEXT", align="C")
pdf.output("shirtificate.pdf")
