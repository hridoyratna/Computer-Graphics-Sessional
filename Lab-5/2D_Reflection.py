import matplotlib.pyplot as plt

def twoD_reflection(points, axis):
    reflected_points = []
    print("\n------ Calculation Steps ------\n")

    for (x, y) in points:
        if axis == 1:  # Reflection on X-axis
            x_new = x
            y_new = -y
            print(f"Reflection on X-axis for ({x},{y}): x' = {x_new}, y' = {y_new}")
        elif axis == 2:  # Reflection on Y-axis
            x_new = -x
            y_new = y
            print(f"Reflection on Y-axis for ({x},{y}): x' = {x_new}, y' = {y_new}")

        reflected_points.append((x_new, y_new))
    return reflected_points


num_points = int(input("Enter number of points : "))

points = []
for i in range(num_points):
    x = float(input(f"Enter x{i+1}: "))
    y = float(input(f"Enter y{i+1}: "))
    points.append((x, y))

print("\nSelect Reflection Axis:")
print("1. Reflection on X-axis")
print("2. Reflection on Y-axis")
axis = int(input("Enter choice (1 or 2): "))

reflected_points = twoD_reflection(points, axis)

print("\nOriginal Points:", points)
print("Reflected Points:", reflected_points)

fig, ax = plt.subplots()

if num_points == 1:
    circle_original = plt.Circle(points[0], 0.1, color='skyblue', alpha=0.7, label="Original Point")
    ax.add_patch(circle_original)

    circle_reflected = plt.Circle(reflected_points[0], 0.1, color='lightcoral', alpha=0.7, label="Reflected Point")
    ax.add_patch(circle_reflected)

    ax.arrow(points[0][0], points[0][1],
             (reflected_points[0][0]-points[0][0])/2,
             (reflected_points[0][1]-points[0][1])/2,
             length_includes_head=True,
             head_width=0.05,
             head_length=0.07,
             fc='green', ec='green')

else:
    x_original = [p[0] for p in points] + [points[0][0]]
    y_original = [p[1] for p in points] + [points[0][1]]
    x_reflected = [p[0] for p in reflected_points] + [reflected_points[0][0]]
    y_reflected = [p[1] for p in reflected_points] + [reflected_points[0][1]]

    ax.fill(x_original, y_original, color='skyblue', alpha=0.5, label="Original Shape")
    ax.plot(x_original, y_original, color='blue', linewidth=2)
    ax.fill(x_reflected, y_reflected, color='lightcoral', alpha=0.5, label="Reflected Shape")
    ax.plot(x_reflected, y_reflected, color='red', linewidth=2)


ax.axhline(0, color='black')
ax.axvline(0, color='black')
ax.grid(True)
ax.set_aspect('equal', adjustable='datalim')
plt.title("2D Reflection Transformation")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()