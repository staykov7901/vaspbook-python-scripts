import numpy as np
import matplotlib.pyplot as plt
from pymatgen.io.vasp.outputs import Locpot, Outcar

# === Load Data ===
locpot = Locpot.from_file("LOCPOT")
outcar = Outcar("OUTCAR")

# === Extract Potential Grid ===
pot_data = locpot.data['total']
line_profile = np.mean(np.mean(pot_data, axis=0), axis=0)

# === Define z-axis ===
z_len = locpot.structure.lattice.c
z = np.linspace(0, z_len, len(line_profile))

# === Extract Fermi Level ===
fermi_energy = outcar.efermi  # in eV

# === Extract Vacuum Potential (last point) ===
vacuum_potential = line_profile[-1]

# === Calculate Work Function ===
work_function = vacuum_potential - fermi_energy

# === Console Output ===
print(f"Vacuum potential at z = c: {vacuum_potential:.3f} eV")
print(f"Fermi level: {fermi_energy:.3f} eV")
print(f"Work function: {work_function:.3f} eV")


# === Plot ===
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(z, line_profile, label='Electrostatic Potential (z-profile)', color='blue')

# Plot the Fermi level as a horizontal line
ax.axhline(y=fermi_energy, color='red', linestyle='--', label=f'Fermi = {fermi_energy:.2f} eV')

# Scatter point for vacuum potential
ax.scatter(z[-1], vacuum_potential, color='green', label=f'Vacuum = {vacuum_potential:.2f} eV')

# Set labels and title
ax.set_xlabel('z (Å)')
ax.set_ylabel('Potential (eV)')
ax.set_title('Electrostatic Potential Profile from LOCPOT')
ax.grid(True)

# === Adjust Legend and Annotations ===
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=2, frameon=False)

# === Space for bottom annotation ===
fig.tight_layout()
fig.subplots_adjust(bottom=0.25)
fig.text(0.1, 0.1, f'WF = {work_function:.2f} eV', ha='center', fontsize=11, style='italic')

# Show plot
#plt.show()
plt.savefig('line.png')

