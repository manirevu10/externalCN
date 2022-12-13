def min_search(dist, visited):
    min = 1e7
    min_index = 0
    for i in range(len(dist)):
        if dist[i] < min and visited[i] == False:
            min = dist[i]
            min_index = i 
    return min_index


V = int(input("Enter no vertexes: "))
graph = []

for i in range(V):
    graph.append(list(map(int,input().split())))

src = int(input())

dist = [1e7] * V
visited = [False] * V
dist[src] = 0

path = [0] * V

for v in range(V):
    if graph[src][v] > 0:
        path[v] = src

for i in range(V):

    u = min_search(dist, visited)
    visited[u] = True

    for v in range(V):
        if(graph[u][v] > 0 and visited[v] == False and dist[u] + graph[u][v] < dist[v]):
            dist[v] = graph[u][v] + dist[u]
            path[v] = u
    


for v in range(V):
    if v == src:
        continue
    print(v, '->', dist[v], end = " path - ")
    
    u = v 
    print(v,end='')
    while u != src:
        print('->',path[u], end= "",sep="")
        u = path[u]
    print()
