import numpy as np
import matplotlib.pyplot as plt

# Define the spatial grid
x = np.linspace(-10, 10, 500)

# Define atomic orbitals (1s-like) centered at -a and +a
a = 2.0  # Distance between atoms
def AO(x, center):
    return np.exp(-np.abs(x - center))  # Simple 1s-like orbital

# Atomic orbitals
ao1 = AO(x, -a)
ao2 = AO(x, +a)

# Normalize (not strictly necessary for visualization, but more realistic)
ao1 /= np.linalg.norm(ao1)
ao2 /= np.linalg.norm(ao2)

# Construct bonding and antibonding molecular orbitals
bonding = ao1 + ao2
antibonding = ao1 - ao2

# Normalize for display
bonding /= np.max(np.abs(bonding))
antibonding /= np.max(np.abs(antibonding))

# Plotting
fig, axs = plt.subplots(2, 2, figsize=(12, 6))

# Plot AO1
axs[0, 0].plot(x, ao1, label='AO (Atom A)', color='black')
axs[0, 0].set_title('Atomic Orbital - Atom A')
axs[0, 0].grid(True)
axs[0, 0].legend()

# Plot AO2
axs[0, 1].plot(x, ao2, label='AO (Atom B)', color='black')
axs[0, 1].set_title('Atomic Orbital - Atom B')
axs[0, 1].grid(True)
axs[0, 1].legend()

# Plot Bonding MO
axs[1, 0].plot(x, bonding, label='Bonding MO (AO1 + AO2)', color='black')
axs[1, 0].set_title('Bonding Molecular Orbital')
axs[1, 0].grid(True)
axs[1, 0].legend()

# Plot Antibonding MO
axs[1, 1].plot(x, antibonding, label='Antibonding MO (AO1 - AO2)', color='black')
axs[1, 1].set_title('Antibonding Molecular Orbital')
axs[1, 1].grid(True)
axs[1, 1].legend()

plt.tight_layout()
plt.show()
