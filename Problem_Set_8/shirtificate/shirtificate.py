from fpdf import FPDF
import sys

if len(sys.argv) == 2:
    user_input = sys.argv[1]
else:
    user_input = input("Name: ")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", style="B", size=48)
pdf.cell(210, 50, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")

pdf.image("shirtificate.png", w=180, x=15, y=70)
pdf.set_font("helvetica", style="B", size=23)
pdf.set_text_color(255, 255, 255)
pdf.cell(200, 150, f"{user_input} took CS50", new_x="LMARGIN", new_y="NEXT", align="C")

pdf.output("shirtificate.pdf")
