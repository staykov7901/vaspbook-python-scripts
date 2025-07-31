# vaspbook-python-scripts

Python Scripts for the book: Ab Initio Simulations in Materials Science: Hands-On Introduction to Electronic Structure Modeling with VASP 
https://www.amazon.com/dp/B0FGSNL5QR

bonding.py: plots the overlap between two AO orbitals at two atoms, bonding and antibonding

dos.py: plots DOS using DOSCAR file obtained with LORBIT=11 option and POSCAR file. a POSCAR and DOSCAR are included in the repository

line.py: plots the electrostatic potential from a LOCPOT file and computes the workfunction. requires the OUTCAR file for the Fermi energy. Due to size limitations the LOCPOT is not supplied, however optimized CONTCAR of Fe2O3 surface slab is provided for easy computation

harmonic.py: plots 3D spherical harmonic functions

orbital.py: plots the angular part of an atomic orbital, radial part, and square of the radial part

oscilator.py: plots the lowest quantum levels of quantum oscillator in parabolic potential

particle_box.py: plots the lowest quantum levels of a particle in a box

saddle.py: plots the geometry of a saddle point used to visualize transition state

SlaterGauss.py: plots a comparison between a Slater and a Gauss functon for atomic orbitals

sphere.py: vizualizes spherical coordinate system

sto3g.py: demostrates contracted gaussian of sto3G basis set

sto-opt.py: plots optimized contracted gaussian function
