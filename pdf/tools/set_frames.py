def set_frames(doc, myFirstPage, myLaterPages, elements, Frame, PageTemplate, NextPageTemplate):
	# Sütun ayarlamaları
	frame1 = Frame(40, 30, 230, 560, id='col1')
	frame2 = Frame(310, 30, 260, 560, id='col2')
	frame3 = Frame(20, 150, 270, 650, id='col3')
	frame4 = Frame(310, 150, 260, 650, id='col4')

	doc.addPageTemplates([PageTemplate(id='Page1', frames=[frame1, frame2], onPage=myFirstPage), ])
	doc.addPageTemplates([PageTemplate(id='Page2', frames=[frame3, frame4], onPage=myLaterPages), ])
	elements.append(NextPageTemplate('Page2'))