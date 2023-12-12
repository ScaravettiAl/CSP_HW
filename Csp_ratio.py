from constraint import Problem
import random
import timeit
import numpy as np

def generate_CSP(num_var, num_constr):
    # Create a CSP problem
    problem = Problem()

    # List of variables
    variables = [f'variabile_{i}' for i in range(1, num_var + 1)]

    # Add variables and domains
    for variable_name in variables:
        problem.addVariable(variable_name, list(range(1, 10)))

    # Add constraints
    
    def sum_constraint(*values):
        return sum(values) <= random.randint(1,num_var*3)  


    for i in range (1,num_constr):
        problem.addConstraint(sum_constraint, variables)


    # Solve the problem
    solutions = problem.getSolutions()


max_var = 5
max_constr = 7

time_measure = np.zeros((max_var, max_constr))

for i in range (max_var):
    for j in range(max_constr):
     time_measure[i, j] = timeit.timeit(lambda : generate_CSP(i+1, j+1), number = 5)
    
print("Time: ", time_measure)

row_labels = [f'Vars={i}' for i in range(1, max_var + 1)]
col_labels = [f'Constraints={j}' for j in range(1, max_constr + 1)]

print("Execution Time Matrix:")
print("   ", end="")
for label in col_labels:
    print(f"{label: <15}", end="")
print()

for i, row in enumerate(time_measure):
    print(f"{row_labels[i]} |", end="")
    for value in row:
        print(f"{value: <15.6f}", end="")
    print()

#By varying the numbers of variables(1-5) and constraints(1-7) and writing the results in a 
# matrix(e.g. the element [3,6] is the time to execute a problem with 3 vars and 6 constraints)
# we conclude that time increases mainly with the increase of the number of variables, 
# while the number of constraints doesn't particularly affect the execution time   