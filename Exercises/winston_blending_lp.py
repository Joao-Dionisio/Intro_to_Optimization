from pyscipopt import Model, quicksum

# data

buying_price = [45,35,25]
selling_price = [70,60,50]
refine_cost = 4
demand = [3000,2000,1000]
availability = [5000,5000,5000]

octane_gas = [10,8,6]
octane_oil = [12,6,8]

sulfur_gas = [1,2,1]
sulfur_oil = [0.5,2,3]

m = Model()

x = {}
for i in range(3):
    for j in range(3):
        x[i,j] = m.addVar("x[%i,%i]"%(i,j))

ads = {}
for i in range(3):
    ads[i] = m.addVar("ads[%i]"%i)

# demand satisfaction
for i in range(3):
    m.addCons(quicksum(x[i,j] for j in range(3)) == demand[i] + ads[i])

# oil limit
for j in range(3):
    m.addCons(quicksum(x[i,j] for i in range(3)) <= availability[j])

# refinery capacity
m.addCons(quicksum(x[i,j] for i in range(3) for j in range(3)) <= 14000)

# octane rating
for i in range(3):
    m.addCons(quicksum(octane_oil[j]*x[i,j] for j in range(3)) >= octane_gas[i]*quicksum(x[i,j] for j in range(3)))

# sulfur content
for i in range(3):
    m.addCons(quicksum(sulfur_oil[j]*x[i,j] for j in range(3)) <= sulfur_gas[i]*quicksum(x[i,j] for j in range(3)))

revenue = quicksum(selling_price[i]*x[i,j] for i in range(3) for j in range(3))
cost = quicksum(buying_price[j]*x[i,j] for i in range(3) for j in range(3)) + quicksum(refine_cost*x[i,j] for i in range(3) for j in range(3))
ads = quicksum(ads[i] for i in range(3))

# Revenue - cost - ads
m.setObjective(revenue-cost-ads)


m.optimize()

print([(var.name, m.getVal(var)) for var in m.getVars()])