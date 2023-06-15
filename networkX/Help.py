import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
# nodes = ["A", "B", "C", "D", "E", "F", "G", "H"]

# G.add_nodes_from(nodes)

G.add_edge("a", "b", weight=3.0)
G.add_edge("a", "e", weight=5.0)
G.add_edge("a", "h", weight=4.0)

G.add_edge("b", "c", weight=2.0)
G.add_edge("b", "e", weight=5.0)
G.add_edge("b", "f", weight=7.0)

G.add_edge("e", "h", weight=7.0)
G.add_edge("e", "f", weight=4.0)

G.add_edge("h", "f", weight=5.0)
G.add_edge("h", "i", weight=2.0)

G.add_edge("c", "d", weight=3.0)
G.add_edge("c", "f", weight=2.0)
G.add_edge("c", "g", weight=6.0)


################################
G.add_edge("d", "z", weight=2.0)
G.add_edge("d", "g", weight=7.0)
G.add_edge("g", "z", weight=6.0)
G.add_edge("g", "j", weight=4.0)
G.add_edge("g", "f", weight=4.0)

G.add_edge("i", "j", weight=6.0)
G.add_edge("i", "f", weight=4.0)
G.add_edge("j", "f", weight=3.0)
G.add_edge("j", "z", weight=5)
# G.add_edge("c", "d", weight=3.0)
# G.add_edge("c", "f", weight=2.0)
# G.add_edge("c", "g", weight=6.0)

print(nx.shortest_path_length(G,"a", "f",weight="weight"))


nx.draw_spring(G, with_labels=True)
plt.show()