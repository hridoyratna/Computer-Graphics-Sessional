import matplotlib.pyplot as plt
import math
from matplotlib.patches import Arc

def twoD_rotation(points, theta_deg, rotation_type):
    theta = math.radians(theta_deg)
    rotated_points = []

    print("\n------ Calculation ------")

    for (x, y) in points:

        if rotation_type == 1:  # Counter-Clockwise
            x_new = x * math.cos(theta) - y * math.sin(theta)
            y_new = x * math.sin(theta) + y * math.cos(theta)

            print(f"Counter-Clockwise Rotation for ({x},{y})")
            print(f"x' = {x}cos({theta_deg}) - {y}sin({theta_deg}) = {x_new}")
            print(f"y' = {x}sin({theta_deg}) + {y}cos({theta_deg}) = {y_new}\n")

        elif rotation_type == 2:  # Clockwise
            x_new = x * math.cos(theta) + y * math.sin(theta)
            y_new = y * math.cos(theta) - x * math.sin(theta)

            print(f"Clockwise Rotation for ({x},{y})")
            print(f"x' = {x}cos({theta_deg}) + {y}sin({theta_deg}) = {x_new}")
            print(f"y' = {y}cos({theta_deg}) - {x}sin({theta_deg}) = {y_new}\n")

        rotated_points.append((x_new, y_new))

    return rotated_points


num_points = int(input("Enter number of points : "))
points = []
for i in range(num_points):
    x = float(input(f"Enter x{i+1}: "))
    y = float(input(f"Enter y{i+1}: "))
    points.append((x, y))

theta_deg = float(input("Enter rotation angle (in degrees): "))

print("\nSelect Rotation Type:")
print("1. Counter-Clockwise")
print("2. Clockwise")
rotation_type = int(input("Enter choice (1 or 2): "))

rotated_points = twoD_rotation(points, theta_deg, rotation_type)

print("Original Points:", points)
print("Rotated Points:", rotated_points)


fig, ax = plt.subplots()

if num_points == 1:
    ax.plot([0, points[0][0]], [0, points[0][1]], color='blue', label="Original Position", linewidth=2)
    ax.plot([0, rotated_points[0][0]], [0, rotated_points[0][1]], color='red', label="Rotated Position", linewidth=2)

    ax.arrow(points[0][0], points[0][1], 
             rotated_points[0][0] - points[0][0], 
             rotated_points[0][1] - points[0][1], 
             length_includes_head=True, head_width=0.25, 
             head_length=0.35, fc='green', ec='green')

else:
    x_original = [p[0] for p in points] + [points[0][0]]
    y_original = [p[1] for p in points] + [points[0][1]]
    x_rot = [p[0] for p in rotated_points] + [rotated_points[0][0]]
    y_rot = [p[1] for p in rotated_points] + [rotated_points[0][1]]

    ax.fill(x_original, y_original, color='skyblue', alpha=0.5, label="Original Shape")
    ax.plot(x_original, y_original, color='blue', linewidth=2)

    ax.fill(x_rot, y_rot, color='lightcoral', alpha=0.5, label="Rotated Shape")
    ax.plot(x_rot, y_rot, color='red', linewidth=2)

ax.axhline(0, color='black')
ax.axvline(0, color='black')
ax.grid(True)
ax.set_aspect('equal', adjustable='datalim')

plt.title("2D Rotation Transformation")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()