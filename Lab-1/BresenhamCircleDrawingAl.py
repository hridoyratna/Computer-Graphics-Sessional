import matplotlib.pyplot as plt


def bresenham_circle(xc, yc, r):
    x = 0
    y = r
    d = 3 - 2 * r

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
        if d < 0:
            x += 1
            d = d + 4*x + 6
            
        else:
            x += 1
            y -= 1
            d = d + 4*(x - y) + 10
           
           

        

    return x_points, y_points


xc = int(input("Enter center x: "))
yc = int(input("Enter center y: "))
r = int(input("Enter radius: "))

x, y = bresenham_circle(xc, yc, r)

plt.scatter(x, y)
plt.title("Bresenham Circle Drawing Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()
