num_vertex = 7
edges = [(0,1), (0,2), (0,6), (0,5), (5,3), (4,3), (5,4), (6,4)]

undirected = [[0 for i in range(num_vertex)] for j in range(num_vertex)]
directed = [[0 for i in range(num_vertex)] for j in range(num_vertex)]

for s, e in edges:
    undirected[s][e] = 1
    undirected[e][s] = 1

for s, e in edges:
    directed[s][e] = 1

print('Undirected Graph')
for _ in range(num_vertex):
    print(undirected[_])
print('Directed Graph')
for _ in range(num_vertex):
    print(directed[_])
