import networkx as nx
import matplotlib.pyplot as plt

name = 'cities.csv'


def function_of_opening(a):
    with open(a, mode='r') as file:
        list_of_cities = []
        for f in file:
            line = f[:-1].split(';')
            line[2] = int(line[2])
            list_of_cities.append(line)
        return list_of_cities


result = function_of_opening(name)

g = nx.Graph()
for edge in result:
    g.add_edge(edge[0], edge[1], weight=edge[2])


pos = nx.spring_layout(g)
nx.draw_networkx(g, pos)
plt.title("Graph of Ukraine")
plt.show()
