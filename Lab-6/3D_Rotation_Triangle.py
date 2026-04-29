import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def create_Triangle():
    return np.array([
        [0,0,0],
        [1,1,2],
        [1,1,3]
    ])

def plot_triangle(ax,vertices,color):
    faces=[
        [vertices[0],vertices[1],vertices[2]]
    ]
    ax.add_collection3d(Poly3DCollection(faces,facecolor=color,edgecolor='black',linewidth=1,alpha=0.5))


def rotationAxis_X(vertices,Rotation_angle):
    rotation = vertices.copy()

    theta = np.radians(Rotation_angle)

    for i in range(len(vertices)):
        x,y,z = vertices[i]

        y_new = (y*np.cos(theta)) - (z*np.sin(theta))
        z_new = (y*np.sin(theta)) + (z*np.cos(theta))

        rotation[i] = [x,y_new,z_new]
    return rotation

def rotationAxis_Y(vertices,Rotation_angle):
    rotation = vertices.copy()

    theta = np.radians(Rotation_angle)

    for i in range(len(vertices)):
        x,y,z = vertices[i]

        x_new = (z*np.sin(theta)) + (x*np.cos(theta))
        z_new = (z*np.cos(theta)) - (x*np.sin(theta))

        rotation[i] = [x_new,y,z_new]
    return rotation

def rotationAxis_Z(vertices,Rotation_angle):
    rotation = vertices.copy()

    theta = np.radians(Rotation_angle)

    for i in range(len(vertices)):
        x,y,z = vertices[i]

        x_new = (x*np.cos(theta)) - (y*np.sin(theta))
        y_new = (x*np.sin(theta)) + (y*np.cos(theta))

        rotation[i] = [x_new,y_new,z]
    return rotation


original = create_Triangle()
axis = input("Choose Rotation Axis(X / Y / Z): ").lower()
Rotation_angle = int(input("Enter Rotation angle(0-90): "))

if axis == 'x':
    rotation = rotationAxis_X(original,Rotation_angle)
elif axis == 'y':
    rotation = rotationAxis_Y(original,Rotation_angle)
else:
    rotation = rotationAxis_Z(original,Rotation_angle)

fig = plt.figure(figsize=(8,4))
ax = fig.add_subplot(111, projection='3d')

plot_triangle(ax,original,'blue')
plot_triangle(ax,rotation,'red')

ax.set_title(f"3D Rotation of Transformation({axis.upper()}axis) ")
ax.set_xlim(-3,3)
ax.set_ylim(-3,3)
ax.set_zlim(-3,3)

legend_elements = [
    Patch(facecolor='blue',edgecolor='black',alpha=0.5,label='Original Triangle'),
    Patch(facecolor='red',edgecolor='black',alpha=0.5,label='Rotated Triangle')
]

ax.legend(handles=legend_elements)

plt.show()