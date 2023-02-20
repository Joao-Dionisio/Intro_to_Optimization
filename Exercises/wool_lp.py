from pyscipopt import Model

m = Model()

A = m.addVar()
B = m.addVar()

m.addCons(0.4*A + 0.5*B <= 100) # kg of yellow wool used <= 100
m.addCons(0.5*A + 0.2*B <= 100)
m.addCons(0.3*A + 0.8*B <= 120)

m.setObjective(500*A + 200*B, "maximize")
m.optimize()