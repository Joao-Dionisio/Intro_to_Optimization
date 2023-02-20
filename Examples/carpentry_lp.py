from pyscipopt import Model

m = Model()                              
d = m.addVar(lb=0)                       # desks
t = m.addVar(lb=0)                       # tables
c = m.addVar(lb=0)                       # chairs
m.addCons(8*d + 6*t + c <= 40)           # boards 
m.addCons(4*d + 2*t + 1.5*c <= 20)       # finishes
m.addCons(2*d + 1.5*t + 0.5*c <= 8)      # carpentry

m.setObjective(60*d + 30*t + 20*c, "maximize")   
m.optimize()        