def is_point_in_circle(x, y, radius):
    return x**2 + y**2 <= radius**2
x = float(input("Введите координату x точки: "))
y = float(input("Введите координату y точки: "))
radius = float(input("Введите радиус круга: "))
if is_point_in_circle(x, y, radius):
    print(f"Точка ({x}, {y}) принадлежит кругу с радиусом {radius}.")
else:
    print(f"Точка ({x}, {y}) не принадлежит кругу с радиусом {radius}.")