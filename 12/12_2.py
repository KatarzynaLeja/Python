import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

for node in range(1, 9):
    G.add_node(node)
for (a, b) in ((1, 2), (1, 3), (1, 5), (1, 7), (2, 4), (2, 6), (3, 5), (3, 6), (3, 8), (4, 8)):
    G.add_edge(a, b)

G.nodes(data=True)
list(G.nodes.data())

G.edges(data=True)
list(G.edges.data())

nx.draw(G, with_labels=True, node_size=400, node_shape='8', node_color='#42cbed',
        edge_color='#706f6f', style='dotted')

plt.show()
plt.savefig('graph.png')
