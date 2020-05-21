num_vertex = 7
edges = [(0,1), (0,2), (0,6), (0,5), (5,3), (4,3), (5,4), (6,4)]

undirected = dict()
directed = dict()

for s, e in edges:
    if undirected.get(s):
        undirected.get(s).append(e)
    else:
        undirected[s] = [e]
    if undirected.get(e):
        undirected.get(e).append(s)
    else:
        undirected[e] = [s]

for s, e in edges:
    if directed.get(s):
        directed.get(s).append(e)
    else:
        directed[s] = [e]

print('Undirected Graph')
for key in undirected:
    print(key, undirected.get(key))
print('Directed Graph')
for key in directed:
    print(key, directed.get(key))