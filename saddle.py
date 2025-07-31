import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the grid
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

# Define the saddle function: z = x^2 - y^2
Z = X**2 - Y**2

# Create the figure and 3D axis
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surf = ax.plot_surface(X, Y, Z, cmap='gray', alpha=0.8, edgecolor='k')

# Mark the saddle point at (0, 0, 0)
ax.scatter(0, 0, 0, color='black', s=50, label='Saddle Point')

# Add labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Saddle Point: $z = x^2 - y^2$')
ax.legend()

plt.show()
