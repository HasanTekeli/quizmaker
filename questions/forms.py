from django import forms
from django.forms import ModelForm, Textarea, RadioSelect, formset_factory, TextInput
from .models import Exam, AnswerKey


class CustomSelect(forms.Select):
    option_inherits_attrs = True


class AnswerKeyForm(forms.ModelForm):
    class Meta:
        model = AnswerKey
        fields = ('answer_a','answer_b')
        widgets = {
            'answer_a': Textarea(attrs={
                                    'cols': 50,
                                    'rows': 1,
                                    'placeholder': "25 cevabı buraya sırayla girin"}),
            'answer_b': Textarea(attrs={
                                    'cols': 50,
                                    'rows': 1,
                                    'placeholder': "25 cevabı buraya sırayla girin"}),

        }


        