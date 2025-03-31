def genrange(start_num, end_num):
    num = start_num

    while num <= end_num:
        yield num
        num += 1


