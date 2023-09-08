from fpdf import FPDF

# class PDF(FPDF):
#     def header(self):
#         self.set_font("Courier", "B", 15)
#         self.cell(80)
#         self.cell(30, 10, "CS50 Shirtificate", border=1, align="C")
#         self.ln(20)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Courier", "B", 30)
pdf.cell(100, 10, "CS50 Shirtificate", align="C")
pdf.image("shirtificate.png", 10, 50, 180)
# pdf.cell()
pdf.output("shirtificate.pdf")