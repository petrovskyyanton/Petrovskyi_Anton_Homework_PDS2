import networkx as nx
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


def shortest_path_between_two_cities(g, city_1, city_2):
    return f"The shortest path between {city_1} and {city_2}:\n" \
           f"{nx.shortest_path(g, city_1, city_2, weight='weight')}\n" \
           f"The lenght between {city_1} and {city_2}:\n" \
           f"{nx.shortest_path_length(g, city_1, city_2, weight='weight')}"


print(shortest_path_between_two_cities(g, 'Zavodske', 'Kovel'))


