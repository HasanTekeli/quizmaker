from reportlab.platypus import TableStyle
from reportlab.lib import colors

q_table_style = TableStyle([
						('TEXTCOLOR',(0,0),(-1,-1),colors.black),
						('ALIGN',(1,0),(-1,-1),'LEFT'),
						('ALIGN',(0,0),(0,-1),'LEFT'),
						('VALIGN',(0,0),(0,-1),'TOP'),
						('COLWIDTHS',(0,0),(0,-1),20),
						('LEFTPADDING',(0,0),(-1,-1),0),
						])
o_table_style = TableStyle([
						('TEXTCOLOR',(0,0),(-1,-1),colors.black),
						('ALIGN',(0,0),(-1,-1),'LEFT'),
						('VALIGN',(0,0),(-1,-1),'TOP'),
						('LEFTPADDING',(0,0),(-1,-1),0),
						('BOTTOMPADDING',(0,0),(-1,0),-1),
						])