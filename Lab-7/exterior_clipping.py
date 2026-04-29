import matplotlib.pyplot as plt 
from shapely.geometry import Polygon, box 

xmin, xmax, ymin, ymax = 40, 80, 40, 80

clipping_window = box(xmin, ymin, xmax, ymax)

obj_a = Polygon([
    (20,60),(60,100),(100,60),(60,20)
]) 

obj_b = Polygon([
    (50,50),(50,70),(70,70),(70,50)
])

obj_c = Polygon([
    (10,20),(20,30),(30,10)
])

original_obj = [
    (obj_a,'blue','obj_a(Partial)'),
    (obj_b, 'green','obj_b(inside)'),
    (obj_c, 'red', 'obj_c(outside)')
]

clipping_point = []
for obj, color, label in original_obj:

    exterior_result = obj.difference(clipping_window)
    clipping_point.append((exterior_result,color,label))


fig, (ax1, ax2) = plt.subplots(1,2, figsize=(14,6))

def draw_polygon(ax, obj, color, label):
    if obj.is_empty:
        return
    
    if obj.geom_type == 'Polygon':
        x,y = obj.exterior.xy
        ax.fill(x, y, color=color, label=label,alpha=0.4)
        ax.plot(x,y,linewidth=2,color=color)
    elif obj.geom_type == 'MultiPolygon':
        for i,poly in enumerate(obj.geoms):
            x,y = poly.exterior.xy
            ax.fill(x, y, color=color, alpha=0.4, label=label if i == 0 else "")
            ax.plot(x,y,linewidth=2,color=color)

ax1.set_title("Before Exterior clipping")
ax1.plot([xmin,xmax,xmax,xmin,xmin],[ymin,ymin,ymax,ymax,ymin],color='black')

for obj,color,label in original_obj:
    draw_polygon(ax1, obj, color, label)

ax1.set_xlim(0,120)
ax1.set_ylim(0,120)
ax1.set_aspect('equal')
ax1.grid(True)
ax1.legend(loc='upper right')

ax2.set_title("After Exterior clipping")
ax2.plot([xmin,xmax,xmax,xmin,xmin],[ymin,ymin,ymax,ymax,ymin],color='black')

for obj,color,label in clipping_point:
    draw_polygon(ax2, obj, color, label)

ax2.set_xlim(0,120)
ax2.set_ylim(0,120)
ax2.set_aspect('equal')
ax2.grid(True)
ax2.legend(loc='upper right')

plt.tight_layout()
plt.show()