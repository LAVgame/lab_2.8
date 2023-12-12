#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    """
    Запрашивает ввод с клавиатуры и возвращает введенную строку.
    """
    user_input = input("Введите значение: ")
    return user_input

def test_input(value):
    """
    Проверяет, можно ли преобразовать переданное значение к целому числу.
    Возвращает True, если преобразование возможно, иначе возвращает False.
    """
    try:
        int(value)
        return True
    except ValueError:
        return False

def str_to_int(value):
    """
    Преобразует переданное значение к целочисленному типу и возвращает полученное число.
    """
    return int(value)

def print_int(value):
    """
    Выводит переданное значение на экран.
    """
    print(value)

if __name__ == "__main__":
    # Вызываем первую функцию
    user_input = get_input()

    # Передаем данные во вторую функцию
    if test_input(user_input):
        # Если вторая функция возвращает True, передаем данные в третью функцию
        int_value = str_to_int(user_input)

        # Передаем полученное число в четвертую функцию
        print_int(int_value)
    else:
        print("Введенное значение не является целым числом.")
