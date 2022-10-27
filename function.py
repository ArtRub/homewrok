def next(a):
    checker = True
    b = a.split(".")
    leap_year = int(b[2])
    if b[1] in ['4', '6', '9', '11']:
        number_days = 30
    else:
        number_days = 31
    if leap_year % 400 == 0 or (leap_year % 100 != 0 and leap_year % 4 == 0):
        print("Високосный год")
    else:
        checker = False
        print("Невисокосный год")
    if int(b[0]) == 29 and int(b[1]) == 2 and checker == False:
        print("Такой даты не существует")
    elif int(b[0]) > 31 or int(b[1]) > 12:
        print("Такой даты не существует")
    else:
        if int(b[0]) == 31 and int(b[1]) == 12:
            day = 1
            month = 1
            year = int(b[2]) + 1
        elif int(b[0]) == 31:
            day = 1
            month = int(b[1]) + 1
            year = int(b[2]) + 1
        elif int(b[0]) == 30 and number_days == 30:
            day = 1
            month = int(b[1]) + 1
            year = b[2]
        elif int(b[0]) == 29 and int(b[1]) == 2 and checker == True:
            day = 1
            month = int(b[1]) + 1
            year = b[2]
        elif int(b[0]) == 28 and int(b[1]) == 2 and checker == False:
            day = 1
            month = int(b[1]) + 1
            year = b[2]
        else:
            day = int(b[0]) + 1
            month = b[1]
            year = b[2]
        print('{:0>2}.{:0>2}.{:0>4}'.format(day, month, year))

