import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D 
 
cube = [ 
    (0, 0, 0), 
    (2, 0, 0), 
    (2, 2, 0), 
    (0, 2, 0), 
    (0, 0, 2), 
    (2, 0, 2), 
    (2, 2, 2), 
    (0, 2, 2) 
] 
 
edges = [ 
    (0,1),(1,2),(2,3),(3,0),  # bottom 
    (4,5),(5,6),(6,7),(7,4),  # top 
    (0,4),(1,5),(2,6),(3,7)   # vertical 
] 
 
tx, ty, tz = 3, 4, 2 
 
def translate_3d(points, tx, ty, tz): 
    translated = [] 
    for (x, y, z) in points: 
        x_new = x + tx 
        y_new = y + ty 
        z_new = z + tz 
        translated.append((x_new, y_new, z_new)) 
    return translated 
 
translated_cube = translate_3d(cube, tx, ty, tz) 
 
fig = plt.figure(figsize=(8, 6)) 
ax = fig.add_subplot(111, projection='3d') 
 
for edge in edges: 
    p1 = cube[edge[0]] 
    p2 = cube[edge[1]] 
    ax.plot([p1[0], p2[0]], 
            [p1[1], p2[1]], 
            [p1[2], p2[2]], 
            color='blue', label='Original Cube' if edge 
== edges[0] else "") 
 
for edge in edges: 
    p1 = translated_cube[edge[0]] 
    p2 = translated_cube[edge[1]] 
    ax.plot([p1[0], p2[0]], 
            [p1[1], p2[1]], 
            [p1[2], p2[2]], 
            color='green', label='Translated Cube' if 
edge == edges[0] else "") 
 
ax.quiver(0, 0, 0, tx, ty, tz, color='red',  arrow_length_ratio=0.1, label='Translation Vector') 
 
ax.set_title("3D Translation (Non-Matrix Form)") 
ax.set_xlabel("X") 
ax.set_ylabel("Y") 
ax.set_zlabel("Z") 
ax.legend() 
plt.show() 