import matplotlib.pyplot as plt

xmin, xmax, ymin, ymax = 30, 50, 20, 40

polygon = [
    (25,30),
    (40,45),
    (55,30),
    (40,15)
]

def inside_left(p):
    return p[0] >= xmin

def inside_right(p):
    return p[0] <= xmax

def inside_top(p):
    return p[1] <= ymax

def inside_bottom(p):
    return p[1] >= ymin

def intersect(p,p1,edge):
    x0, y0 = p
    x1, y1 = p1

    if edge == 'left':
        x = xmin
        y = y0 + (y1 - y0)*(xmin - x0)/(x1 - x0)
    elif edge == 'right':
        x = xmax
        y = y0 + (y1 - y0)*(xmax - x0)/(x1 - x0)
    elif edge == 'top':
        x = x0 + (x1 - x0)*(ymax - y0)/(y1 - y0)
        y = ymax
    elif edge == 'bottom':
        x = x0 + (x1 - x0)*(ymin - y0)/(y1 - y0)
        y = ymin
    return (x,y)


def sutherland_Hodgman_clip_polygon(polygon,edge):
    clipped_polygon = []

    if edge == 'left':
        inside = inside_left
    elif edge == 'right':
        inside = inside_right
    elif edge == 'top':
        inside = inside_top
    elif edge == 'bottom':
        inside = inside_bottom
    
    prev_point = polygon[-1]

    for curr_point in polygon:
        if inside(curr_point):
            if not inside(prev_point):
                clipped_polygon.append(intersect(prev_point,curr_point,edge))
            clipped_polygon.append(curr_point)
        elif inside(prev_point):
            clipped_polygon.append(intersect(prev_point,curr_point,edge))

        prev_point = curr_point
    return clipped_polygon


clipped = polygon
clipped = sutherland_Hodgman_clip_polygon(clipped,'left')
clipped = sutherland_Hodgman_clip_polygon(clipped,'right')
clipped = sutherland_Hodgman_clip_polygon(clipped,'top')
clipped = sutherland_Hodgman_clip_polygon(clipped,'bottom')

fig, ax = plt.subplots(1,2, figsize=(8,6))
ax[0].plot([xmin,xmax,xmax,xmin,xmin],[ymin,ymin,ymax,ymax,ymin],color='black')
x_vals = [p[0] for p in polygon] + [polygon[0][0]]
y_vals = [p[1] for p in polygon] + [polygon[0][1]]

ax[0].plot(x_vals,y_vals,marker='o')
ax[0].set_title("Before clipping")
ax[0].set_aspect('equal')
ax[0].grid(True)


ax[1].plot([xmin,xmax,xmax,xmin,xmin],[ymin,ymin,ymax,ymax,ymin],color='black')
if clipped:
    x_vals = [p[0] for p in clipped] + [clipped[0][0]]
    y_vals = [p[1] for p in clipped] + [clipped[0][1]]
    ax[1].plot(x_vals,y_vals,marker='o',color='green')

ax[1].set_title("After clipping")
ax[1].set_aspect('equal')
ax[1].grid(True)

plt.tight_layout()
plt.show()
