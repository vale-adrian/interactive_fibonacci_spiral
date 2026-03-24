import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Arc
from matplotlib.widgets import Slider

def get_fibonacci(n):
    """Generate the first n Fibonacci numbers (starting 1, 1, 2, 3...)."""
    fibs = [1, 1]
    for _ in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

# Setting the maximum number 'n' supported by slider
MAX_N = 80
fibs = get_fibonacci(MAX_N)

# Computing the anchor centers for the arcs
centers = [(0, 0), (0, 0)]
# Directions correspond to moving the center: Up, Left, Down, Right
dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
for i in range(2, MAX_N):
    prev_c = centers[-1]
    d = dirs[(i - 2) % 4]
    new_c = (prev_c[0] + d[0] * fibs[i-2], prev_c[1] + d[1] * fibs[i-2])
    centers.append(new_c)

# Plotting the figure
fig, ax = plt.subplots(figsize=(8, 8))
plt.subplots_adjust(bottom=0.15) 

def draw_spiral(n):
    """Draws the Fibonacci spiral up to the nth term."""
    ax.clear()
    
    min_x = min_y = float('inf')
    max_x = max_y = float('-inf')
    
    for i in range(n):
        R = fibs[i]
        cx, cy = centers[i]
        q = i % 4
        
        # Determining the bounding box of the square based on the current quadrant
        if q == 0:
            x0, x1 = cx - R, cx
            y0, y1 = cy, cy + R
        elif q == 1:
            x0, x1 = cx - R, cx
            y0, y1 = cy - R, cy
        elif q == 2:
            x0, x1 = cx, cx + R
            y0, y1 = cy - R, cy
        else: # q == 3
            x0, x1 = cx, cx + R
            y0, y1 = cy, cy + R
            
        # Track min/max boundaries to keep the camera focused
        min_x, max_x = min(min_x, x0), max(max_x, x1)
        min_y, max_y = min(min_y, y0), max(max_y, y1)
        
        # Draw the underlying square
        rect = Rectangle((x0, y0), R, R, fill=False, edgecolor='steelblue', alpha=0.5, linestyle='--')
        ax.add_patch(rect)
        
        # Draw the quarter-circle arc
        start_angle = 90 + i * 90
        end_angle = start_angle + 90
        arc = Arc((cx, cy), R * 2, R * 2, angle=0, theta1=start_angle, theta2=end_angle, 
                  color='crimson', linewidth=2.5)
        ax.add_patch(arc)
        
    # Dynamically adjust the view limits with a little padding
    if n > 0:
        pad = max(max_x - min_x, max_y - min_y) * 0.05
        if pad == 0: pad = 1
        ax.set_xlim(min_x - pad, max_x + pad)
        ax.set_ylim(min_y - pad, max_y + pad)
        
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(f"Fibonacci Spiral up to n={n}  (F_{n} = {fibs[n-1]})", fontsize=14, pad=15)

# Set the initial state for the plot
initial_n = 7
draw_spiral(initial_n)

# Add the interactive slider at the bottom
ax_slider = plt.axes([0.15, 0.05, 0.7, 0.03])
slider = Slider(ax_slider, 'n', 1, MAX_N, valinit=initial_n, valstep=1)

# Update function triggered when the slider is moved
def update(val):
    draw_spiral(int(slider.val))
    fig.canvas.draw_idle()

slider.on_changed(update)

# Launch the visualizer
plt.show()