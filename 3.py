import networkx as nx
import matplotlib.pyplot as plt
from itertools import chain


def CM(ds, create_using):
    n = len(ds)
    G = nx.empty_graph(n, create_using)

    if n == 0:
        return G

    s = list(chain.from_iterable([n] * d for n, d in enumerate(ds)))

    n = len(s)
    m = n // 2
    sa, sb = s[:m], s[m:]
    G.add_edges_from(zip(sa, sb))
    return G


def configuration_model(ds, create_using=None, seed=None):
    G = nx.empty_graph(14, create_using, default=nx.MultiGraph)
    G = CM(ds, G)

    return G


k = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3]

g = configuration_model(k, create_using=None, seed=None)
print(g)
g1 = nx.draw(g, with_labels=False, node_size=15, width=0.2, node_color='blue')
plt.show()