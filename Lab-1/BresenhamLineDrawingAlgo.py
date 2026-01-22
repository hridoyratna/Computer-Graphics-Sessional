import matplotlib.pyplot as plt


def bresenham_line(x1, y1, x2, y2):
    x_points = []
    y_points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    x, y = x1, y1

    if dx >= dy:
        p = 2*dy - dx
        for _ in range(dx + 1):
            x_points.append(x)
            y_points.append(y)

            x += 1
            if p >= 0:
                y += 1
                p -= 2*dx
            p += 2*dy
    else:
        p = 2*dx - dy
        for _ in range(dy + 1):
            x_points.append(x)
            y_points.append(y)

            y += 1
            if p >= 0:
                x += 1
                p -= 2*dy
            p += 2*dx

    return x_points, y_points


x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

x, y = bresenham_line(x1, y1, x2, y2)

plt.plot(x, y, marker='o')
plt.title("Bresenham Line Drawing Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
