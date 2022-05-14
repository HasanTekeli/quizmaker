from django.http import HttpResponse
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from pdf import strings
from pdf.tools.set_booklet_info_table import booklet_info_table
from pdf.tools.qr_generator import qr_generator
from django.conf import settings

static_folder = settings.BASE_DIR + '/static'

font_bold = 'Times-New-Roman-Bold'
font = 'Times-New-Roman'

pageWidth = 210*mm


class PageOutline():
    def __init__(self, exam_info, exam_session, booklet_type, right_logo):
        self.exam_info = exam_info
        self.exam_session = exam_session
        self.booklet_type = booklet_type
        self.right_logo = right_logo

    def outline1(self, canvas):
        # Sayfa yapısı
        header_font_size = 12

        # Content
        title1 = strings.uni
        title2 = strings.school
        title3 = strings.department
        canvas.saveState()
        # Başlık kısmının çerçevesi:
        canvas.rect(15, 750, 565, 70) #sol, alt, en, boy

        # Başlık kısmı logo
        canvas.drawInlineImage(str(static_folder)+ '/img/left_logo.png', 20, 755, 60, 60)

        # Kitapçık türü
        canvas.drawCentredString(105, 795, self.booklet_type)
        #

        if self.right_logo == "QR":
            qr_generator(canvas, self.exam_info, self.exam_session, self.booklet_type)
            canvas.drawCentredString(485, 795, self.booklet_type)
            canvas.roundRect(475, 790, 20, 20, 2, stroke=1, fill=0)
        elif self.right_logo == "LOGO":
            canvas.drawInlineImage(str(static_folder)+ '/img/right_logo.png', 485, 755, 90, 60)
            canvas.drawCentredString(465, 795, self.booklet_type)
            canvas.roundRect(455, 790, 20, 20, 2, stroke=1, fill=0)
        else:
            canvas.drawCentredString(485, 795, self.booklet_type)
            canvas.roundRect(475, 790, 20, 20, 2, stroke=1, fill=0)

        # Üst Başlık Kitapçık türü çerçeveleri
        canvas.setFont(font_bold, 16)
        canvas.roundRect(95, 790, 20, 20, 2, stroke=1, fill=0)

        # Başlık yazısı
        canvas.setFont(font_bold, header_font_size)
        canvas.drawCentredString(290, 800, title1)
        canvas.drawCentredString(290, 785, title2)
        canvas.drawCentredString(290, 770, title3)

        # İlk sütun açıklama
        firstColumnText = strings.firstColumnTextP
        firstColumnText.wrapOn(canvas, 230, 50)
        firstColumnText.drawOn(canvas, 25, 705)

        # Öğrenci bilgileri çerçeve
        canvas.roundRect(15, 645, 240, 50, 0, stroke=1, fill=0)
        # İlk sütun öğrenci bilgileri
        student_info = strings.studentInfoP
        student_info.wrapOn(canvas, 230, 100)
        student_info.drawOn(canvas, 25, 650)

        # Üst bölüm sütunlar arası çizgi
        canvas.line(260, 750, 260, 640)

        # Sağ sütun bilgiler
        second_column_text = strings.secondColumnTextP
        second_column_text.wrapOn(canvas, 195, 110)
        second_column_text.drawOn(canvas, 270, 650)

        ########################
        # Dikkat Kitapçık türü
        booklet_info_table(canvas, font_bold, "front")

        ###############################

        #Sayfa Altı Kitapçık türü ve sayfa numarası
        canvas.setFont(font_bold, 16)
        canvas.roundRect(15, 18, 20, 20, 2, stroke=1, fill=0)
        canvas.roundRect(560, 18, 20, 20, 2, stroke=1, fill=0)
        canvas.drawCentredString(pageWidth/2, 22, '1')

        #Orta yazılı çizgi
        canvas.line(pageWidth / 2, 40, pageWidth / 2, 585)
        canvas.saveState()
        canvas.setFont(font, 10)
        #### Orta yazının arka plan rengini beyaz yapmak için dikdörtgen ###
        # 1. Sayfa
        canvas.setFillColorRGB(255, 255, 255)
        canvas.rect(291, 200, 12, 200, stroke=0, fill=1)
        # 291: sayfanın solundan uzaklık
        # 200: sayfanın altından uzaklık
        # 12: En
        # 200: Boy
        canvas.setFillColorRGB(0, 0, 0)
        ########
        canvas.rotate(90)

        canvas.drawString(205, -301, strings.department)
        canvas.restoreState()
        canvas.restoreState()

        # Soruların çerçevesi
        canvas.rect(15, 40, 565, 600, stroke=1, fill=0)

        # Soru başlık kısmı
        canvas.drawString(23, 620, 'Circle the correct answer.')
        canvas.drawCentredString(pageWidth/2, 600, 'QUESTIONS')
        canvas.drawString(445, 620, 'Duration: 30 minutes')

        canvas.saveState()
        canvas.restoreState()

    def outline2(self, canvas):
        canvas.saveState()
        # Başlık kısmının çerçevesi:
        canvas.rect(15, 150, 565, 650, stroke=1, fill=0) #2.Sayfa soru çerçevesi
        canvas.restoreState()
        #Orta yazılı çizgi 2.Sayfa
        canvas.line(pageWidth / 2, 150, pageWidth / 2, 800)
        canvas.saveState()
        canvas.setFont(font, 10)
        #### Orta yazının arka plan rengini beyaz yapmak için dikdörtgen ###
        # 2. Sayfa
        canvas.setFillColorRGB(255, 255, 255)
        canvas.rect(291, 320, 12, 200, stroke=0, fill=1)
        # 291: sayfanın solundan uzaklık
        # 320: sayfanın altından uzaklık
        # 12: En
        # 200: Boy
        canvas.setFillColorRGB(0, 0, 0)
        ########
        canvas.rotate(90)
        canvas.drawString(325, -301, strings.department)
        canvas.restoreState()
        canvas.saveState()
        canvas.restoreState()

        #Sayfa Altı Kitapçık türü ve sayfa numarası
        canvas.setFont(font_bold, 16)
        canvas.roundRect(15, 128, 20, 20, 2, stroke=1, fill=0)
        canvas.roundRect(560, 128, 20, 20, 2, stroke=1, fill=0)
        canvas.drawCentredString(pageWidth/2, 132, '2')
        #Sayfa üstü kitapçık türü
        canvas.setFont(font_bold, 16)
        canvas.roundRect(15, 803, 20, 20, 2, stroke=1, fill=0)
        canvas.roundRect(560, 803, 20, 20, 2, stroke=1, fill=0)

        #2. Sayfa açıklama
        info_2ndpage_bottom = strings.info_2ndpage_bottomP
        info_2ndpage_bottom.wrapOn(canvas, 430, 40)
        info_2ndpage_bottom.drawOn(canvas, 25, 40)

        # Dikkat Kitapçık türü yazan tablo
        booklet_info_table(canvas, font_bold, "back")

    def front_page(self, booklet_type, canvas):  # Ön Sayfa
        # Sayfa Altı Kitapçık türü
        canvas.drawCentredString(25, 22, booklet_type)
        canvas.drawCentredString(570, 22, booklet_type)

        if booklet_type == 'A':
            canvas.roundRect(504, 660, 12, 12, 4, stroke=1, fill=1)
            canvas.roundRect(544, 660, 12, 12, 4, stroke=1, fill=0)
        else:
            canvas.roundRect(504, 660, 12, 12, 4, stroke=1, fill=0)
            canvas.roundRect(544, 660, 12, 12, 4, stroke=1, fill=1)

    def back_page(self, booklet_type, canvas):  # Arka sayfa
        # Sayfa Altı Kitapçık türü
        canvas.drawCentredString(25, 132, booklet_type)
        canvas.drawCentredString(570, 132, booklet_type)

        # Sayfa üstü kitapçık türü
        canvas.drawCentredString(25, 807, booklet_type)
        canvas.drawCentredString(570, 807, booklet_type)

        # Sayfa altı kitapçık türü dolgulu yuvarlaklar

        if booklet_type == 'A':
            canvas.roundRect(504, 40, 12, 12, 4, stroke=1, fill=1)
            canvas.roundRect(544, 40, 12, 12, 4, stroke=1, fill=0)
        else:
            canvas.roundRect(504, 40, 12, 12, 4, stroke=1, fill=0)
            canvas.roundRect(544, 40, 12, 12, 4, stroke=1, fill=1)

    def bookletA1(self, canvas):
        bookletType = "A"
        self.front_page(bookletType, canvas)
        
    def bookletA2(self, canvas):
        bookletType = "A"
        self.back_page(bookletType, canvas)

    def bookletB1(self, canvas):
        bookletType = "B"
        self.front_page(bookletType, canvas)

    def bookletB2(self, canvas):
        bookletType = "B"
        self.back_page(bookletType, canvas)

    def pageStyle(self, pdfName):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="{0}"'.format(pdfName)

        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Question', parent=styles['Normal'], fontName=font_bold, alignment=TA_JUSTIFY))
        styles.add(ParagraphStyle(name='Option', parent=styles['Normal'], fontName=font, alignment=TA_JUSTIFY))
        return response, styles

    