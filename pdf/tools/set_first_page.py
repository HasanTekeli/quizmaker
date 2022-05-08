font_bold = 'Times-New-Roman-Bold'
font = 'Times-New-Roman'


def first_page(canvas, page, exam_info, exam_ydl, exam_session, booklet_type):
	header_font_size = 12
	# Başlık (Sınav İsmi)
	canvas.setFont(font_bold, header_font_size)
	title4 = '{0}'.format(exam_info)
	canvas.saveState()

	# Burada class based olarak sayfanın tüm yapısı oluşturuluyor.
	page.outline1(canvas)
	canvas.saveState()
	# Burada class based olarak A kitapçığı 1.sayfaya özgü bölümler oluşturuluyor.
	if booklet_type == 'A':
		page.bookletA1(canvas)
	else:
		page.bookletB1(canvas)

	# Başlık yazısı (Sınav İsmi)
	canvas.drawCentredString(290, 755, title4)

	# Oturum ve lisans önlisans bilgisi
	if exam_ydl == '183':
		pass
	elif exam_ydl == '184':
		pass
	else:
		canvas.setFont(font_bold, 10)
		canvas.roundRect(480, 730, 100, 20, 0, stroke=1, fill=0)
		canvas.line(550, 730, 550, 750)
		canvas.drawString(490, 737, exam_session)
		if exam_ydl == '185L':
			canvas.drawString(565, 737, 'L')
		elif exam_ydl == '186L':
			canvas.drawString(565, 737, 'L')
		else:
			canvas.drawString(565, 737, ' ')

	canvas.saveState()
	canvas.restoreState()
