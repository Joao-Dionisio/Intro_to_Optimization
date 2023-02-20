from pyscipopt import Model, quicksum

steak_data = [370,60,20,10,15]
chicken_data = [270,8,2,20,20]
apple_data = [130,8,0,7,10]
hamburger_data = [500,40,40,35,10]
macaroni_data = [220,15,35,15,15]
veg_pie_data = [210,70,30,15,15]
rice_data = [215,25,50,25,15]
codfish_data = [170,60,20,15,10]

var_data =  [steak_data,chicken_data,apple_data,hamburger_data,macaroni_data,veg_pie_data,rice_data,codfish_data]

m = Model()

# To answer the second question of the exercise, the variables would need to be integer
steak = m.addVar("steak") # steak = m.addVar(vtype="I") <- like so
chicken = m.addVar("chicken")
apple = m.addVar("apple")
hamburger = m.addVar("hamburger")
macaroni = m.addVar("macaroni")
veg_pie = m.addVar("veg_pie")
rice = m.addVar("rice")
codfish = m.addVar("codfish")

vars = [steak,chicken,apple,hamburger,macaroni,veg_pie,rice,codfish]

for j in range(1,len(var_data[0])): # going over every nutrient
    m.addCons(quicksum(vars[i]*var_data[i][j] for i in range(len(vars))) >= 700) # the quantity of food, multiplied by its nutritional score, added up for every food, must exceed the weekly nutritional requirement 

m.setObjective(quicksum(vars[i]*var_data[i][0] for i in range(len(vars))))

m.optimize()

print([(var, m.getVal(var)) for var in m.getVars()])