# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).



N = int(input("Введите номер четверти:"))
if N == 1:
    print("X > 0, Y > 0")
elif N == 2:
    print("X < 0, Y > 0")
elif N == 3:
    print("X < 0, Y < 0")
elif N == 4:
    print("X > 0, Y < 0")
else:
    print("Неверный номер четверти")