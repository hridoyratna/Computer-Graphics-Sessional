import matplotlib.pyplot as plt 
import numpy as np 
 
xmin, xmax = 20, 60 
ymin, ymax = 20, 60 
 
cx, cy, r = 30, 40, 15 
 
theta = np.linspace(0, 2*np.pi, 800) 
circle_points = [(cx + r*np.cos(t), cy + r*np.sin(t)) 
for t in theta] 
 
def inside(p): 
    x, y = p 
    return xmin <= x <= xmax and ymin <= y <= ymax 
 
clipped_points = [p for p in circle_points if inside(p)] 
 
fig, axs = plt.subplots(1, 2, figsize=(12, 5)) 
 
axs[0].plot([xmin, xmax, xmax, xmin, xmin], 
            [ymin, ymin, ymax, ymax, ymin], 'k-') 
 
axs[0].plot([p[0] for p in circle_points], 
            [p[1] for p in circle_points], 
            color='blue') 
 
axs[0].set_title("Curve Clipping - Before") 
axs[0].set_aspect('equal') 
axs[0].grid(True) 
 
axs[1].plot([xmin, xmax, xmax, xmin, xmin], 
            [ymin, ymin, ymax, ymax, ymin], 'k-') 
 
axs[1].plot([p[0] for p in clipped_points], 
            [p[1] for p in clipped_points], 
            color='green') 
 
axs[1].set_title("Curve Clipping - After") 
axs[1].set_aspect('equal') 
axs[1].grid(True) 
 
plt.tight_layout() 
plt.show() 