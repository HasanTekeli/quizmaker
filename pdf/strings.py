from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_JUSTIFY

font_bold = 'Times-New-Roman-Bold'

uni = 'ZONGULDAK BÜLENT ECEVİT UNIVERSITY'
school = 'SCHOOL OF FOREIGN LANGUAGES'
department = 'DEPARTMENT OF FOREIGN LANGUAGES'

paragraph_style_12 = ParagraphStyle("P12",
									fontName=font_bold,
									fontSize=12,
									alignment=TA_JUSTIFY
									)

paragraph_style_11 = ParagraphStyle("P11",
									fontName=font_bold,
									fontSize=11,
									alignment=TA_JUSTIFY,
									leading=14
									)

paragraph_style_10 = ParagraphStyle("P10",
									fontName=font_bold,
									fontSize=10,
									alignment=TA_JUSTIFY,
									leading=13
									)

firstColumnTextP = Paragraph('''Soru kitapçıklarınızın üzerindeki isim / soy 
								isim, okul numarası ve bölüm kısımlarını
								doldurmayı unutmayınız.''', paragraph_style_12)

studentInfoP = Paragraph('''Name / Surname: <br/>
	Number:<br/>
	Department:''', paragraph_style_11)


secondColumnTextP = Paragraph('''
	Lütfen  kodlama  için   sadece   <u>yumuşak 
	uçlu kurşun kalem</u> kullanınız. <br/><br/>
	Soru    kitapçıkları     üzerindeki     soru
	kitapçık türünü (A / B)  optik  formdaki
	ilgili   alana   kodlamayan   öğrencilerin
	sınav sonuçları <u>değerlendirilmeyecektir.</u>''', paragraph_style_10)


info_2ndpage_bottomP = Paragraph('''
	SORU  KİTAPÇIKLARI  ÜZERİNDEKİ  SORU  KİTAPÇIK TÜRÜNÜ  <u>( A / B )</u>  OPTİK
	FORMDAKİ İLGİLİ ALANA KODLAMAYAN ÖĞRENCİLERİN SINAV SONUÇLARI
	<u>DEĞERLENDİRİLMEYECEKTİR</u>.''', paragraph_style_11)
