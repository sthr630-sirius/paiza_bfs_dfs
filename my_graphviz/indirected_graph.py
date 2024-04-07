from graphviz import Graph

def OutGraph(g, color, cnt):
    G = Graph(format="png")
    for i in range(len(g)):
        G.node(str(i), label=str(i+1), shape="circle", style="filled", color=color[i])
        for j in range(len(g[i])):
            G.edge(str(i), str(g[i][j]))
    G.render("./png/graph"+ str(cnt+1))
