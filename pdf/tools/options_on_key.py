import copy

# Soruları girilen cevap anahtarına göre sıralama.
# option_temp fazladan bir seçenek koyma yeri,
# oraya kes yapıştır yaparak yerlerini değiştiriyor.

def set_options_on_a(get_questions, a_answer):
    for x in get_questions:

        i = list(get_questions).index(x)

        if a_answer[i] == 'A' or a_answer[i] == 'a':
            x.option_temp = copy.copy(x.option1)
            x.option1 = copy.copy(x.option_temp)
            i += 1

        elif a_answer[i] == 'B' or a_answer[i] == 'b':
            x.option_temp = copy.copy(x.option2)
            x.option2 = copy.copy(x.option1)
            x.option1 = copy.copy(x.option_temp)
            i += 1

        elif a_answer[i] == 'C' or a_answer[i] == 'c':
            x.option_temp = copy.copy(x.option3)
            x.option3 = copy.copy(x.option1)
            x.option1 = copy.copy(x.option_temp)
            i += 1

        elif a_answer[i] == 'D' or a_answer[i] == 'd':
            x.option_temp = copy.copy(x.option4)
            x.option4 = copy.copy(x.option1)
            x.option1 = copy.copy(x.option_temp)
            i += 1

def set_options_on_b(get_questions, b_answer):

    for x in get_questions:
        i = list(get_questions).index(x)
        if b_answer[i] == 'A' or b_answer[i] == 'a':
            x.option_temp = copy.copy(x.option1)
            x.option1 = copy.copy(x.option_temp)
            i += 1

        elif b_answer[i] == 'B' or b_answer[i] == 'b':
            x.option_temp = copy.copy(x.option2)
            x.option2 = copy.copy(x.option1)
            x.option1 = copy.copy(x.option_temp)
            i += 1

        elif b_answer[i] == 'C' or b_answer[i] == 'c':
            x.option_temp = copy.copy(x.option3)
            x.option3 = copy.copy(x.option1)
            x.option1 = copy.copy(x.option_temp)
            i += 1

        elif b_answer[i] == 'D' or b_answer[i] == 'd':
            x.option_temp = copy.copy(x.option4)
            x.option4 = copy.copy(x.option1)
            x.option1 = copy.copy(x.option_temp)
            i += 1