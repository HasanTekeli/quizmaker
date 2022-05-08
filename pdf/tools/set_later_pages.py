def later_pages(canvas, page, booklet_type):
	# Burada class based olarak sayfa tablosu oluşturuluyor.
	page.outline2(canvas)
	canvas.saveState()
	# Burada class based olarak A kitapçığı 2.sayfaya özgü bölümler oluşturuluyor.
	if booklet_type == 'A':
		page.bookletA2(canvas)
	else:
		page.bookletB2(canvas)