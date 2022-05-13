def set_texts(exam_year, exam_semester, exam_ydl, e_type_upper, exam_session, booklet_type):
	exam_info = '{0} {1} TERM YDL{2} {3} EXAM'.format(exam_year,
													  exam_semester,
													  exam_ydl[0:3],
													  e_type_upper)
	pdf_name = '{0} {1} TERM YDL{2} {3} EXAM {4} {5}.pdf'.format(exam_year,
																exam_semester,
																exam_ydl,
																e_type_upper,
																exam_session,
																booklet_type)
	return exam_info, pdf_name
