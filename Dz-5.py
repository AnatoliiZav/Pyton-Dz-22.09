# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

X1 = float(input("Введите координату X первой точки:"))
Y1 = float(input("Введите координату Y первой точки:"))
X2 = float(input("Введите координату X второй точки:"))
Y2 = float(input("Введите координату Y второй точки:"))


S = ((X2 -X1)**2 + (Y2-Y1)**2)**(0.5)

print("Расстояние между точками =" + str(S))