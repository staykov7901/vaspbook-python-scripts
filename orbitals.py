import numpy as np
import matplotlib.pyplot as plt
from scipy.special import sph_harm, genlaguerre
from mpl_toolkits.mplot3d import Axes3D

# Orbital quantum numbers
n, l, m = 3, 1, 0

# ---------- RADIAL FUNCTION R_nl ----------
# Bohr radius (in atomic units)
a0 = 1.0

def R_nl(r):
    """Normalized radial function for hydrogen atom (atomic units)"""
    # Radial prefactor
    rho = 2 * r / (n * a0)
    normalization = np.sqrt((2 / (n * a0))**3 * np.math.factorial(n - l - 1) / 
                            (2 * n * np.math.factorial(n + l)))
    laguerre = genlaguerre(n - l - 1, 2 * l + 1)(rho)
    return normalization * np.exp(-rho / 2) * rho**l * laguerre

# ---------- ANGULAR PLOT ----------
# Spherical grid
phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(0, np.pi, 100)
phi, theta = np.meshgrid(phi, theta)

# Angular wavefunction
Y_lm = sph_harm(m, l, phi, theta).real
r_ang = np.abs(Y_lm)

# Spherical to Cartesian for orbital shape
x = r_ang * np.sin(theta) * np.cos(phi)
y = r_ang * np.sin(theta) * np.sin(phi)
z = r_ang * np.cos(theta)

# Color map: blue = +, red = −
norm = plt.Normalize(vmin=-np.max(np.abs(Y_lm)), vmax=np.max(np.abs(Y_lm)))
colors = plt.cm.seismic(norm(Y_lm))

# ---------- RADIAL PLOT ----------
r_vals = np.linspace(0, 20, 500)
R_vals = R_nl(r_vals)
P_vals = r_vals**2 * R_vals**2  # radial probability density

# ---------- PLOTS ----------
fig = plt.figure(figsize=(14, 6))

# Subplot 1: Angular 3D shape
ax1 = fig.add_subplot(1, 3, 1, projection='3d')
ax1.plot_surface(x, y, z, facecolors=colors, rstride=1, cstride=1, antialiased=True, shade=False)
ax1.set_title(f"{n}{['s','p','d','f'][l]} orbital (m={m}) — Angular part", fontsize=12)
ax1.axis('off')
ax1.set_box_aspect([1, 1, 1])

# Subplot 2: Radial part
ax2 = fig.add_subplot(1, 3, 2)
ax2.plot(r_vals, R_vals, color='black', linewidth=2)
ax2.set_title("Wavefunction", fontsize=12)
ax2.set_xlabel("Distance from nucleus (Bohr radii)")
ax2.set_ylabel(r"$R_{nl}(r)$")
ax2.grid(True)

# Subplot 3: Density part
ax3 = fig.add_subplot(1, 3, 3)
ax3.plot(r_vals, P_vals, color='black', linewidth=2)
ax3.set_title("Radial Probability Density", fontsize=12)
ax3.set_xlabel("Distance from nucleus (Bohr radii)")
ax3.set_ylabel(r"$r^2 |R_{nl}(r)|^2$")
ax3.grid(True)

plt.tight_layout()
plt.show()
