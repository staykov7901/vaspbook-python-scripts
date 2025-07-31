import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Spherical coordinate parameters
r = 1
theta = np.pi / 4  # azimuthal angle (xy-plane)
phi = np.pi / 3    # polar angle (from z-axis)

# Convert point to Cartesian coordinates
x = r * np.sin(phi) * np.cos(theta)
y = r * np.sin(phi) * np.sin(theta)
z = r * np.cos(phi)

# Create mesh for sphere surface
theta_sphere, phi_sphere = np.meshgrid(np.linspace(0, 2 * np.pi, 100),
                                       np.linspace(0, np.pi, 100))
x_sphere = r * np.sin(phi_sphere) * np.cos(theta_sphere)
y_sphere = r * np.sin(phi_sphere) * np.sin(theta_sphere)
z_sphere = r * np.cos(phi_sphere)

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot full sphere surface
ax.plot_surface(x_sphere, y_sphere, z_sphere, color='gray', alpha=0.3, edgecolor='none')

# Plot radius vector
ax.plot([0, x], [0, y], [0, z], color='black', linewidth=2, label='r (radius)')
ax.scatter([x], [y], [z], color='black', s=100)

# Theta arc (in xy-plane)
theta_arc = np.linspace(0, theta, 100)
arc_x = 0.4 * np.cos(theta_arc)
arc_y = 0.4 * np.sin(theta_arc)
arc_z = np.zeros_like(theta_arc)
ax.plot(arc_x, arc_y, arc_z, 'k', linestyle=':', label='θ (theta)')

# Phi arc (from z-axis to r)
phi_arc = np.linspace(0, phi, 100)
arc_x_phi = 0.4 * np.sin(phi_arc) * np.cos(theta)
arc_y_phi = 0.4 * np.sin(phi_arc) * np.sin(theta)
arc_z_phi = 0.4 * np.cos(phi_arc)
ax.plot(arc_x_phi, arc_y_phi, arc_z_phi, 'k', linestyle='--', label='φ (phi)')

# Axis settings
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Spherical Coordinates')

# Set symmetric limits for full sphere visibility
ax.set_box_aspect([1, 1, 1])
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

ax.legend()
plt.show()
