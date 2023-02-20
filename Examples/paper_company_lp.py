from pyscipopt import Model

m = Model()

A = m.addVar()
B = m.addVar()

m.addCons(A <= 6000)
m.addCons(B <= 4000)

m.addCons(A >= 0)
m.addCons(B >= 0)

m.addCons(A/200 + B/140 <= 40)

m.setObjective(25*A + 30*B, "maximize")

m.optimize()

####################################

m2 = Model()

A = m2.addVar(lb=0, ub=6000)
B = m2.addVar(lb=0, ub=4000)

m2.addCons(A/200 + B/140 <= 40)

m2.setObjective(25*A + 30*B, "maximize")

m2.optimize()

