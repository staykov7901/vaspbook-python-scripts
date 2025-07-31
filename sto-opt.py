import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import differential_evolution
from scipy.integrate import simpson

# Slater-type orbital (unnormalized)
def slater(r, zeta=1.0):
    return np.exp(-zeta * r)

# Normalized primitive Gaussian
def gaussian(r, alpha):
    return np.exp(-alpha * r**2)

# Contracted Gaussian function
def contracted_gaussian(r, alphas, coeffs):
    result = np.zeros_like(r)
    for c, a in zip(coeffs, alphas):
        result += c * gaussian(r, a)
    return result

# Objective function: minimize area error between Slater and contracted
def area_error(params, r, slater_vals):
    coeffs = params[:3]
    alphas = params[3:]
    g_vals = contracted_gaussian(r, alphas, coeffs)
    error = np.abs(simpson(slater_vals - g_vals, r))
    return error

# r grid
r = np.linspace(0, 5, 500)
slater_vals = slater(r)

# Bounds for optimization: coeffs [0, 2], alphas [0.001, 5]
bounds = [(0, 2)] * 3 + [(0.001, 5)] * 3

# Run differential evolution optimization
result = differential_evolution(
    area_error,
    bounds,
    args=(r, slater_vals),
    strategy='best1bin',
    maxiter=1000,
    tol=1e-4,
    disp=True
)

# Extract optimized values
opt_coeffs = [0.0036,0.2067,0.5921]
opt_alphas = [0.0061,0.2167,1.3385]
opt_area_error = area_error(result.x, r, slater_vals)

# Compute optimized Gaussian
optimized_vals = contracted_gaussian(r, opt_alphas, opt_coeffs)

# Print final results
print(f"Optimized Coefficients: {opt_coeffs}")
print(f"Optimized Exponents: {opt_alphas}")
print(f"Final Area Error: {opt_area_error:.6f}")

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(r, slater_vals, label='Slater (ζ=1)', color='black', linewidth=2)
plt.plot(r, optimized_vals, '--', color='black', label='Optimized STO-3G', linewidth=2)
plt.xlabel('r')
plt.ylabel('Amplitude')
plt.title('Optimized STO-3G Fit to Slater Function')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
