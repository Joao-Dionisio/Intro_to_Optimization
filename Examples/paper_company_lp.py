from pyscipopt import Model

m = Model() # Create a SCIP model

A = m.addVar("Type A") # add a SCIP variable to model m, call it "Type A", and assign it to a Python variable
B = m.addVar("Type B")

m.addCons(A <= 6000) # Add constraint to model m enforcing that the Python variable A (so SCIP variable called "Type A") is <= 6000 
m.addCons(B <= 4000)

m.addCons(A >= 0)
m.addCons(B >= 0)

m.addCons(A/200 + B/140 <= 40)

m.setObjective(25*A + 30*B, "maximize") # Set objective of model m, 25 times value of A + 30 times value of B. Maximization problem

m.optimize() # With the variables, the constraints, and the objective function, we optimize model m

print([(i.name, m.getVal(i)) for i in m.getVars()]) # A SCIP variable has a name attribute, which gives the name assigned at creation ("Type A", "Type B")
                                                    # To get the value of a variable (variable A, for example) of model m, use m.getVal(A) 
                                                    # To get all the variables of model m, use m.getVars()

####################################
"""

m2 = Model()

A = m2.addVar(lb=0, ub=6000) # We can directly add bound constraints (lower bound/upper bound) on variable creation, for simpler code
B = m2.addVar(lb=0, ub=4000)

m2.addCons(A/200 + B/140 <= 40)

m2.setObjective(25*A + 30*B, "maximize")

m2.optimize()

"""