import matplotlib.pyplot as plt
import math


def dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))
    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1
    x_points = []
    y_points = []

    for i in range(int(steps) + 1):
        x_points.append(math.ceil(x))
        y_points.append(math.ceil(y))
        x += x_inc
        y += y_inc

    return x_points, y_points


x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

x, y = dda(x1, y1, x2, y2)

plt.plot(x, y, marker='o')
plt.title("DDA Line Drawing Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
