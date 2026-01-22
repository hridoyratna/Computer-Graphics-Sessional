import matplotlib.pyplot as plt


def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r

    x_points = []
    y_points = []

    while x <= y:
        points = [
            ( x + xc,  y + yc),
            ( y + xc,  x + yc),
            (-x + xc,  y + yc),
            (-y + xc,  x + yc),
            (-x + xc, -y + yc),
            (-y + xc, -x + yc),
            ( x + xc, -y + yc),
            ( y + xc, -x + yc)
        ]

        for px, py in points:
            x_points.append(px)
            y_points.append(py)

        # Decision parameter update
        if p < 0:
            p = p + 2*x + 3
        else:
            p = p + 2*(x - y) + 5
            y -= 1

        x += 1

    return x_points, y_points


xc = int(input("Enter center x: "))
yc = int(input("Enter center y: "))
r = int(input("Enter radius: "))

x, y = midpoint_circle(xc, yc, r)

plt.scatter(x, y)
plt.title("Mid-Point Circle Drawing Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()
