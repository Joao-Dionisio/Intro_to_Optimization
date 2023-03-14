from pyscipopt import Model, quicksum
import random

V = 500

E = {}
for i in range(V):
    for j in range(V):
        if i != j:
            if random.random() <= 0.8:
                E[i,j] = 1

m = Model()

x = {}
for i in range(V):
    #x[i] = m.addVar(lb=0)
    x[i] = m.addVar(vtype="INTEGER")

for i,j in E:
    m.addCons(x[i] + x[j] >= 1)

m.setObjective(quicksum(x[i] for i in range(V)))

m.optimize()
