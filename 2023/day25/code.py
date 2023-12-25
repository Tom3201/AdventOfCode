import networkx as nx

with open("data.txt") as f:
    data = f.read().splitlines()

g = nx.Graph()
for line in data:
    name, components = line.split(":")
    for component in components.split():
        g.add_edge(name, component)
        g.add_edge(component, name)

g.remove_edges_from(nx.minimum_edge_cut(g))
a, b = nx.connected_components(g)
print(len(a) * len(b))
