#!/usr/bin/env python

import numpy

def computeDist (pos1, pos2) :
        """
        Computes the distance between the points pos1 and pos2, which are points in 3D space

        Arguments
        pos1 -- Explain
        pos2 -- Explain        
        """
        # Note for students: Replace 'pass' with the body of this function
        pass

def computeEnergy (dist) :
        """
        Computes a Lennard-Jones energy for a pair of atoms with distance dist

        Arguments
        dist -- Explain        
        """
        # Note for students: Replace 'pass' with the body of this function
        # The expression for the Lennard-Jones energy is supplied in the PDF exam-file
        pass

def getTotalEnergy (positions) :
        """
        Computes the total Lennard-Jones energy (sum of all pairwise energies) for a set of atoms

        Arguments
        positions -- List of lists. Positions in 3D space for all atoms
        """
        # Note for students: Replace 'pass' with the body of this function
        # Both of the functions above are called in the body of this function
        pass

def getTotalEnergyFromMatrix ( matrix ) :
        """
        Computes the total Lennard-Jones energy from a matrix of distances
       
        Arguments 
        matrix -- A numpy array containing distances. Only the upper triangle should be filled
                  (zeros everywhere else)
        """
        # Note for students: Replace 'pass' with the body of this function
        # None of the functions above are called in the body of this function
        pass
i=0
new_list=[]
while i<len(c):
  new_list.append(c[i:i+3])
  i+=3
# Here the main function starts

# Question 1e
# Read the text in the supplied input file called positionfile.txt into a string. 
# The name of the file should be supplied on the command line


# Now use the shell command 'grep' to select the lines that contains the atomic positions.

# Convert the atomic posisions to floats and store them in a list. Store the positions of all atoms
# in a list of lists.


# Question 1f
# Use the function getTotalEnergy() to compute the total energy of this system of atoms.


# Question 1g
# Use the positions of 1e to create a numpy matrix of distances
# Try to make this process as efficient as you can

# Now compute the total energy from the matrix of distances, using the above function

# Question 1h
# Use the text obtained in Question 1e. Find out how many times each word occurs in the file, and print the two most frequently used words to screen.
