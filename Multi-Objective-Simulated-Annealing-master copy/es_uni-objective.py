#! /usr/bin/python
# -*- coding: utf-8 -*-

import math
import random

# Number of districts
with open("phase2_inputs/inputs20/input20_9.in", "r") as f:
    read = []
    for line in f:
        read.append(line.strip())

# information we are given
num_of_wizards = read[0]
num_of_constraints = read[1]
constraints = []
wizards = set()
for line in read[2:]:
    for wizard in line.split():
        wizards.add(wizard)
    constraints.append(line.split())
state = list(wizards)

districts_number = 16
maximun_bomber_stations = 5
maximun_bomber_in_district = 1

# Districts neighbors
neighbors = state


def districtsCoverBySomeSolution(stations):
    """
    Calculate the number of districts cover by one solution
    Given a bomber station (for each one), return all adjacent neighbors.
    """
    districts_cover = dict()
    cent = False
    cont = 0
    while cont < len(stations):
        # Itself is cover
        if stations[cont] > 0:
            districts_cover[cont+1] = True
            # Get all neighbors from station-district location
            #print cont+1,' ',neighbors[cont+1]
            for distrito in neighbors[cont+1]:
                districts_cover[distrito] = True
                # Exit loop if all districts all cover
                if len(districts_cover) == districts_number:
                    cent = True
        cont += 1
    return districts_cover
    
def f1(solution):
    """
    WE SHOULD TO MAXIMIZE
    This function calculate the districts cover by one vector of solution.
    This vector is the index where bombers has a station.
    """
    return float(len(districtsCoverBySomeSolution(solution)))
    
def f2(solution):
    """
    WE SHOULD TO MINIMIZE
    Calculate the number of overlaps.
    """
    acum = 0
    n = len(solution)
    i = 0
    # For each bomber station in the solution, calculate the overlaps
    # with the next other bomber stations in solutions vector
    while i < n - 1:
        if solution[i] > 0:
            # Next solutions given i
            j = i + 1
            while j < n:
                if solution[j] > 0:
                    # Sumarize overlaps between neighbors
                    if len(set(neighbors[i + 1]) & set(neighbors[j + 1])) > 1:
                        acum += len(set(neighbors[i + 1]) & set(neighbors[j + 1]))
                j += 1
        i += 1
    return acum
    
    
def f3(solution):
    """
    This function is the global aproach to solve the main problem, try
    to maximize the sum of (maximize #1 function + maximize - #2 function)
    """
    return -0.8*f1(solution) + 0.2*f2(solution) 
    

def generateRandSolution(x = None):
    """
    Generate a vector with random values
    If x is None, this function create one new random vector,
    if it is not, copy x vector and permut two position in order
    to get a new individual of x entorn.
    """
    solution = []
    if x == None:
        for i in range(1 , districts_number+1):
            solution.append(random.randrange(0 , maximun_bomber_in_district))
    else:
        for i in x:
            solution.append(i)
        n = len(solution)
        # Apply two random transformations in two positions in order to
        # get a "near" new solution
        for i in range(0 , 2):
            rand_index = random.randrange(1 , n)
            # 0.5 of propability in each branch
            if random.random() < 0.5:
                solution[rand_index] +=  1
            else:
                solution[rand_index] -=  1
            # Check if values are in range [0 .. N]
            if solution[rand_index] < 0:
                solution[rand_index] = 0
            elif solution[rand_index] > maximun_bomber_in_district:
                solution[rand_index] = maximun_bomber_in_district
    return solution
    

# General algorithm parameters    
params = {}
# Initial temperature
params['temperature'] = 100.0
# Cooling factor
params['alpha'] = 0.9
# Steps number keeping the temperature
params['np'] = 20
# Final temperature
params['final_temperature'] = 0.01
# Number of iterations without improving
params['number_iterations_without_improves'] = 2000
# Total number of iterations
params['nnum'] = 0  

PE = []

# Generate random initial solution 
x = generateRandSolution()
#x = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
PE.append(x)
n = 0
# Start the algorithm
cont = 0
while (params['temperature'] > params['final_temperature'] and
        params['nnum'] < params['number_iterations_without_improves']):
    # Get solution of x entorn
    y = generateRandSolution(x)
    # Calculate distance between two solutions
    delta = f(y) - f(x)
    # If delta is better, accept new solution
    if delta < 0.0:
        x = []
        x.extend(y)
    # If it is not better, compute probabilities to accept other solutions
    else:
        if (random.random() < math.exp(- float(delta) / params['temperature'])):
            x = []
            x.extend(y)
    # Low temperature
    if params['nnum'] % params['np'] == 0:
        params['temperature'] *= params['alpha']
    params['nnum'] += 1
    print f3(x)

print '-----------------'
print x
print 'f1: %f' % f1(x)
print 'f2: %f' % f2(x)
print 'f: %f' % f(x)
print len(districtsCoverBySomeSolution(x))



