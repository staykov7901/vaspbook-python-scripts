import numpy as np
import matplotlib.pyplot as plt
from scipy.special import hermite, factorial

# Parameters
n_max = 10
x = np.linspace(-4, 4, 1000)
m = 1.0
omega = 2.0
hbar = 1.0

# Constants
alpha = np.sqrt(m * omega / hbar)

# Potential: V(x) = (1/2) m ω² x²
V = 0.5 * m * omega**2 * x**2

# Wavefunction ψₙ(x)
def psi(n, x):
    Hn = hermite(n)(alpha * x)
    norm = 1.0 / np.sqrt((2**n) * factorial(n)) * (alpha / np.pi**0.25)**0.5
    return norm * Hn * np.exp(-0.5 * (alpha * x)**2)

# Energy: Eₙ = ℏω(n + 1/2)
def energy(n):
    return hbar * omega * (n + 0.5)

# Set up plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Plot the parabolic potential on both plots
ax1.plot(x, V, color='lightgray', label='V(x) = ½ mω²x²')
ax2.plot(x, V, color='lightgray', label='V(x) = ½ mω²x²')

for n in range(n_max + 1):
    E_n = energy(n)
    psi_n = psi(n, x)
    density_n = psi_n**2

    # Plot wavefunction and density offset by energy level
    ax1.plot(x, psi_n + E_n, color='k', label=f'n={n}')
    ax1.hlines(E_n, x[0], x[-1], colors='gray', linestyles='dotted')

    ax2.plot(x, density_n + E_n, color='k', label=f'n={n}')
    ax2.hlines(E_n, x[0], x[-1], colors='gray', linestyles='dotted')

# Formatting
for ax, title, ylabel in zip(
        [ax1, ax2],
        ["Wavefunctions ψₙ(x) + Eₙ", "Probability Densities |ψₙ(x)|² + Eₙ"],
        ["ψₙ(x) + Eₙ", "|ψₙ(x)|² + Eₙ"]
    ):
    ax.set_xlabel("Position x")
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(True)
    #ax.legend(loc='upper right')

plt.tight_layout()
plt.show()
