cube_list = [i ** 3 for i in range(1, 1001, 2)]


def summ_digits(num):
    summ = 0
    while num > 0:
        summ += num % 10
        num //= 10
    return summ


cube_sum = 0

for cube in cube_list:
    if summ_digits(cube) % 7 == 0:
        cube_sum += cube

print(cube_sum)

cube_sum = 0

for cube in cube_list:
    if summ_digits(cube + 17) % 7 == 0:
        cube_sum += cube

print(cube_sum)
