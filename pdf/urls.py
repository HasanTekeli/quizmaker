from django.urls import path
from django.urls import re_path as url
from . import views

app_name='pdf'

urlpatterns = [
    url(r'^export/(?P<exam_id>[-\w]+)/$', views.exportPDF, name='exam_export'),
    url(r'^export/(?P<exam_id>[-\w]+)/b/$', views.exportPDFb, name='exam_export_b'),
]