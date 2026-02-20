import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def twoD_translation(points, Tx, Ty):
    translated_points = []

    print("\n------ Calculation ------")
    for (x, y) in points:
        x_new = x + Tx
        y_new = y + Ty

        print(f"For Point ({x}, {y})")
        print(f"x' = {x} + {Tx} = {x_new}")
        print(f"y' = {y} + {Ty} = {y_new}\n")

        translated_points.append((x_new, y_new))

    return translated_points

num_points = int(input("Enter number of points : "))

points = []

for i in range(num_points):
    x = float(input(f"Enter x{i+1}: "))
    y = float(input(f"Enter y{i+1}: "))
    points.append((x, y))

if num_points == 1:
    radius = float(input("Enter radius for drawing the circle: "))
else:
    radius = None

Tx = float(input("Enter Translation Tx: "))
Ty = float(input("Enter Translation Ty: "))

translated_points = twoD_translation(points, Tx, Ty)

print("Original Points:", points)
print("Translated Points:", translated_points)

fig, ax = plt.subplots()

if num_points == 1:
    # Original circle
    original_circle = Circle(points[0], radius, color='skyblue', alpha=0.5, label="Original Shape")
    ax.add_patch(original_circle)

    # Translated circle
    translated_circle = Circle(translated_points[0], radius, color='lightcoral', alpha=0.5, label="Translated Shape")
    ax.add_patch(translated_circle)

    ax.arrow(points[0][0], points[0][1], Tx, Ty, length_includes_head=True, head_width=radius*0.3, color='black')

else:
    x_original = [p[0] for p in points] + [points[0][0]]
    y_original = [p[1] for p in points] + [points[0][1]]

    x_translated = [p[0] for p in translated_points] + [translated_points[0][0]]
    y_translated = [p[1] for p in translated_points] + [translated_points[0][1]]

    ax.fill(x_original, y_original, color='skyblue', alpha=0.5, label="Original Shape")

    ax.fill(x_translated, y_translated, color='lightcoral', alpha=0.5, label="Translated Shape")

    ax.plot(x_original, y_original, color='blue')
    ax.plot(x_translated, y_translated, color='red')

    for i in range(num_points):
        ax.arrow(points[i][0], points[i][1], Tx, Ty, length_includes_head=True, head_width=0.3, color='black')

# Axis settings
ax.axhline(0)
ax.axvline(0)
ax.grid(True)
ax.set_aspect('equal', adjustable='datalim')

plt.title("2D Translation (Original vs Translated)")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()