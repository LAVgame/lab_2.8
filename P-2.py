import math

def circle(radius):
    """
    Вычисляет площадь круга по формуле: π * r^2.
    """
    return math.pi * radius**2

def cylinder():
    """
    Вычисляет площадь цилиндра.
    Пользователь выбирает, хочет ли он получить только площадь боковой поверхности
    (S_cylinder_side), или полную площадь цилиндра (S_cylinder_full).
    """
    radius = float(input("Введите радиус цилиндра: "))
    height = float(input("Введите высоту цилиндра: "))

    # Вычисление площади боковой поверхности цилиндра
    S_cylinder_side = 2 * math.pi * radius * height

    # Вывод результатов площади боковой поверхности
    print(f"Площадь боковой поверхности цилиндра: {S_cylinder_side}")

    # Пользователь выбирает, хочет ли он получить полную площадь цилиндра
    full_area_choice = input("Хотите получить полную площадь цилиндра? (yes/no): ").lower()

    if full_area_choice == 'yes':
        # Вычисление полной площади цилиндра (боковая поверхность + 2 * площадь круга)
        S_cylinder_full = S_cylinder_side + 2 * circle(radius)

        # Вывод полной площади цилиндра
        print(f"Полная площадь цилиндра: {S_cylinder_full}")

if __name__ == "__main__":
    # Вызов функции cylinder()
    cylinder()
