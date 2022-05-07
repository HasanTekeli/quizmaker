from django.contrib import admin
from .models import Exam,Question,Year,Semester,AnswerKey
# Register your models here.
admin.site.register(Year)
admin.site.register(Semester)
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(AnswerKey)