import turtle
import math

turtle.shape('turtle')

rad = 180 / math.pi  # Высчитываем угол поворота спирали в радианах.
p = (0.5 / (2 * math.pi)) * rad  # 1 - шаг спирали
l = 0
for spiral in range(1000):
    l += 0.1
    turtle.forward(l)
    turtle.left(p)
