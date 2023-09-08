from fpdf import FPDF

# class PDF(FPDF):
#     def header(self):
#         self.set_font("Courier", "B", 15)
#         self.cell(80)
#         self.cell(30, 10, "CS50 Shirtificate", border=1, align="C")
#         self.ln(20)
name = input("Name: ")


pdf = FPDF()
pdf.add_page()
pdf.image("shirtificate.png", 10, 50, 180)
pdf.set_font("Courier", "B", 30)
pdf.cell(190, 10, "CS50 Shirtificate", new_x ="LMARGIN", new_y="NEXT", align="C")
pdf.set_text_color(255, 255, 255)
pdf.cell(190, 150, name + " took CS50", new_x ="LMARGIN", new_y="NEXT", align="C")
pdf.output("shirtificate.pdf")