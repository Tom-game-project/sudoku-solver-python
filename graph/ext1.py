from graphviz import Digraph

G = Digraph(format="svg")
G.attr("node", shape="circle")
edges = [
    ("root","1"),
    ("1","1.1"),
    ("1","1.2"),
    ("root","2"),
    ("root","3"),

]
for i,j in edges:
    G.edge(str(i), str(j))
G.render("tree")
