import numpy as np
import matplotlib.pyplot as plt

# Radial coordinate
r = np.linspace(0, 5, 500)

# Parameters
zeta = 1.0   # Slater exponent
alpha = 0.5  # Gaussian exponent

# Slater-type orbital (unnormalized)
sto = np.exp(-zeta * r)

# Gaussian-type orbital (unnormalized)
gto = np.exp(-alpha * r**2)

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(r, sto, label='Slater-type Orbital (STO)', color='black')
plt.plot(r, gto, label='Gaussian-type Orbital (GTO)', color='black', linestyle='--')

plt.title('Comparison of Slater and Gaussian Orbitals')
plt.xlabel('Radial Distance (r)')
plt.ylabel('Wavefunction Value')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
