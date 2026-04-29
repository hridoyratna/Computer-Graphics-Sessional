import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.patches import Patch

def triangle():
    return np.array([
        [3,4,1],
        [6,4,2],
        [5,6,3]
    ])

def plot_triangle(ax,vertices,color):
    faces = [
        [vertices[0],vertices[1],vertices[2]]
    ]

    ax.add_collection3d(Poly3DCollection(faces, facecolor=color,linewidth=1,edgecolor='black',alpha=0.5))



def reflectedAxis_XY(vertices):
    reflected = vertices.copy()

    for i in range(len(vertices)):
        x,y,z = vertices[i]

        z = -z

        reflected[i] = [x,y,z]
    return reflected

def reflectedAxis_YZ(vertices):
    reflected = vertices.copy()

    for i in range(len(vertices)):
        x,y,z = vertices[i]

        x = -x

        reflected[i] = [x,y,z]
    return reflected

def reflectedAxis_ZX(vertices):
    reflected = vertices.copy()

    for i in range(len(vertices)):
        x,y,z = vertices[i]

        y = -y

        reflected[i] = [x,y,z]
    return reflected


original = triangle()

axis = input(f"Choose Reflection axis(XY / YZ / ZX ): ").lower()

if axis == 'xy':
    reflected = reflectedAxis_XY(original)
elif axis == 'yz':
    reflected = reflectedAxis_YZ(original)
else:
    reflected = reflectedAxis_ZX(original)

fig = plt.figure(figsize=(8,4))
ax = fig.add_subplot(111, projection='3d')

plot_triangle(ax,original,'blue')
plot_triangle(ax,reflected,'red')

ax.set_xlim(0,10)
ax.set_ylim(0,10)
ax.set_zlim(0,10)
ax.set_title(f"3D Reflection of Transformation ({axis.upper()}) axis")

legend_elements = [
    Patch(facecolor='blue',edgecolor='black',alpha=0.5,label='Original'),
    Patch(facecolor='red',edgecolor='black',alpha=0.5,label='Reflected')
]

ax.legend(handles=legend_elements)

plt.show()