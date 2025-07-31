from ase import Atoms
from ase.io import write
from ase.io import read
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import cm

filename1 = "DOSCAR"
filename2 = "POSCAR"

#function readposcar reads the poscar cartesian file and returns a list of atoms and lattice
def readposcar (file_in_name):
   #open the input file
  filein = open(file_in_name,'r')
  #create a list for atoms
  #readatoms = []
  #Iterate through lines
  lattice=[]
  elements = []
  newelements = []
  atoms = []
  numberofelements = []
  coordinates = []

  for i, line in enumerate(filein):
      if i == 0:
        newlineno=line
      elif i == 1:
        newlineno=line
      elif i == 2:
        newline=line.split()
        lattice.append(float(newline[0]))
      elif i == 3:
        newline=line.split()
        lattice.append(float(newline[1]))
      elif i == 4:
        newline=line.split()
        lattice.append(float(newline[2]))
      elif i == 5:
        elements = line.split()
      elif i == 6:
        numberofelements = line.split()
        i=0
        while i < len(elements):
            numberofelements[i]=float(numberofelements[i])
            i=i+1
      elif i == 7:
         newlineno=line
      else:
         newline=line.split()
         newvalue=[float(newline[0]), float(newline[1]), float(newline[2])]
         coordinates.append(newvalue)
  filein.close()
  for element in elements:
     j=0
     while j < numberofelements[elements.index(element)]:
        newelements.append(element)
        j=j+1 
  j=0
  while j < len(newelements):
     #newvalue=[newelements[j], coordinates[j][0], coordinates[j][1], coordinates[j][2]]
     atoms.append(newelements[j])
     #
     j=j+1 
  return atoms

#function totaldosS reads total spin polarized DOS
def totaldosS (file_in_name,atoms):
  #open the input file
  energy = []
  dosup = []
  dosdown = []
  atomsdosup = []
  atomsdosdown = []
  filein = open(file_in_name,'r')
  alllines = filein.readlines()
  newline = alllines[5].split()
  numberofstates = int(newline[2])
  fermi = float(newline[3])
  uplimit = 10
  downlimit = -10
  
  i=6
  while i <= 5+numberofstates:
     currentline = alllines[i].split()
     if float(currentline[0])-fermi > downlimit and float(currentline[0])-fermi < uplimit:
        energy.append(float(currentline[0])-fermi)
        dosup.append(float(currentline[1]))
        dosdown.append(-float(currentline[2]))
     i=i+1
  j=0
  while j < len(atoms):
     startingi = 5+numberofstates+2+j*(1+numberofstates)
     i=startingi
     newdosup = []
     newdosdown = []
     #print(i)
     while i < startingi+numberofstates:
        currentline = alllines[i].split()
        if float(currentline[0])-fermi > downlimit and float(currentline[0])-fermi < uplimit:
        #print(currentline)
           newdosup.append(float(currentline[1])+float(currentline[3])+float(currentline[5])+float(currentline[7])+float(currentline[9])+float(currentline[11])+float(currentline[13])+float(currentline[15])+float(currentline[17]))
           newdosdown.append(-float(currentline[2])-float(currentline[4])-float(currentline[6])-float(currentline[8])-float(currentline[10])-float(currentline[12])-float(currentline[14])-float(currentline[16])-float(currentline[18]))
        i=i+1
     atomsdosup.append(newdosup)
     atomsdosdown.append(newdosdown)
     j=j+1
  j=len(atoms)-1

  while j > 0:
     if atoms[j] == atoms[j-1]:
        atomsdosup[j-1]=[x + y for x, y in zip(atomsdosup[j], atomsdosup[j-1])]
        atomsdosup.pop(j)
        atomsdosdown[j-1]=[x + y for x, y in zip(atomsdosdown[j], atomsdosdown[j-1])]
        atomsdosdown.pop(j)
        atoms.pop(j)
        j=j-1
     else: 
      j=j-1



  j=0
#  plt.subplot(2, 1, 1)
  n=len(atoms)
  color = iter(cm.rainbow(np.linspace(0, 1, n)))
  while j < len(atoms):
    c = next(color)
    plt.plot(energy, atomsdosup[j], label=atoms[j], color=c)
    plt.plot(energy, atomsdosdown[j], color=c)    
    j=j+1 
  plt.legend(loc='upper left')

  plt.savefig('dos.png')

  #Close the file when you're done
  filein.close()

totaldosS(filename1,readposcar(filename2))
