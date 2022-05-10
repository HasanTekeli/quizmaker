from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView, TemplateView
from django.forms import modelformset_factory, Textarea, TextInput
from django.http import JsonResponse

from .models import Question, Exam


class HomeView(TemplateView):
    template_name = 'home.html'


class ExamListView(LoginRequiredMixin,ListView):
    model = Exam
    context_object_name = 'exams'
    template_name = 'mc/exam_list.html'

    def get_queryset(self):
        queryset = super(ExamListView, self).get_queryset().filter(is_archived=False)
        return queryset


class ArchivedExamListView(LoginRequiredMixin, ListView):
    model = Exam
    context_object_name = 'exams'
    template_name = 'mc/exam_list.html'

    def get_queryset(self):
        queryset = super(ArchivedExamListView, self).get_queryset().filter(is_archived=True)
        return queryset


def archive_exam(request, exam_id):
    is_archived = request.GET.get('is_archived', True)
    exam = Exam.objects.get(id=exam_id)
    try:
        exam.is_archived = is_archived
        exam.save()
        return HttpResponseRedirect(reverse('quiz:exam_list'))
    except Exception as e:
        return JsonResponse({"success": False})


@login_required
def exam_detail(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    question = Question.objects.all().filter(exam_title_id=exam_id)
    return render(request, 'mc/exam_detail.html', context={'exam':exam, 'question':question})

@login_required
def exam_detail_update(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    QuestionFormSet = modelformset_factory(Question,
                                           fields=('question', 'option1',
                                                   'option2', 'option3',
                                                   'option4', 'columns', 'row_height'),
                                           widgets={
                                            'question': Textarea(attrs={'cols': 50, 'rows': 3}),
                                            'option1': TextInput(attrs={'placeholder': 'Doğru cevabı buraya yazın'})},
                                           extra=25,
                                           max_num=25)

    if request.method == 'POST':
        formset = QuestionFormSet(request.POST, queryset=Question.objects.filter(exam_title__id=exam.id))
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.exam_title_id = exam.id
                instance.save()
            
            return HttpResponseRedirect(reverse('quiz:exam_detail', args=[exam.id]))
        
    else:
        formset = QuestionFormSet(queryset=Question.objects.filter(exam_title__id=exam.id))
        return render(request, 'mc/exam_detail_update.html', {'exam': exam, 'formset': formset})

 