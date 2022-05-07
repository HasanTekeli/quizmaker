#####QR code generator
from reportlab.graphics import renderPDF
from reportlab.graphics.barcode import qr
from reportlab.graphics.shapes import Drawing

def qr_generator(canvas, exam_info, exam_session, booklet_type):
    # Fonksiyonun içi views.py 104. satırdan alındı.
    generated_qr = qr.QrCodeWidget(exam_info+exam_session+' '+booklet_type)
    bounds = generated_qr.getBounds()
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    d = Drawing(60,60,transform=[60./width,0,0,60./height,0,0])
    d.add(generated_qr)
    renderPDF.draw(d, canvas, 520, 755) #qrcode
