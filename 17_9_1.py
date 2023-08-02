"""Задание 17.9.1"""
from typing import List


def sort_func(num_list: List) -> List:
    for i in range(len(num_list)):
        for j in range(len(num_list) - i - 1):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
    return num_list


def string_validation(numbers: str) -> List:
    """Преобразование строки в список из целых чисел (int) и чисел с плавающей запятой (float)"""
    elements_list = []
    for elem in numbers.split():  # сплитуем строку разбивая на числа и символы, минуя пробелы
        try:
            if elem.isdigit():
                elements_list.append(int(elem))  # закидываем в список целое число

        except:  # отсеиваем символы не добавляя в список
            continue
    return elements_list


def binary_search(arr: List, target: int) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low


entered_data = input('Введите числа через пробел: ')
numbers_list = string_validation(entered_data)
numbers_list = sort_func(numbers_list)
print(f'Отсортированный список целых чисел по возрастанию: {numbers_list}')

while True:
    try:
        num = int(input('Введите число: '))
        if numbers_list[0] <= num <= numbers_list[-1]:
            result = binary_search(numbers_list, num)
            print(f'Ответ: {result}')
            break
        else:
            print('Ошибка! Число не входит в диапазон введенных чисел. Попробуйте еще раз.\n')
    except ValueError:
        print('Введено не целое число. Попробуйте еще раз.\n')
