import reportlab
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from django.conf import settings

reportlab.rl_config.TTFSearchPath.append(str(settings.BASE_DIR) + '/static/fonts')
static_folder = settings.BASE_DIR + '/static'

pdfmetrics.registerFont(
    TTFont('Times-New-Roman-Bold', 'TTimesb.ttf')
)
pdfmetrics.registerFont(
   	TTFont('Times-New-Roman', 'times.ttf')
)

