'''
This script takes original.pdf as template and
adds records from list.csv to specific location
to generare multiple pdfs with records as filename
in the same directory
'''


from pyPdf import PdfFileWriter, PdfFileReader
import StringIO
from reportlab.pdfgen import canvas

# To register a specific font
# from reportlab.pdfbase import pdfmetrics
# from reportlab.pdfbase.ttfonts import TTFont
# pdfmetrics.registerFont(TTFont('Allura', 'Allura.ttf'))

for line in open('list.csv'):
	packet = StringIO.StringIO()
	# create a new PDF with Reportlab
	can = canvas.Canvas(packet, (864, 608.9))
	can.setFillColorRGB(0,0,100/256)
	can.setFont("Allura", 40)
	can.drawCentredString(432, 240, line)
	can.save()

	#move to the beginning of the StringIO buffer
	packet.seek(0)
	new_pdf = PdfFileReader(packet)
	# read your existing PDF
	existing_pdf = PdfFileReader(file("original.pdf", "rb"))
	output = PdfFileWriter()
	page = existing_pdf.getPage(0)
	page.mergePage(new_pdf.getPage(0))
	output.addPage(page)
	# finally, write "output" to a real file
	outputStream = file(line[:-1]+".pdf", "wb")
	output.write(outputStream)
	outputStream.close()
