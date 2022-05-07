from django.http import HttpResponse
import reportlab
from reportlab.lib.units import mm, cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from pdf import strings
from django.conf import settings

from pdf.tools.qr_generator import qr_generator

reportlab.rl_config.TTFSearchPath.append(str(settings.BASE_DIR) + '/static/fonts')
static_folder = settings.BASE_DIR + '/static'

pdfmetrics.registerFont(
    TTFont('Times-New-Roman-Bold', 'TTimesb.ttf')
)
pdfmetrics.registerFont(
    TTFont('Times-New-Roman', 'times.ttf')
)
font_bold = 'Times-New-Roman-Bold'
font = 'Times-New-Roman'

dikkat = 'DİKKAT!!!'
booklet = 'KİTAPÇIK TÜRÜ'
pageWidth = 210*mm

def front_page(bookletType, canvas): # Ön Sayfa
    #Kitapçık türü
    canvas.drawCentredString(105,795,bookletType)
    #canvas.drawCentredString(485,795,bookletType)
    canvas.drawCentredString(465,795,bookletType)

    #Sayfa Altı Kitapçık türü
    canvas.drawCentredString(25,22,bookletType)
    canvas.drawCentredString(570,22,bookletType)
    if bookletType == 'A':
        canvas.roundRect(500,660,12,12,4,stroke=1,fill=1)
        canvas.roundRect(540,660,12,12,4,stroke=1,fill=0)
    else:
        canvas.roundRect(500,660,12,12,4,stroke=1,fill=0)
        canvas.roundRect(540,660,12,12,4,stroke=1,fill=1)

def back_page(bookletType, canvas): # Arka sayfa
    #Sayfa Altı Kitapçık türü
    canvas.drawCentredString(25,132,bookletType)
    canvas.drawCentredString(570,132,bookletType)
    
    #Sayfa üstü kitapçık türü
    canvas.drawCentredString(25,807,bookletType)
    canvas.drawCentredString(570,807,bookletType)

    #Sayfa altı kitapçık türü dolgulu yuvarlaklar
    if bookletType == 'A':
        canvas.roundRect(460,40,12,12,4,stroke=1,fill=1)
        canvas.roundRect(500,40,12,12,4,stroke=1,fill=0)
    else:
        canvas.roundRect(460,40,12,12,4,stroke=1,fill=0)
        canvas.roundRect(500,40,12,12,4,stroke=1,fill=1)


