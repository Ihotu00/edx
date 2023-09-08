from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Courier", "B", 15)
        self.cell(80)
        self.cell(30, 10, "CS50 Shirtificate", border=1, align="C")
        self.ln(20)

pdf = PDF()
pdf.add_page()
pdf.set_font("Courier", size=12)