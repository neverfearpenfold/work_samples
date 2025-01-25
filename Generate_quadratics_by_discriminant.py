#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""A tiny Python program to generate quadratic functions by discriminant.
All coefficients should be integers. Once you have that working, you're
ready for class -- you can edit and run Python code; now you just need
to learn Python!
"""

import sys
import math

target_discriminant = int(input("Please input the integer discriminant you want:"))
coefficient_bound = int(input("How big of a coefficient do you want? (e.g. 10 would be coefficients from -10 to +10): "))
print(f"Great! We'll only produce quadratics with coefficients between -{coefficient_bound} and {coefficient_bound}.")
print("""
( a , b , c) = ax\u00b2 + bx + c = y
-------------""")

how_many_quadratics = 0
coefficients = ()
list_of_coefficients = []

for i in range(-coefficient_bound,coefficient_bound+1,1):
    for j in range(-coefficient_bound,coefficient_bound+1,1):
        for k in range(-coefficient_bound,coefficient_bound+1,1):
            discrim = lambda i,j,k: j*j-4*i*k
            calculated_discriminant = discrim(i, j, k)
            
            if(calculated_discriminant == target_discriminant):
                coefficients = (i, j, k)
                list_of_coefficients.append(coefficients)
                how_many_quadratics += 1

print(f"There are {how_many_quadratics} different quadratics with discriminant = {target_discriminant}")
print(f"and coefficients between -{coefficient_bound} and +{coefficient_bound}")

for n in range(0,len(list_of_coefficients)):
    if(n==0):
        print(f"{list_of_coefficients[0]} = {list_of_coefficients[0][0]}x\u00b2 + {list_of_coefficients[0][1]}x + {list_of_coefficients[0][2]} = y")
    print(list_of_coefficients[n])
