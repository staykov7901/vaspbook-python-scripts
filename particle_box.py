import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 3.0              # Length of the box
n_max = 4            # Number of states to plot
x = np.linspace(0, L, 1000)

# Define wavefunction
def psi(n, x, L):
    return np.sqrt(2 / L) * np.sin(n * np.pi * x / L)

# Define energy levels (natural units)
def energy(n, L):
    hbar = 1.0
    m = 1.0
    return (n**2 * np.pi**2 * hbar**2) / (2 * m * L**2)

# Set up side-by-side plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

for n in range(1, n_max + 1):
    E_n = energy(n, L)
    psi_n = psi(n, x, L)
    density_n = psi_n**2

    # Left: Wavefunctions offset by energy
    ax1.plot(x, psi_n + E_n, color='k', label=f'n={n}')
    ax1.hlines(E_n, 0, L, colors='gray', linestyles='dotted')

    # Right: Densities offset by energy
    ax2.plot(x, density_n + E_n, color='k', label=f'n={n}')
    ax2.hlines(E_n, 0, L, colors='gray', linestyles='dotted')

# Formatting
for ax, title, ylabel in zip(
        [ax1, ax2],
        ["Wavefunctions ψₙ(x) at Energy Levels", "Probability Densities |ψₙ(x)|² at Energy Levels"],
        ["ψₙ(x) + Eₙ", "|ψₙ(x)|² + Eₙ"]
    ):
    ax.set_xlim(0, L)
    ax.set_xlabel("Position x")
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    #ax.legend()
    ax.grid(True)
    ax.axvline(0, color='k', linestyle='--', linewidth=1)
    ax.axvline(L, color='k', linestyle='--', linewidth=1)

plt.tight_layout()
plt.show()
