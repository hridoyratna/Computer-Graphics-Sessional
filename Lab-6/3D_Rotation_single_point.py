import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# ✅ Single point
def create_point():
    return np.array([1, 2, 3])

# ✅ Rotation about X-axis
def rotationAxis_X(point, angle):
    theta = np.radians(angle)
    x, y, z = point

    y_new = y*np.cos(theta) - z*np.sin(theta)
    z_new = y*np.sin(theta) + z*np.cos(theta)

    return np.array([x, y_new, z_new])

# ✅ Rotation about Y-axis
def rotationAxis_Y(point, angle):
    theta = np.radians(angle)
    x, y, z = point

    x_new = z*np.sin(theta) + x*np.cos(theta)
    z_new = z*np.cos(theta) - x*np.sin(theta)

    return np.array([x_new, y, z])

# ✅ Rotation about Z-axis
def rotationAxis_Z(point, angle):
    theta = np.radians(angle)
    x, y, z = point

    x_new = x*np.cos(theta) - y*np.sin(theta)
    y_new = x*np.sin(theta) + y*np.cos(theta)

    return np.array([x_new, y_new, z])

# 🔷 Main
original = create_point()

axis = input("Choose Rotation Axis (x / y / z): ").lower()
angle = float(input("Enter Rotation angle (degree): "))

if axis == 'x':
    rotated = rotationAxis_X(original, angle)
elif axis == 'y':
    rotated = rotationAxis_Y(original, angle)
elif axis == 'z':
    rotated = rotationAxis_Z(original, angle)
else:
    print("Invalid axis!")
    exit()

# 🔷 Plot
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Plot points
ax.scatter(original[0], original[1], original[2], color='blue', s=100)
ax.scatter(rotated[0], rotated[1], rotated[2], color='red', s=100)

# Optional: connect with line
ax.plot(
    [original[0], rotated[0]],
    [original[1], rotated[1]],
    [original[2], rotated[2]],
    linestyle='dashed'
)

ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
ax.set_zlim(-5,5)

ax.set_title(f"3D Rotation of a Point ({axis.upper()}-axis)")

legend_elements = [
    Patch(facecolor='blue', label='Original Point'),
    Patch(facecolor='red', label='Rotated Point')
]

ax.legend(handles=legend_elements)

plt.show()