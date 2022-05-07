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

#Bu q2 neden orada anlamadım. 
# Sonradan sıkıntı çıkarsa diye burada dursun.
# aldığım yer: exportpdfb'nin sonundaki else'in 
# başında idi. reference verilen yer ise:
# else'in sonundaki q.setStyle(q2_table_style)
q2_table_style = TableStyle([
						('TEXTCOLOR',(0,0),(-1,-1),colors.black),
						('ALIGN',(1,0),(-1,-1),'LEFT'),
						('BACKGROUND', (0,0),(0,1), colors.blue),
						('ALIGN',(0,0),(0,-1),'LEFT'),
						('VALIGN',(0,0),(0,-1),'TOP'),
						('LEFTPADDING',(0,0),(-1,-1),0),
						
						
						#('BOX',(0,0),(-1,-1),0.25,colors.black),
						#('INNERGRID',(0,0),(-1,-1),0.25,colors.black),
						])