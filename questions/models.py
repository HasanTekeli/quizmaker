from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Year(models.Model):
    year = models.CharField(max_length=9, blank=True,
                    unique=True, null=True)

    class Meta:
        verbose_name = _("Yıl")
        verbose_name_plural = _("Yıllar")

    def __str__(self):
        return self.year


class Semester(models.Model):
    SEM_CHOICES = (
        ('FALL', 'Güz'),
        ('SPRING', 'Bahar')
    )
    semester = models.CharField(max_length=7, choices=SEM_CHOICES, null=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE, default="")

    class Meta:
        verbose_name=_("Dönem")
        verbose_name_plural=_("Dönemler")
    
    def __str__(self):
        return "{0} ({1})".format(self.semester, self.year)


class Exam(models.Model):
    EXAM_CHOICES = (
        ('Midterm', 'Midterm'),
        ('Midterm Makeup', 'Midterm_Makeup'),
        ('Final', 'Final'),
        ('Final Makeup', 'Final_Makeup'),
    )
    YDL_CHOICES = (
        ('183', '183'),
        ('184', '184'),
        ('185', '185 Önlisans'),
        ('185L', '185 Lisans'),
        ('186', '186 Önlisans'),
        ('186L', '186 Lisans'),
    )
    BOOKLET_CHOICES = (
        ('A', 'A'),
        ('B', 'B')
    )
    SESSION_CHOICES = (
        ('1', '1. Oturum'),
        ('2', '2. Oturum')
    ) 
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True)
    exam = models.CharField(max_length=15, choices=EXAM_CHOICES, null=True,
                            verbose_name=_("Sınav Seçimi"), default="Midterm")
    ydl = models.CharField(max_length=4, choices=YDL_CHOICES, null=True, 
                            verbose_name=_("YDL183,184,etc."))
    session = models.CharField(max_length=1, choices=SESSION_CHOICES, null=True,
                            verbose_name=_("Oturum"))
    exam_title = "{0} {1} {2}".format(semester,exam,ydl)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return "{0} {1} {2} {3}".format(self.semester,self.exam,self.ydl,self.session)

    def get_absolute_url(self):
        return reverse('quiz:exam_detail', args=[int(self.id)])


class Question(models.Model):
    COL_CHOICES = (
        ('1', '1 sütun'),
        ('2', '2 sütun'),
        ('4', '4 sütun')
    )
    exam_title = models.ForeignKey(Exam, related_name='examfk', on_delete=models.CASCADE, default="")
    question = models.TextField(max_length=4000, blank=True, verbose_name=_("Soru"), default="")
    option1 = models.CharField(max_length=200, blank=True, verbose_name=_("1.Seçenek"), default="")
    option2 = models.CharField(max_length=200, blank=True, verbose_name=_("2.Seçenek"), default="")
    option3 = models.CharField(max_length=200, blank=True, verbose_name=_("3.Seçenek"), default="")
    option4 = models.CharField(max_length=200, blank=True, verbose_name=_("4.Seçenek"), default="")
    columns = models.CharField(max_length=1, choices=COL_CHOICES, default="1")
    option_temp = models.CharField(max_length=200, blank=True, verbose_name=_("GeçiciSeçenek"), default="")
    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return "/questions/%s" % self.id


class AnswerKey(models.Model):
    get_exam = models.ForeignKey(Exam, related_name="examfk2", on_delete=models.CASCADE,default="")
    answer_a = models.CharField(max_length=25, verbose_name=_("A Kitapçığı Cevapları"), default="")
    answer_b = models.CharField(max_length=25, verbose_name=_("B Kitapçığı Cevapları"), default="")

    def __str__(self):
        return '{0}'.format(self.get_exam)


