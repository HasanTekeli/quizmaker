#views.py'dan alınanlar:
# Line 97-98:
exam_info = '{0} {1} TERM YDL{2} {3} EXAM'.format(exam_year,exam_semester,exam_ydl[0:3],e_type_upper)
pdfName = '{0} {1} TERM YDL{2} {3} EXAM {4} {5}.pdf'.format(exam_year,exam_semester,exam_ydl,e_type_upper,exam_session,bookletType)

# Line 101:
header_font_size = 12