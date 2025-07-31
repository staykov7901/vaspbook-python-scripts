import numpy as np
import matplotlib.pyplot as plt

# Define radial grid
r = np.linspace(0, 5, 500)
sto = np.exp(-r)  # Slater function with zeta = 1

# Primitive Gaussian function
def gaussian(r, alpha):
    return np.exp(-alpha * r**2)

# Contracted Gaussian
def contracted_gaussian(r, coeffs, exps):
    return sum(c * gaussian(r, a) for c, a in zip(coeffs, exps))

# Scale contracted function to lie fully within Slater function
def scale_to_fit(sto_vals, approx_vals):
    scale = np.min(sto_vals / (approx_vals + 1e-10))  # Avoid division by zero
    return approx_vals * scale

# STO-nG basis parameters
sto1g_coeffs = [1.0]
sto1g_exps = [0.270950]

sto2g_coeffs = [0.678914, 0.430129]
sto2g_exps = [0.151623, 0.851819]

sto3g_coeffs = [0.444635, 0.535328, 0.154329]
sto3g_exps = [0.109818, 0.405771, 2.22766]

# Evaluate and scale the contracted Gaussians
sto1g = contracted_gaussian(r, sto1g_coeffs, sto1g_exps)
sto2g = contracted_gaussian(r, sto2g_coeffs, sto2g_exps)
sto3g = contracted_gaussian(r, sto3g_coeffs, sto3g_exps)

sto1g_scaled = scale_to_fit(sto, sto1g)
sto2g_scaled = scale_to_fit(sto, sto2g)
sto3g_scaled = scale_to_fit(sto, sto3g)

# Plot both full and zoomed-in views
plt.figure(figsize=(12, 5))

# Subplot 1: Full range
plt.subplot(1, 2, 1)
plt.plot(r, sto, label='Slater (ζ=1)', color='black', linewidth=2)
plt.plot(r, sto1g_scaled, '--', color='black', label='STO-1G')
plt.plot(r, sto2g_scaled, ':', color='black', label='STO-2G')
plt.plot(r, sto3g_scaled, '.-', color='black', label='STO-3G')
plt.xlabel('r')
plt.ylabel('Amplitude')
plt.title('STO-nG Approximations Inside Slater Function')
plt.legend()
plt.grid(True)

# Subplot 2: Zoomed-in region (r > 3)
mask = r > 3
plt.subplot(1, 2, 2)
plt.plot(r[mask], sto[mask], label='Slater (ζ=1)', color='black', linewidth=2)
plt.plot(r[mask], sto1g_scaled[mask], '--', color='black',label='STO-1G')
plt.plot(r[mask], sto2g_scaled[mask], ':', color='black',label='STO-2G')
plt.plot(r[mask], sto3g_scaled[mask], '.-', color='black',label='STO-3G')
plt.xlabel('r')
plt.ylabel('Amplitude')
plt.title('Zoomed View: r > 3')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
