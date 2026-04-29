import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.patches import Patch

def create_cube():
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
    faces = [
        [vertices[0],vertices[1],vertices[2],vertices[3]],
        [vertices[4],vertices[5],vertices[6],vertices[7]],
        [vertices[0],vertices[1],vertices[5],vertices[4]],
        [vertices[2],vertices[3],vertices[7],vertices[6]],
        [vertices[1],vertices[2],vertices[6],vertices[5]],
        [vertices[4],vertices[7],vertices[3],vertices[0]]
    ]
    ax.add_collection3d(Poly3DCollection(faces,facecolors=color,linewidth=1,edgecolors='black',alpha=0.4))


def Scaled_cube(vertices,Sx,Sy,Sz):
    scaled = vertices.copy()

    for i in range(len(vertices)):
        x,y,z = vertices[i]

        x = x*Sx
        y = y*Sy
        z = z*Sz

        scaled[i] = [x,y,z]
    return scaled

original = create_cube()

Sx = float(input("Scaling parameter of X axis: ")) 
Sy = float(input("Scaling parameter of Y axis: ")) 
Sz = float(input("Scaling parameter of Z axis: ")) 

scaled = Scaled_cube(original,Sx,Sy,Sz)

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')

plot_cube(ax,original,'blue')
plot_cube(ax,scaled,'red')

ax.set_xlim(0,10)
ax.set_ylim(0,10)
ax.set_zlim(0,10)
ax.set_title(f"3D Scaling of Transformation")

legend_elements = [
    Patch(facecolor='blue',edgecolor='black',alpha=0.4,label='Original Cube'),
    Patch(facecolor='red',edgecolor='black',alpha=0.4,label='Scaled Cube')
]
ax.legend(handles=legend_elements)

plt.show()