class PageOutline():
    def __init__(self, exam_info, exam_session, booklet_type):
        self.exam_info = exam_info
        self.exam_session = exam_session
        self.booklet_type = booklet_type

    def outline1(self, canvas):
        #Sayfa yapısı
        header_font_size = 12

        #Content
        title1 = strings.uni
        title2 = strings.school
        title3 = strings.department
        canvas.saveState()
        # Başlık kısmının çerçevesi:
        canvas.line(15,820,580,820) #Üst çizgi
        canvas.line(15,820,15,750) #Sol yan çizgi
        canvas.line(15,750,580,750) #Alt çizgi
        canvas.line(580,820,580,750) #Sağ çizgi

        #Başlık kısmı logo
        canvas.drawInlineImage(str(static_folder)+ '/img/logo.png', 20, 755, 60, 60)

        #####QR code generator
        #qr_generator(canvas, self.exam_info, self.exam_session, self.booklet_type)

        #30. yıl logosu
        canvas.drawInlineImage(str(static_folder)+ '/img/30.png', 485, 755, 90, 60)

        #Kitapçık türü çerçeveleri
        canvas.setFont(font_bold, 16)
        canvas.roundRect(95,790,20,20,2,stroke=1, fill=0)
        #canvas.roundRect(475,790,20,20,2,stroke=1, fill=0) #qr geldiğinde bu açılıp alttaki yoruma çevrilecek.
        canvas.roundRect(455,790,20,20,2,stroke=1, fill=0)

        #Başlık yazısı
        canvas.setFont(font_bold, header_font_size)
        canvas.drawCentredString(290, 800, title1)
        canvas.drawCentredString(290, 785, title2)
        canvas.drawCentredString(290, 770, title3)
		
        #İlk sütun açıklama
        text = canvas.beginText(30, 730) # Eklenecek metnin başlangıç ve bitiş koordinatlarını veriyor.
        text.setFont(font_bold, 12)
        text.setFillColor(colors.black)
        for line in strings.firstColumnText: #textLines içindeki satırları tek tek okuması için
            text.textLine(line)
        canvas.drawText(text)

        #İlk sütun öğrenci bilgileri
        text = canvas.beginText(20, 680) # Eklenecek metnin başlangıç ve bitiş koordinatlarını veriyor.
        text.setFont(font_bold, 11)
        text.setFillColor(colors.black)
        for line in strings.studentInfo: #textLines içindeki satırları tek tek okuması için
            text.textLine(line)
        canvas.drawText(text)

        #Öğrenci bilgileri çerçeve
        canvas.roundRect(15,645,240,50,0,stroke=1,fill=0)

        #Üst bölüm sütunlar arası çizgi
        canvas.line(260,750,260,640)
        #Sağ sütun bilgiler
        text = canvas.beginText(280, 730) # Eklenecek metnin başlangıç ve bitiş koordinatlarını veriyor.
        text.setFont(font_bold, 10)
        text.setFillColor(colors.black)
        for line in strings.secondColumnText: #textLines içindeki satırları tek tek okuması için
            text.textLine(line)
        canvas.drawText(text)

        #Sağ sütun altı çizili kelimelerin çizgileri
        canvas.line(412,727,454,727) #yumuşak
        canvas.line(280,715,360,715) #uçlu kurşun kalem
        canvas.line(346,655,450,655) #değerlendirilmeyecektir.

        #Dikkat Kitapçık türü
        canvas.setFont(font_bold, 14)
        canvas.drawString(490,710,dikkat) #Dikkat!!!
        canvas.setFont(font_bold, 10)
        canvas.drawString(485,695,booklet) #Kitapçık Türü
        canvas.roundRect(475,650,100,55,0,stroke=1,fill=0)
        canvas.line(475,690,575,690) #Kitapçık türü alt çizgi
        canvas.setFont(font_bold, 14)
        canvas.drawString(500,675,'A')
        canvas.drawString(540,675,'B')

        #Sayfa Altı Kitapçık türü ve sayfa numarası
        canvas.setFont(font_bold, 16)
        canvas.roundRect(15,18,20,20,2,stroke=1, fill=0)
        canvas.roundRect(560,18,20,20,2,stroke=1, fill=0)
        canvas.drawCentredString(pageWidth/2,22,'1')

        #Orta yazılı çizgi
        canvas.line(pageWidth/2,40,pageWidth/2,200)
        canvas.saveState()
        canvas.setFont(font, 10)
        canvas.rotate(90)

        canvas.drawString(205, -301,strings.department)
        canvas.restoreState()
        canvas.line(pageWidth/2,400,pageWidth/2,585)
        canvas.restoreState()

        # Soruların çerçevesi
        canvas.rect(15,40,565,600,stroke=1,fill=0)

		#Soru başlık kısmı
        canvas.drawString(23,620,'Circle the correct answer.')
        canvas.drawCentredString(pageWidth/2,600,'QUESTIONS')
        canvas.drawString(445,620,'Duration: 30 minutes')

        canvas.saveState()
        canvas.restoreState()

    def outline2(self, canvas):
        canvas.saveState()
		# Başlık kısmının çerçevesi:
        canvas.rect(15,150,565,650,stroke=1,fill=0) #2.Sayfa soru çerçevesi
        canvas.restoreState()
        #Orta yazılı çizgi 2.Sayfa
        canvas.line(pageWidth/2,150,pageWidth/2,320)
        canvas.saveState()
        canvas.setFont(font, 10)
        canvas.rotate(90)

        canvas.drawString(325, -301,strings.department)
        canvas.restoreState()
        canvas.line(pageWidth/2,520,pageWidth/2,800)
        canvas.saveState()
        canvas.restoreState()

        #Sayfa Altı Kitapçık türü ve sayfa numarası
        canvas.setFont(font_bold, 16)
        canvas.roundRect(15,128,20,20,2,stroke=1, fill=0)
        canvas.roundRect(560,128,20,20,2,stroke=1, fill=0)
        canvas.drawCentredString(pageWidth/2,132,'2')
        #Sayfa üstü kitapçık türü
        canvas.setFont(font_bold, 16)
        canvas.roundRect(15,803,20,20,2,stroke=1, fill=0)
        canvas.roundRect(560,803,20,20,2,stroke=1, fill=0)

        #2. Sayfa açıklama
        info_2ndpage_bottom = strings.info_2ndpage_bottom
        text = canvas.beginText(30,80) # Eklenecek metnin başlangıç ve bitiş koordinatlarını veriyor.
        text.setFont(font_bold, 10)
        text.setFillColor(colors.black)
        for line in info_2ndpage_bottom: #textLines içindeki satırları tek tek okuması için
            text.textLine(line)
        canvas.drawText(text)
        canvas.line(346,78,380,78)
        canvas.line(30,55,185,55) #Değerlendirilmeyecektir
        canvas.line(30,53,185,53) #Değerlendirilmeyecektir

        #Dikkat Kitapçık türü
        canvas.setFont(font_bold, 14)
        canvas.drawString(450,90,dikkat) #Dikkat!!!
        canvas.setFont(font_bold, 10)
        canvas.drawString(445,75,booklet) #Kitapçık Türü
        canvas.roundRect(435,30,100,55,0,stroke=1,fill=0)
        canvas.line(435,70,535,70) #Kitapçık türü alt çizgi
        canvas.setFont(font_bold, 14)
        canvas.drawString(460,55,'A')
        canvas.drawString(500,55,'B')

    def bookletA1(self, canvas):
        bookletType = "A"
        front_page(bookletType, canvas)
        
    def bookletA2(self, canvas):
        bookletType = "A"
        back_page(bookletType, canvas)

    def bookletB1(self, canvas):
        bookletType = "B"
        front_page(bookletType, canvas)

    def bookletB2(self, canvas):
        bookletType = "B"
        back_page(bookletType, canvas)

    def pageStyle(self,pdfName):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="{0}"'.format(pdfName)

        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Question', parent=styles['Normal'], fontName=font_bold, alignment=TA_JUSTIFY))
        styles.add(ParagraphStyle(name='Option', parent=styles['Normal'], fontName=font, alignment=TA_JUSTIFY))
        return response, styles

    