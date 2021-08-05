for i in range(1, 101):
    if i == 1 or i > 11 and i % 10 == 1:
        print(i, 'процент')
    elif i == 2 or i == 3 or i == 4 or i > 14 and (i % 10 == 2 or i % 10 == 3 or i % 10 == 4):
        print(i, 'процента')
    else:
        print(i, 'процентов')