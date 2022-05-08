from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from reportlab.lib.units import mm, cm
from reportlab.platypus import (SimpleDocTemplate,
								Frame,
								PageTemplate, NextPageTemplate)
import random # soru karıştırma için
from django.db.models.base import ObjectDoesNotExist
from questions.models import Question, Exam, AnswerKey
# Dosyaları ayrıştırmak için eklenen bölüm:
from pdf.page_outline import PageOutline
from pdf.tools.conditional_spacer import ConditionalSpacer
from pdf.tools import options_on_key
from pdf.tools.options_columns import set_option_column
# Dosya ayrıştırma bitiş

font_bold = 'Times-New-Roman-Bold'
font = 'Times-New-Roman'

@login_required
def exportPDF(request,exam_id): #A Kitapçığı
	get_exam = get_object_or_404(Exam, id=exam_id)
	get_semester = str(get_exam.semester)
	get_session = get_exam.session
	exam_session = '{0}. Oturum'.format(get_session)
	exam_year = get_semester[-10:-1]
	exam_semester = get_semester[0:-12]
	e_type = get_exam.exam
	e_type_upper = e_type.upper()
	exam_ydl = get_exam.ydl
	#### Soruların belli bir düzende karıştırılması için eklenen / düzenlenen kısım
	get_ques_in_order = Question.objects.all().filter(exam_title_id=get_exam)
	#185 ve 186 da tüm soruları karıştır, 183-184'te son soru yerinde kalsın.
	if exam_ydl == "183" or exam_ydl == "184":
		list_of_ques = list(get_ques_in_order)
		ques_except_last = [x for i,x in enumerate(list_of_ques) if i!=24]
		last_que = list_of_ques.pop()
		list_of_ques_except_last = list(ques_except_last)
		random.seed(2)
		random.shuffle(list_of_ques_except_last)
		list_of_ques_except_last.append(last_que)
		get_questions = list(list_of_ques_except_last)
	else:
		get_questions = list(get_ques_in_order)
		random.seed(2)
		random.shuffle(get_questions)
	###############################################################################
	# Cevap anahtarı girilmişse ona göre sırala,
	# yoksa tüm doğru cevaplar A şıkkı olsun.
	try:
		answers = AnswerKey.objects.get(get_exam_id=exam_id)
		a_answer = answers.answer_a
	except ObjectDoesNotExist:
		answers = 'AAAAAAAAAAAAAAAAAAAAAAAAA'
		a_answer = answers
	
	booklet_type = "A"
	exam_info = '{0} {1} TERM YDL{2} {3} EXAM'.format(exam_year,exam_semester,exam_ydl[0:3],e_type_upper)
	pdfName = '{0} {1} TERM YDL{2} {3} EXAM {4} {5}.pdf'.format(exam_year,exam_semester,exam_ydl,e_type_upper,exam_session,booklet_type)

	header_font_size = 12

	page = PageOutline(exam_info, exam_session, booklet_type)
	
	def myFirstPage(canvas, doc):
		
		#Başlık (Sınav İsmi)
		canvas.setFont(font_bold, header_font_size)
		title4 = '{0}'.format(exam_info)
		canvas.saveState()

		#Burada class based olarak sayfanın tüm yapısı oluşturuluyor.
		page.outline1(canvas)
		canvas.saveState()
		#Burada class based olarak A kitapçığı 1.sayfaya özgü bölümler oluşturuluyor.
		page.bookletA1(canvas)
		
		#Başlık yazısı (Sınav İsmi)
		canvas.drawCentredString(290, 755, title4)

		# Oturum ve lisans önlisans bilgisi
		if exam_ydl == '183':
			pass
		elif exam_ydl == '184':
			pass
		else:
			canvas.setFont(font_bold, 10)
			canvas.roundRect(480,730,100,20,0,stroke=1,fill=0)
			canvas.line(550,730,550,750)
			canvas.drawString(490,737,exam_session)
			if exam_ydl == '185L':
				canvas.drawString(565,737,'L')
			elif exam_ydl == '186L':
				canvas.drawString(565,737,'L')
			else:
				canvas.drawString(565,737,' ')		

		canvas.saveState()
		canvas.restoreState()

	def myLaterPages(canvas, doc):
		#Burada class based olarak sayfa tablosu oluşturuluyor.
		page.outline2(canvas)
		canvas.saveState()
		#Burada class based olarak A kitapçığı 2.sayfaya özgü bölümler oluşturuluyor.
		page.bookletA2(canvas)
	
	# Style kısmı class-based oldu.
	page.pageStyle(pdfName)
	response, styles = page.pageStyle(pdfName)

	##############################################
	#Buraya adaptive spacer gibi birşey eklenecek
	if exam_ydl == "183" or exam_ydl == "184":
		opt_2_que_spacer = ConditionalSpacer(1*mm, 1*mm)
	else:
		opt_2_que_spacer = ConditionalSpacer(1*cm, 5*mm)
	
	##############################################
	doc = SimpleDocTemplate(response)
	
	#Sütun ayarlamaları
	frame1 = Frame(40, 30, 230, 560, id='col1')
	frame2 = Frame(310, 30, 260,560, id='col2')
	frame3 = Frame(20, 150, 270, 650, id='col3')
	frame4 = Frame(310, 150, 260,650, id='col4')
	
	# Sütun ekleme

	elements = []
	doc.addPageTemplates([PageTemplate(id='Page1',frames=[frame1,frame2],onPage=myFirstPage),])
	doc.addPageTemplates([PageTemplate(id='Page2',frames=[frame3,frame4],onPage=myLaterPages),])
	elements.append(NextPageTemplate('Page2'))
	# Soru atamaları
	options_on_key.set_options_on_a(get_questions, a_answer)

	set_option_column(get_questions, styles, elements, opt_2_que_spacer)
	doc.build(elements, onFirstPage=myFirstPage, onLaterPages=myLaterPages)
	
	return response

