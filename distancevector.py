alpha = "ABCDEFGHIJKLMLOPQRSTUVWXYZ-"
V = int(input())
graph = []

for i in range(V):
    graph.append(list(map(int,input().split())))

dist = [[ 1e7 for i in range(V)] for i in range(V)]
path = [[0 for i in range(V)] for i in range(V)]
for v in range(V):
    for u in range(V):
        if graph[v][u] or v == u:
            dist[v][u] = graph[v][u]
            if v == u:
                path[v][u] = 26
            else:
                path[v][u] = u



for v in range(V):
    for u in range(V):
        if graph[v][u]:
            for i in range(V):
                if dist[v][u] + dist[u][i] < dist[v][i]:
                    dist[v][i] = dist[v][u] + dist[u][i]
                    path[v][i] = u
print("    ",end = "")
for i in range(V):
    print(alpha[i],end = "   ")
print()
for i in range(V):
    print(alpha[i], end = "   ")
    for j in range(V):
        print(dist[j][i], alpha[path[j][i]], end = "  ")
    print()
