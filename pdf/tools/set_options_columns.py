from pdf import table_style
from reportlab.lib.units import mm, cm
from reportlab.platypus import Paragraph, Table, KeepTogether


def set_option_column_and_rowheight(get_questions, styles, elements, opt_2_que_spacer):
    q_font_size = 10  # Soruların font büyüklüğü
    o_font_size = 10  # Cevapların font büyüklüğü


    q_table_style = table_style.q_table_style
    o_table_style = table_style.o_table_style
    for idx, value in enumerate(get_questions):

        get_row_height = get_questions[idx].row_height
        if get_row_height == '2':
            set_row_height = 23
        elif get_row_height == '3':
            set_row_height = 36
        else:
            set_row_height = 12

        qnum = idx + 1
        wid_qnum = 0.9 * cm
        wid_q = 8.6 * cm
        if int(get_questions[idx].columns) == 2:
            datao = [
                (
                Paragraph('<para fontSize={0}>a. {1}</para>'.format(o_font_size, str(value.option1)), styles['Option']),
                Paragraph('<para fontSize={0}>b. {1}</para>'.format(o_font_size, str(value.option2)),
                          styles['Option'])),
                (
                Paragraph('<para fontSize={0}>c. {1}</para>'.format(o_font_size, str(value.option3)), styles['Option']),
                Paragraph('<para fontSize={0}>d. {1}</para>'.format(o_font_size, str(value.option4)), styles['Option']))
            ]
            o = Table(datao, colWidths=[(4.2 * cm), (4.2 * cm)], rowHeights=set_row_height)
            o.setStyle(o_table_style)
            dataq = [
                (Paragraph('<para fontSize={0}>{1}.</para>'.format(q_font_size, str(qnum)), styles['Question']),
                 Paragraph('<para fontSize={0}> {1}</para>'.format(q_font_size, str(value).replace('\n', '<br />\n')),
                           styles['Question'])),
                ("", o)
            ]
            q = Table(dataq, colWidths=[(wid_qnum), (wid_q)])

            q.setStyle(q_table_style)
        elif int(get_questions[idx].columns) == 4:
            datao = [
                (
                Paragraph('<para fontSize={0}>a. {1}</para>'.format(o_font_size, str(value.option1)), styles['Option']),
                Paragraph('<para fontSize={0}>b. {1}</para>'.format(o_font_size, str(value.option2)), styles['Option']),
                Paragraph('<para fontSize={0}>c. {1}</para>'.format(o_font_size, str(value.option3)), styles['Option']),
                Paragraph('<para fontSize={0}>d. {1}</para>'.format(o_font_size, str(value.option4)), styles['Option']))
            ]
            o = Table(datao, colWidths=[(2 * cm), (2 * cm), (2 * cm), (2 * cm)], rowHeights=set_row_height)
            o.setStyle(o_table_style)
            dataq = [
                (Paragraph('<para fontSize={0}>{1}.</para>'.format(q_font_size, str(qnum)), styles['Question']),
                 Paragraph('<para fontSize={0}> {1}</para>'.format(q_font_size, str(value).replace('\n', '<br />\n')),
                           styles['Question'])),
                ("", o)
            ]
            q = Table(dataq, colWidths=[(wid_qnum), (wid_q)])
            q.setStyle(q_table_style)

        else:
            datao = [
                ('', Paragraph('<para fontSize={0}>a. {1}</para>'.format(o_font_size, str(value.option1)),
                               styles['Option'])),
                ('', Paragraph('<para fontSize={0}>b. {1}</para>'.format(o_font_size, str(value.option2)),
                               styles['Option'])),
                ('', Paragraph('<para fontSize={0}>c. {1}</para>'.format(o_font_size, str(value.option3)),
                               styles['Option'])),
                ('', Paragraph('<para fontSize={0}>d. {1}</para>'.format(o_font_size, str(value.option4)),
                               styles['Option'])),
            ]
            o = Table(datao, colWidths=[(0 * cm), (8.5 * cm)], rowHeights=set_row_height)
            o.setStyle(o_table_style)

            data = [
                (Paragraph('<para fontSize={0}>{1}.</para>'.format(q_font_size, str(qnum)), styles['Question']),
                 Paragraph('<para fontSize={0}> {1}</para>'.format(q_font_size, str(value).replace('\n', '<br />\n')),
                           styles['Question'])),
                ('', o),
            ]
            q = Table(data, colWidths=[(wid_qnum), (wid_q)])
            q.setStyle(q_table_style)

        elements.append(KeepTogether(q))
        elements.append(opt_2_que_spacer)