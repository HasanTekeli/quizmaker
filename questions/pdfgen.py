from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import _baseFontName, _baseFontNameI, ParagraphStyle

styles = getSampleStyleSheet()
styleHeader = styles['Heading2']
styleN = styles['Normal']
styleH = styles['Heading1']
story = []
#add some flowables
story.append(Paragraph("ZONGULDAK BÜLENT ECEVİT UNIVERSITY<br />SCHOOL OF FOREIGN LANGUAGES",styleHeader))
story.append(Paragraph("This is a Heading",styleH))
story.append(Paragraph("This is a paragraph in <i>Normal</i> style.",
 styleN))
c = Canvas('mydoc.pdf')
f = Frame(mm, mm, 200*mm, 290*mm, showBoundary=1)
f.addFromList(story,c)
c.save()