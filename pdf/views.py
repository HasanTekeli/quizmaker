
from django.contrib.auth.decorators import login_required
from reportlab.lib.units import mm, cm
from reportlab.platypus import (SimpleDocTemplate, Frame, PageTemplate, NextPageTemplate)

from django.db.models.base import ObjectDoesNotExist
from questions.models import Question, Exam, AnswerKey

# Dosyaları ayrıştırmak için eklenen bölüm:
from pdf.page_outline import PageOutline
from pdf.tools.conditional_spacer import ConditionalSpacer
from pdf.tools import set_options_acc_to_key
from pdf.tools.set_options_columns import set_option_column
from pdf.tools.prepare_groups import prepare_both_groups
from pdf.tools.set_first_page import first_page
from pdf.tools.set_later_pages import later_pages
from pdf.tools.set_texts import set_texts
from pdf.tools.set_frames import set_frames
# Dosya ayrıştırma bitiş


@login_required
def exportPDF(request, exam_id): #A Kitapçığı
	booklet_type = "A"
	exam_year, exam_semester, exam_ydl, e_type_upper, exam_session, get_questions = prepare_both_groups(request, exam_id, seed_number=2)
	###############################################################################
	# Cevap anahtarı girilmişse ona göre sırala,
	# yoksa tüm doğru cevaplar A şıkkı olsun.
	try:
		answers = AnswerKey.objects.get(get_exam_id=exam_id)
		a_answer = answers.answer_a
	except ObjectDoesNotExist:
		answers = 'AAAAAAAAAAAAAAAAAAAAAAAAA'
		a_answer = answers

	exam_info, pdfName = set_texts(exam_year, exam_semester, exam_ydl, e_type_upper, exam_session, booklet_type)

	page = PageOutline(exam_info, exam_session, booklet_type)
	
	def myFirstPage(canvas, doc):
		first_page(canvas, page, exam_info, exam_ydl, exam_session, booklet_type)


	def myLaterPages(canvas, doc):
		later_pages(canvas, page, booklet_type)
	
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

	# Sütun ayarlamaları
	elements = []
	set_frames(doc, myFirstPage, myLaterPages, elements, Frame, PageTemplate, NextPageTemplate)

	# Soru atamaları
	set_options_acc_to_key.set_options_on_a(get_questions, a_answer)

	set_option_column(get_questions, styles, elements, opt_2_que_spacer)
	doc.build(elements, onFirstPage=myFirstPage, onLaterPages=myLaterPages)
	
	return response


@login_required
def exportPDFb(request,exam_id): # B Kitapçığı
	booklet_type = "B"
	exam_year, exam_semester, exam_ydl, e_type_upper, exam_session, get_questions = prepare_both_groups(request,
																										exam_id,
																										seed_number=4)
	###############################################################################
	try:
		answers = AnswerKey.objects.get(get_exam_id=exam_id)
		b_answer = answers.answer_b
	except ObjectDoesNotExist:
		answers = 'AAAAAAAAAAAAAAAAAAAAAAAAA'
		b_answer = answers

	exam_info, pdfName = set_texts(exam_year, exam_semester, exam_ydl, e_type_upper, exam_session, booklet_type)

	page = PageOutline(exam_info, exam_session, booklet_type)

	def myFirstPage(canvas, doc):
		first_page(canvas, page, exam_info, exam_ydl, exam_session, booklet_type)

	def myLaterPages(canvas, doc):
		later_pages(canvas, page, booklet_type)

	# Style kısmı class-based oldu.
	page.pageStyle(pdfName)
	response, styles = page.pageStyle(pdfName)

	# Buraya adaptive spacer gibi birşey eklenecek
	if exam_ydl == "183" or exam_ydl == "184":
		opt_2_que_spacer = ConditionalSpacer(1*mm, 1*mm)
	else:
		opt_2_que_spacer = ConditionalSpacer(1*cm, 5*mm)
	
	##############################################
	doc = SimpleDocTemplate(response)
	
	# Sütun ayarlamaları
	elements = []
	set_frames(doc, myFirstPage, myLaterPages, elements, Frame, PageTemplate, NextPageTemplate)

	# Cevapları cevap anahtarına göre düzenleme
	set_options_acc_to_key.set_options_on_b(get_questions, b_answer)
	set_option_column(get_questions, styles, elements, opt_2_que_spacer)

	doc.build(elements, onFirstPage=myFirstPage, onLaterPages=myLaterPages)
	
	return response

