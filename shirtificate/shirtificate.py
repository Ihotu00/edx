from fpdf import FPDF

# class PDF(FPDF):
#     def header(self):
#         self.set_font("Courier", "B", 15)
#         self.cell(80)
#         self.cell(30, 10, "CS50 Shirtificate", border=1, align="C")
#         self.ln(20)

pdf = FPDF()
pdf.add_page()
pdf.image("shirtificate.png", 0, 0, 80)
pdf.output("shirtificate.pdf")