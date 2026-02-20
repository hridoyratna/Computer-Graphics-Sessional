import matplotlib.pyplot as plt

def twoD_shearing(points, axis, shx=0, shy=0):
    sheared_points = []
    print("\n------ Calculation Steps ------\n")

    for (x, y) in points:
        if axis == 1:  # Shearing on X-axis
            x_new = x + y * shx
            y_new = y
            print(f"Shearing on X-axis for ({x},{y}): x' = x + y*Shx = {x} + {y}*{shx} = {x_new}, y' = {y_new}")
        elif axis == 2:  # Shearing on Y-axis
            x_new = x
            y_new = y + x * shy
            print(f"Shearing on Y-axis for ({x},{y}): x' = {x_new}, y' = y + x*Shy = {y} + {x}*{shy} = {y_new}")

        sheared_points.append((x_new, y_new))
    return sheared_points


num_points = int(input("Enter number of points : "))

points = []
for i in range(num_points):
    x = float(input(f"Enter x{i+1}: "))
    y = float(input(f"Enter y{i+1}: "))
    points.append((x, y))

print("\nSelect Shearing Axis:")
print("1. Shearing on X-axis")
print("2. Shearing on Y-axis")
axis = int(input("Enter choice (1 or 2): "))

shx = shy = 0
if axis == 1:
    shx = float(input("Enter Shearing factor Shx: "))
elif axis == 2:
    shy = float(input("Enter Shearing factor Shy: "))

sheared_points = twoD_shearing(points, axis, shx, shy)

print("\nOriginal Points:", points)
print("Sheared Points:", sheared_points)


fig, ax = plt.subplots()

x_original = [p[0] for p in points] + [points[0][0]]
y_original = [p[1] for p in points] + [points[0][1]]
x_sheared = [p[0] for p in sheared_points] + [sheared_points[0][0]]
y_sheared = [p[1] for p in sheared_points] + [sheared_points[0][1]]


ax.fill(x_original, y_original, color='skyblue', alpha=0.5, label="Original Shape")
ax.plot(x_original, y_original, color='blue', linewidth=2)
ax.fill(x_sheared, y_sheared, color='lightcoral', alpha=0.5, label="Sheared Shape")
ax.plot(x_sheared, y_sheared, color='red', linewidth=2)


ax.axhline(0, color='black')
ax.axvline(0, color='black')
ax.grid(True)
ax.set_aspect('equal', adjustable='datalim')

plt.title("2D Shearing Transformation")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()