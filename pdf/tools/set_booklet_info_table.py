dikkat = 'DİKKAT!!!'
booklet = 'KİTAPÇIK TÜRÜ'


def booklet_info_table(canvas, font_bold, page_side):
    # Dikkat Kitapçık türü - Ön sayfa
    '''page_side value must be "front" or "back"'''
    x_coor = 495
    if page_side == "front":
        y_coor = 710
        canvas.setFont(font_bold, 14)
        canvas.drawString(x_coor, y_coor, dikkat)  # Dikkat!!!
        canvas.setFont(font_bold, 10)
        canvas.drawString(x_coor-5, y_coor-15, booklet)  # Kitapçık Türü
        canvas.roundRect(x_coor-15, y_coor-60, 100, 55, 0, stroke=1, fill=0)
        canvas.line(x_coor-15, y_coor-20, x_coor+85, y_coor-20)  # Kitapçık türü alt çizgi
        canvas.setFont(font_bold, 14)
        canvas.drawString(x_coor+10, y_coor-35, 'A') # 505, 675
        canvas.drawString(x_coor+50, y_coor-35, 'B') # 545, 675
    elif page_side == "back":
        # Dikkat Kitapçık türü - Arka Sayfa
        y_coor = 90
        canvas.setFont(font_bold, 14)
        canvas.drawString(x_coor, y_coor, dikkat)  # Dikkat!!!
        canvas.setFont(font_bold, 10)
        canvas.drawString(x_coor-5, y_coor-15, booklet)  # Kitapçık Türü
        canvas.roundRect(x_coor-15, 30, y_coor+10, 55, 0, stroke=1, fill=0)
        canvas.line(x_coor-15, y_coor-20, x_coor+85, y_coor-20)  # Kitapçık türü alt çizgi
        canvas.setFont(font_bold, 14)
        canvas.drawString(x_coor+10, y_coor-35, 'A')
        canvas.drawString(x_coor+50, y_coor-35, 'B')