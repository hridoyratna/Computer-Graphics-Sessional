import matplotlib.pyplot as plt

# Define clipping window boundaries
xmin, xmax = 50, 80
ymin, ymax = 10, 40

# Region codes for the 9 zones
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

def compute_outcode(x, y):
    code = INSIDE

    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP

    return code

def cohen_sutherland_line_clip(x0, y0, x1, y1):
    outcode0 = compute_outcode(x0, y0)
    outcode1 = compute_outcode(x1, y1)
    accept = False

    while True:
        if not (outcode0 | outcode1):
            # Both points are inside the window
            accept = True
            break
        elif outcode0 & outcode1:
            # Both points share an outside zone (trivially rejected)
            break
        else:
            # Line crosses a boundary, calculate intersection
            outcode_out = outcode1 if outcode1 > outcode0 else outcode0

            if outcode_out & TOP:
                x = x0 + (x1 - x0) * (ymax - y0) / (y1 - y0)
                y = ymax
            elif outcode_out & BOTTOM:
                x = x0 + (x1 - x0) * (ymin - y0) / (y1 - y0)
                y = ymin
            elif outcode_out & RIGHT:
                y = y0 + (y1 - y0) * (xmax - x0) / (x1 - x0)
                x = xmax
            elif outcode_out & LEFT:
                y = y0 + (y1 - y0) * (xmin - x0) / (x1 - x0)
                x = xmin

            # Update the point that was outside
            if outcode_out == outcode0:
                x0, y0 = x, y
                outcode0 = compute_outcode(x0, y0)
            else:
                x1, y1 = x, y
                outcode1 = compute_outcode(x1, y1)

    return accept, x0, y0, x1, y1


print("--- Cohen-Sutherland Line Clipping ---")
print(f"The clipping window is set at X:({xmin} to {xmax}), Y:({ymin} to {ymax})\n")

try:
    print("Please enter the coordinates for your line segment:")
    x0 = float(input("Enter starting X coordinate (x0): "))
    y0 = float(input("Enter starting Y coordinate (y0): "))
    x1 = float(input("Enter ending X coordinate (x1): "))
    y1 = float(input("Enter ending Y coordinate (y1): "))
except ValueError:
    print("\nInvalid input! Using default values (70, 20) to (100, 10).")
    x0, y0 = 70, 20
    x1, y1 = 100, 10

# Clip the line segment
accept, x0_clip, y0_clip, x1_clip, y1_clip = cohen_sutherland_line_clip(x0, y0, x1, y1)

# Plot the clipping window
plt.plot([xmin, xmax, xmax, xmin, xmin], [ymin, ymin, ymax, ymax, ymin], color='black', label='Clipping Window')

# Plot the original line segment (dashed so you can see what gets cut off)
plt.plot([x0, x1], [y0, y1], color='blue', linestyle='--', label='Original Line')

# Plot the clipped line segment
if accept:
    plt.plot([x0_clip, x1_clip], [y0_clip, y1_clip], color='green', linewidth=2.5, label='Clipped Line')
else:
    # If the line completely misses the window
    plt.text((x0 + x1) / 2, (y0 + y1) / 2, 'Line Rejected', color='red', fontsize=12, fontweight='bold')

# Formatting the graph
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Cohen-Sutherland Line Clipping')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()