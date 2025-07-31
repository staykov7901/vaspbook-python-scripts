import numpy as np
import matplotlib.pyplot as plt
from scipy.special import sph_harm
from mpl_toolkits.mplot3d import Axes3D

# Set quantum numbers
l = 3
m = -2

# Validate input
if abs(m) > l:
    raise ValueError("Invalid input: |m| must be ≤ l.")

# Grid in spherical coordinates
theta = np.linspace(0, 2 * np.pi, 200)   # azimuthal angle
phi = np.linspace(0, np.pi, 100)         # polar angle
theta, phi = np.meshgrid(theta, phi)

# Compute spherical harmonic Y_l^m
Y_lm = sph_harm(m, l, theta, phi)

# Use the real part for visualization
Y_real = Y_lm.real

# Normalize to [0.2, 1.0] radius to ensure visibility for l=0,m=0
r_min = 0.2
r_max = 1.0
r = r_min + (np.abs(Y_real) - np.min(np.abs(Y_real))) / (
    np.max(np.abs(Y_real)) - np.min(np.abs(Y_real)) + 1e-9) * (r_max - r_min)

# Convert to Cartesian coordinates
x = r * np.sin(phi) * np.cos(theta)
y = r * np.sin(phi) * np.sin(theta)
z = r * np.cos(phi)

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot surface with color mapped to real part
surf = ax.plot_surface(
    x, y, z,
#uncomment the line below and coment the following if you want vivid colors instead of gray scale 
#    facecolors=plt.cm.viridis((Y_real - Y_real.min()) / (Y_real.max() - Y_real.min() + 1e-9)),
	facecolors=plt.cm.gray((Y_real - Y_real.min()) / (Y_real.max() - Y_real.min() + 1e-9)),
    rstride=1, cstride=1,
    antialiased=True, linewidth=0
)

# Titles and layout
ax.set_title(f"$Y_{{{l}}}^{{{m}}}(\\theta, \\phi)$", fontsize=24)
ax.set_axis_off()
ax.set_box_aspect([1, 1, 1])

plt.show()
