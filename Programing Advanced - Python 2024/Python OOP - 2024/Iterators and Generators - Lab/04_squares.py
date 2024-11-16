def squares(end_num):
    num = 1

    while num <= end_num:
        yield num * num
        num += 1

