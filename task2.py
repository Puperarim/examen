def get_determinant(matrix):
    det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    return det

string_first = list(map(int, input('Введите первую строку(2 числа через пробел): ').split()))
string_second = list(map(int, input('Введите вторую строку(2 числа через пробел): ').split()))

print(get_determinant([string_first, string_second]))

string_all = list(map(int, input('Введите 4 числа матрицы через пробел: ').split()))

print(get_determinant([string_all[:2], string_all[2:]]))