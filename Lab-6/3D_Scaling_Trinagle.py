import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.patches import Patch

def create_triangle():
    return np.array([
        [3,4,1],
        [6,4,2],
        [5,6,3]
    ])

def plot_triangle(ax,vertices,color):
    faces = [
        [vertices[0],vertices[1],vertices[2]]
    ]
    ax.add_collection3d(Poly3DCollection(faces,facecolors=color,linewidth=1,edgecolors='black',alpha=1))


def Scaled_triangle(vertices,Sx,Sy,Sz):
    scaled = vertices.copy()

    for i in range(len(vertices)):
        x,y,z = vertices[i]

        x = x*Sx
        y = y*Sy
        z = z*Sz

        scaled[i] = [x,y,z]
    return scaled

original = create_triangle()

Sx = float(input("Scaling parameter of X axis: ")) 
Sy = float(input("Scaling parameter of Y axis: ")) 
Sz = float(input("Scaling parameter of Z axis: ")) 

scaled = Scaled_triangle(original,Sx,Sy,Sz)

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')

plot_triangle(ax,original,'blue')
plot_triangle(ax,scaled,'red')

ax.set_xlim(0,8)
ax.set_ylim(0,10)
ax.set_zlim(0,20)
ax.set_title(f"3D Scaling of Transformation")

legend_elements = [
    Patch(facecolor='blue',edgecolor='black',alpha=1,label='Original Triangle'),
    Patch(facecolor='red',edgecolor='black',alpha=1,label='Scaled Triangle')
]
ax.legend(handles=legend_elements)

plt.show()