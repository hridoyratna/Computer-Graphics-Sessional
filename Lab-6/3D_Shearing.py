import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.patches import Patch

def Create_Cube():
    return np.array([
        [0,0,0],
        [2,0,0],
        [2,2,0],
        [0,2,0],
        [0,0,2],
        [2,0,2],
        [2,2,2],
        [0,2,2]
    ])


def plot_cube(ax,vertices,color):
    faces=[
        [vertices[0],vertices[1],vertices[2],vertices[3]],
        [vertices[4],vertices[5],vertices[6],vertices[7]],
        [vertices[0],vertices[1],vertices[5],vertices[4]],
        [vertices[2],vertices[3],vertices[7],vertices[6]],
        [vertices[1],vertices[2],vertices[6],vertices[5]],
        [vertices[4],vertices[7],vertices[3],vertices[0]]
    ]

    ax.add_collection3d(Poly3DCollection(faces, facecolors=color, linewidths=1, edgecolors='black', alpha=0.4))



def shear_x(vertices, shy, shz):
    sheared = vertices.copy()
    for i in range(len(vertices)):
        x, y, z = vertices[i]
        y = y + shy * x
        z = z + shz * x
        sheared[i] = [x, y, z]
    return sheared

def shear_y(vertices, shx, shz):
    sheared = vertices.copy()
    for i in range(len(vertices)):
        x, y, z = vertices[i]
        x = x + shx * y
        z = z + shz * y
        sheared[i] = [x, y, z]
    return sheared 

def shear_z(vertices, shx, shy):
    sheared = vertices.copy()
    for i in range(len(vertices)):
        x, y, z = vertices[i]
        x = x + shx * z
        y = y + shy * z
        sheared[i] = [x, y, z]
    return sheared


original = Create_Cube()
axis = input("Choose shearing axis(x / y/ z): ").lower()

if axis == 'x':
    shy = float(input("Enter Shearing factor of y axis: "))
    shz = float(input("Enter Shearing factor of z axis: "))
    Sheared = shear_x(original,shy,shz) 
elif axis == 'y':
    shx = float(input("Enter Shearing factor of x axis: "))
    shz = float(input("Enter Shearing factor of z axis: "))
    Sheared = shear_y(original,shx,shz)   
else:
    shx = float(input("Enter Shearing factor of x axis: "))
    shy = float(input("Enter Shearing factor of y axis: "))
    Sheared = shear_z(original,shx,shy) 

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111,projection='3d')

plot_cube(ax,original,'blue')
plot_cube(ax,Sheared,'red')

ax.set_title(f"3D Shearing Transformation({axis.upper()}axis)")
ax.set_xlim(0,10)
ax.set_ylim(0,10)
ax.set_zlim(0,10)

legend_elements = [
    Patch(facecolor='blue',edgecolor='black',alpha=0.4,label='Original Cube'),
    Patch(facecolor='red',edgecolor='black',alpha=0.4,label='Sheared Cube')
]

ax.legend(handles=legend_elements)

plt.show()

