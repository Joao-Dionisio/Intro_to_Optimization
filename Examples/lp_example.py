from pyscipopt import Model

m = Model()             # creates the Model m
x = m.addVar(lb=0)      # adds a variable to m with a lower bound of 0 and calls it x
y = m.addVar(lb = 2)    # same as above, with a lower bound of 3 and called y
m.addCons(x + 3*y <= 7) # adds a constraint to the model

m.setObjective(x+y)     # adds the objective to the model. By default, it is a minimization problem
m.optimize()            # optimizes model m