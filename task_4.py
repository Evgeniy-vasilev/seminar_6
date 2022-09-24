# 3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

# Было:
def diff_fract(list):
    list_fract = []

    for i in range(len(list)):
        list_fract.append(round((list[i] % 1), 2))

    fractional = max(list_fract) - min(list_fract)

    return fractional


print(diff_fract([1.1, 1.2, 3.1, 10.01]))

# Стало:
def diff_fract(list):
    list_fract = [round((list[i] % 1), 2) for i in range(len(list))]
    fractional = max(list_fract) - min(list_fract)

    return fractional


print(diff_fract([1.1, 1.2, 3.1, 10.01]))
