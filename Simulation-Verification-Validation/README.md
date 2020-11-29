## Introduction
This code is written as part of the SVV course in the Aerosace Engineering Programme of Delft University of Technology by group A34.
The code calculates and visualizes stress distribution of an aft airplane fuselage subject to vertical stabilizer load (torsion and bending).
Authorship of separate files is identified in each individual files' header. 

## DEPENDENCIES:

numpy >= 1.8.1
matplotlib >= 1.4.2. 

## GETTING STARTED:

To run the code with the inputs for the assignment set to the A34 group, (Boeing777), just run the main.py file in the parent folder. It will use the input from input.csv and automatically visualize partial stress distributions as well as side-by-side comparison of the von Mises stress distributions computed by the code and the von Mises stress "observed" as defined in the validation.rpt file, provided for validation purposes.


## STRUCTURE:

main.py -- contains the main execution routine and the plotting routines

input.csv -- contains the input used by the program for solving the loadcase

validation.rtp -- contains the data used for validation purposes

base.py -- contains the basic classes necessary for the implementation of the project

solversImports.py links the main program to the separate execution units

bmd.py -- contains the module computing the bending moment distribution and unit test for it

discretize.py -- contains the module computing the discretization and unit test for it

frameShear.py -- contains the module computing the shear flow in the frames and unit test for it

mohr.py -- contains the module computing the von Mises stress and unit test for it

qtorsion.py -- contains the module computing the torsional component of the shear flow and unit test for it

sectionProps.py -- contains the module computing the sectional properties and unit test for it

sfd.py -- contains the module computing the shear flow distribution and unit test for it

shearFlow.py -- contains the module computing the force-caused component of the shear flow and unit test for it

shearStress.py -- contains the module computing the shear stress from the shear flow and unit test for it

sigma.py -- contains the module computing the normal stress due to bending and unit test for it

statics.py -- contains the module computing the reaction forces and unit test for it

tmd.py -- contains the module computing the torsional moment distribution and unit test for it
