import argparse
from anneal import Annealer
import math
import random

"""
======================================================================
  Complete the following function.
======================================================================
"""
class WizardSolver(Annealer):

    """Test annealer with a wizard sorting problem.
    """

    # pass extra data (the distance matrix) into the constructor
    
    # state = list of wizard names
    # constraints = list of constraints
    def __init__(self, state, constraints):
        self.constraints = constraints
        self.state = state
        super(WizardSolver, self).__init__(state)  # important!

    def move(self):
        """Swaps two wizards in the list."""
        a = random.randint(0, len(self.state) - 1)
        b = random.randint(0, len(self.state) - 1)
        self.state[a], self.state[b] = self.state[b], self.state[a]

    def energy(self):
        """Calculates the number of constraints the list passes""" 
        e = 0
        for i in range(len(self.constraints)):
            constraint = self.constraints[i]
            if self.state.index(constraint[2]) > self.state.index(constraint[1]) and self.state.index(constraint[1]) > self.state.index(constraint[0]):
                e += 1
            if self.state.index(constraint[2]) > self.state.index(constraint[0]) and self.state.index(constraint[0]) > self.state.index(constraint[1]): 
                e += 1
            if self.state.index(constraint[2]) < self.state.index(constraint[0]) and self.state.index(constraint[0]) < self.state.index(constraint[1]): 
                e += 1
            if self.state.index(constraint[2]) < self.state.index(constraint[1]) and self.state.index(constraint[1]) < self.state.index(constraint[0]): 
                e += 1
        return e
        

def solve(num_wizards, num_constraints, wizards, constraints):
    """
    Write your algorithm here.
    Input:
        num_wizards: Number of wizards
        num_constraints: Number of constraints
        wizards: An array of wizard names, in no particular order
        constraints: A 2D-array of constraints, 
                     where constraints[0] may take the form ['A', 'B', 'C']i

    Output:
        An array of wizard names in the ordering your algorithm returns
    """
    read_input("phase2_inputs/inputs20/input20_0.in")
    wiz = WizardSolver(wizards, constraints)
    best_state, energy= wiz.anneal()
    return best_state

"""
======================================================================
   No need to change any code below this line
======================================================================
"""

def read_input(filename):
    with open(filename) as f:
        num_wizards = int(f.readline())
        num_constraints = int(f.readline())
        constraints = []
        wizards = set()
        for _ in range(num_constraints):
            c = f.readline().split()
            constraints.append(c)
            for w in c:
                wizards.add(w)
                
    wizards = list(wizards)
    return num_wizards, num_constraints, wizards, constraints

def write_output(filename, solution):
    with open(filename, "w") as f:
        for wizard in solution:
            f.write("{0} ".format(wizard))

if __name__=="__main__":
    parser = argparse.ArgumentParser(description = "Constraint Solver.")
    parser.add_argument("input_file", type=str, help = "___.in")
    parser.add_argument("output_file", type=str, help = "___.out")
    args = parser.parse_args()

    num_wizards, num_constraints, wizards, constraints = read_input(args.input_file)
    solution = solve(num_wizards, num_constraints, wizards, constraints)
    write_output(args.output_file, solution)