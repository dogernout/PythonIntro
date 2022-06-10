import copy


def det3x3(mas):
    return mas[0][0] * mas[1][1] * mas[2][2] + mas[1][0] * mas[2][1] * mas[0][2] + mas[0][1] * mas[1][2] * mas[2][0] - mas[0][2] * mas[1][1] * mas[2][0] - mas[0][0] * mas[2][1] * mas[1][2] - mas[2][2] * mas[0][1] * mas[1][0]


def make3x3(val, ind):
    i = 0
    matr = copy.deepcopy(val)
    matr.pop(0)
    while i < 3:
        matr[i].pop(ind)
        i += 1
    return det3x3(matr)


a = eval(input())
mas = [[0] * 4 for i in range(4)]
i = 0
while i < 4:
    j = 0
    while j < 4:
        mas[i][j] = a[i][j]
        j += 1
    i += 1
print(mas[0][0] * make3x3(mas, 0) - mas[0][1] * make3x3(mas, 1) + mas[0][2] * make3x3(mas, 2) - mas[0][3] * make3x3(mas, 3))
