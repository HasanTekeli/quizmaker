from django.shortcuts import get_object_or_404
import random

from questions.models import Question, Exam


def prepare_both_groups(request, exam_id, seed_number):
    get_exam = get_object_or_404(Exam, id=exam_id)
    get_semester = str(get_exam.semester)
    get_session = get_exam.session
    exam_session = '{0}. Oturum'.format(get_session)
    exam_year = get_semester[-10:-1]
    exam_semester = get_semester[0:-12]
    e_type = get_exam.exam
    e_type_upper = e_type.upper()
    exam_ydl = get_exam.ydl
    right_logo = get_exam.right_logo

    #### Soruların belli bir düzende karıştırılması için eklenen / düzenlenen kısım
    get_ques_in_order = Question.objects.all().filter(exam_title_id=get_exam)
    # 185 ve 186 da tüm soruları karıştır, 183-184'te son soru yerinde kalsın.
    if exam_ydl == "183" or exam_ydl == "184":
        list_of_ques = list(get_ques_in_order)
        ques_except_last = [x for i, x in enumerate(list_of_ques) if i != 24]
        try:  # Hiç soru eklenmemişse hata vermemesi için try except blokunda
            last_que = list_of_ques.pop()
        except IndexError:
            pass
        list_of_ques_except_last = list(ques_except_last)
        random.seed(seed_number)
        random.shuffle(list_of_ques_except_last)
        try:  # Hiç soru eklenmemişse hata vermemesi için try except blokunda
            list_of_ques_except_last.append(last_que)
        except UnboundLocalError:
            pass
        get_questions = list(list_of_ques_except_last)
    else:
        get_questions = list(get_ques_in_order)
        random.seed(seed_number)
        random.shuffle(get_questions)
    return exam_year, exam_semester, exam_ydl, e_type_upper, exam_session, get_questions, right_logo