@login_required
def exportPDFb(request,exam_id): # B Kitapçığı
	get_exam = get_object_or_404(Exam, id=exam_id)
	get_semester = str(get_exam.semester)
	get_session = get_exam.session
	exam_session = '{0}. Oturum'.format(get_session)
	exam_year = get_semester[-10:-1]
	exam_semester = get_semester[0:-12]
	e_type = get_exam.exam
	e_type_upper = e_type.upper()
	exam_ydl = get_exam.ydl
	#### Soruların belli bir düzende karıştırılması için eklenen / düzenlenen kısım
	get_ques_in_order = Question.objects.all().filter(exam_title_id=get_exam)
	#185 ve 186 da tüm soruları karıştır, 183-184'te son soru yerinde kalsın.
	if exam_ydl == "183" or exam_ydl == "184":
		list_of_ques = list(get_ques_in_order)
		ques_except_last = [x for i,x in enumerate(list_of_ques) if i!=24]
		last_que = list_of_ques.pop()
		list_of_ques_except_last = list(ques_except_last)
		random.seed(4)
		random.shuffle(list_of_ques_except_last)
		list_of_ques_except_last.append(last_que)
		get_questions = list(list_of_ques_except_last)
	else:
		get_questions = list(get_ques_in_order)
		random.seed(4)
		random.shuffle(get_questions)
	###############################################################################
	try:
		answers = AnswerKey.objects.get(get_exam_id=exam_id)
		b_answer = answers.answer_b
	except ObjectDoesNotExist:
		answers = 'AAAAAAAAAAAAAAAAAAAAAAAAA'
		b_answer = answers
	
	booklet_type = "B"
	exam_info = '{0} {1} TERM YDL{2} {3} EXAM'.format(exam_year,exam_semester,exam_ydl[0:3],e_type_upper)
	pdfName = '{0} {1} TERM YDL{2} {3} EXAM {4} {5}.pdf'.format(exam_year,exam_semester,exam_ydl,e_type_upper,exam_session,booklet_type)
	header_font_size = 12
	
	page = PageOutline(exam_info, exam_session, booklet_type)

	def myFirstPage(canvas, doc):
		# Sınavı ismi
		canvas.setFont(font_bold, header_font_size)
		title4 = '{0}'.format(exam_info)
		canvas.saveState()
		
		# Burada class based olarak sayfanın tüm yapısı oluşturuluyor.
		page.outline1(canvas)
		canvas.saveState()
		
		# Burada class based olarak A kitapçığı 1.sayfaya özgü bölümler oluşturuluyor.
		page.bookletB1(canvas)

		# Başlık sınav ismi
		canvas.drawCentredString(290, 755, title4)

		# Oturum ve lisans önlisans bilgisi
		if exam_ydl == '183':
			pass
		elif exam_ydl == '184':
			pass
		else:
			canvas.setFont(font_bold, 10)
			canvas.roundRect(480,730,100,20,0,stroke=1,fill=0)
			canvas.line(550,730,550,750)
			canvas.drawString(490,737,exam_session)
			if exam_ydl == '185L':
				canvas.drawString(565,737,'L')
			elif exam_ydl == '186L':
				canvas.drawString(565,737,'L')
			else:
				canvas.drawString(565,737,' ')

		canvas.saveState()
		canvas.restoreState()

	def myLaterPages(canvas, doc):
		# Burada class based olarak sayfa tablosu oluşturuluyor.
		page.outline2(canvas)
		canvas.saveState()

		page.bookletB2(canvas)

	# Style kısmı class-based oldu.
	page.pageStyle(pdfName)
	response, styles = page.pageStyle(pdfName)
	

	#Buraya adaptive spacer gibi birşey eklenecek
	if exam_ydl == "183" or exam_ydl == "184":
		opt_2_que_spacer = ConditionalSpacer(1*mm, 1*mm)
	else:
		opt_2_que_spacer = ConditionalSpacer(1*cm, 5*mm)
	
	##############################################
	doc = SimpleDocTemplate(response)
	
	#Sütun ayarlamaları
	frame1 = Frame(40, 30, 230, 560, id='col1')
	frame2 = Frame(310, 30, 260,560, id='col2')
	frame3 = Frame(20, 150, 270, 650, id='col3')
	frame4 = Frame(310, 150, 260,650, id='col4')
	
	#Sütun ekleme
	elements = []
	doc.addPageTemplates([PageTemplate(id='Page1',frames=[frame1,frame2],onPage=myFirstPage),])
	doc.addPageTemplates([PageTemplate(id='Page2',frames=[frame3,frame4],onPage=myLaterPages),])
	elements.append(NextPageTemplate('Page2'))

	#Cevapları cevap anahtarına göre düzenleme
	options_on_key.set_options_on_b(get_questions, b_answer)
	set_option_column(get_questions, styles, elements, opt_2_que_spacer)

	
	doc.build(elements, onFirstPage=myFirstPage, onLaterPages=myLaterPages)
	
	return response

