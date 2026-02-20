import matplotlib.pyplot as plt

def twoD_scaling(points, Sx, Sy):
    scaled_points = []

    print("\n------ Calculation ------")
    for (x, y) in points:
        x_new = x * Sx
        y_new = y * Sy

        print(f"For Point ({x}, {y})")
        print(f"x' = {x} × {Sx} = {x_new}")
        print(f"y' = {y} × {Sy} = {y_new}\n")

        scaled_points.append((x_new, y_new))

    return scaled_points

num_points = int(input("Enter number of points : "))

points = []
for i in range(num_points):
    x = float(input(f"Enter x{i+1}: "))
    y = float(input(f"Enter y{i+1}: "))
    points.append((x, y))

Sx = float(input("Enter Scaling factor Sx: "))
Sy = float(input("Enter Scaling factor Sy: "))

scaled_points = twoD_scaling(points, Sx, Sy)

print("Original Points:", points)
print("Scaled Points:", scaled_points)

plt.figure()

x_original = [p[0] for p in points] + [points[0][0]]
y_original = [p[1] for p in points] + [points[0][1]]

x_scaled = [p[0] for p in scaled_points] + [scaled_points[0][0]]
y_scaled = [p[1] for p in scaled_points] + [scaled_points[0][1]]

plt.fill(x_original, y_original, color='skyblue', alpha=0.5, label="Original Shape")
plt.plot(x_original, y_original, color='blue')

plt.fill(x_scaled, y_scaled, color='lightcoral', alpha=0.5, label="Scaled Shape")
plt.plot(x_scaled, y_scaled, color='red')

plt.axhline(0)
plt.axvline(0)
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='datalim')

plt.title("2D Scaling Transformation")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()

plt.show()