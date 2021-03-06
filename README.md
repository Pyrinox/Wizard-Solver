# Wizard-Solver

### Wizard Party Project Write Up
For our solution to the project, we decided to use the simulated annealing optimization library on Github (https://github.com/perrygeo/simanneal). The module efficiently solves the TSP problem and thus we reduce our Wizard Party Problem(WPP) to TSP. The algorithm finds the initial condition by randomizing and then keep that as the current best state. The module searches for the optimal state of a system by moving one random wizard using a random number generator. For faster runtime on our input files, we also used PyPy: a fast and compliant alternative implementation of the Python language.

The reason why simulated annealing is a good algorithm for solving the WPP is that it avoids getting caught in a local maxima/minimum. One challenge of the WPP is that moving one Wizard may break any arbitrary and unpredictable number of other constraints, as well as solve any number of constraints. Given this, the absolute minimum would be hidden in a very dense graph of wild oscillations, with many local maximums and local minimums to parse through. Using simulated annealing, we can attempt to find the true minimum. The true minimum varies by temperature, so we used one of the functions in the library called auto_schedule to generate an optimal maximum temperature, minimum temperature, and number of steps needed to generate the optimal solution.

We used memoization to save processing time by remembering the previous energy level, and preprocessed a dictionary with wizard names as the key and a list of all constraints involving that wizard as the value. Before we move the wizard, we keep track of the current number of constraints failing, as well as the wizard name. This will allow us to recalculate, after the move, the number of constraints involving that wizard that fail, and obtain a difference of number of the failing constraints. Using this difference and the previous energy level, we can determine whether a move was better or worse. If it is worse, do not update the previous energy level. If it is better, update the previous energy level and check to see it the current energy level is better than the best energy level (in which case, update the variable). By doing all of the above, we can avoid constantly having to recalculate energy levels using all of the constraints, saving us a significant amount of time.

#### The process of simulated annealing optimization goes as follows:
1. We generate our initial state by reading the input file from top to bottom.
2. We run the auto_schedule function on that state to get an optimal maximum
temperature, minimum temperature, and number of steps needed to generate the
optimal solution (this varies by input files).
3. Using these values as initial values, we randomly change the list of wizards (alter the
state of the list) with the move function. In our case, we move a single wizard and insert him/her back into the list at a random index. Before you actually move the wizard though, record the number of constraints that are currently being satisfied by the list.
4. We assess the energy of the new list. In our case, the energy is the number of constraints the list of wizards does not pass (since we want to minimize our energy and be consistent with the framework). We used memoization to avoid checking all the constraints every time we try to measure the energy. Using the knowledge that, by moving only one wizard, the only constraints that may break or pass must involve the wizard that was moved, we can avoid checking all of the constraints.
5. We then compare the energy to the previous energy and decide whether to accept the new list or reject it, based on the current temperature.
6. We repeated this process until we have passed all constraints.
