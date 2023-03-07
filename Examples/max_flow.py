from pyscipopt import Model

# data creation
V = [0,1,2,3,4,5]
s, t = V[0], V[-1] # source and target are first and last 
C = {}
C[s,1] = 2.3
C[s,2] = 1.7
C[1,3] = 1.2
C[2,1] = 0.6
C[2,4] = 1.9
C[3,2] = 0.5
C[3,4] = 1.2
C[3,t] = 0.8
C[4,t] = 2  

N = {s:[1,2],1:[3],2:[1,4],3:[2,4,t],4:[t],t:[]} # set of destinations

# model creation
m = Model()             

f = {}
for u,v in C:
    f[u,v] = m.addVar(lb=0,ub=C[u,v]) # flow variable with capacity

for v in V:
    if v == s or v == t:
        continue
    inflow = 0
    for u in N:
        if v in N[u]:
            inflow = inflow + f[u,v]
    outflow = sum(f[v,w] for w in N[v])
    m.addCons(inflow - outflow == 0) # flow conservation

m.setObjective(sum(f[s,v] for v in N[s]), "maximize") # max-flow  


try: # plot the result using networkx and matplotlib
    import networkx as nx
    import matplotlib.pyplot as plt

    plt.clf()
    G = nx.DiGraph()

    G.add_nodes_from(V)
    for (i,j) in C:
        G.add_edge(i,j,color="black")

    edges = G.edges()
    
    #position = nx.drawing.layout.spring_layout(G)
    position = {}
    position[0] = (0,0)
    position[1] = (2,1)
    position[2] = (2,-1)
    position[3] = (4,1)
    position[4] = (4,-1)
    position[5] = (6,0)

    nx.draw(G,position,node_color="black",nodelist=V)

    edge_labels = {}
    for (i,j) in C:
        edge_labels[i,j] = C[i,j]
    nx.draw_networkx_edge_labels(G,position,edge_labels=edge_labels)
    
    node_labels ={}
    for v in V:
        node_labels[v] = str(v)

    nx.draw_networkx_labels(G,position,labels=node_labels,font_color="white")
    plt.show()

    m.optimize()

    plt.clf()
    G = nx.DiGraph()

    G.add_nodes_from(V)
    for (i,j) in C:
        if round(m.getVal(f[i,j]),1) == C[i,j]:
            G.add_edge(i,j,color="r",weight=5,label='a')
        else:
            G.add_edge(i,j,color="g", weight=2, label='a')

    edges = G.edges()
    colors = [G[u][v]["color"] for u,v in edges]
    widths = [G[u][v]["weight"] for u,v in edges]
    labels = [G[u][v]["label"] for u,v in edges]
    
    #position = nx.drawing.layout.spring_layout(G)
    position = {}
    position[0] = (0,0)
    position[1] = (2,1)
    position[2] = (2,-1)
    position[3] = (4,1)
    position[4] = (4,-1)
    position[5] = (6,0)

    nx.draw(G,position,node_color="black",nodelist=V, edge_color=colors, width=widths)

    edge_labels = {}
    for (i,j) in C:
        edge_labels[i,j] = "%.1f/%.1f"%(round(m.getVal(f[i,j]),1),C[i,j])
    nx.draw_networkx_edge_labels(G,position,edge_labels=edge_labels)
    
    node_labels ={}
    for v in V:
        node_labels[v] = str(v)

    nx.draw_networkx_labels(G,position,labels=node_labels,font_color="white")
    plt.show()
except ImportError:
    m.optimize()
    print("install 'networkx' and 'matplotlib' for plotting")
