inf = 10000000

matrix = [[inf,inf, 3, 1, inf], # v0
          [inf, inf, 4, inf, 2], # v1
          [3, 4, inf, inf, 2], # v2
          [1, inf, inf, inf, inf], # v3
          [inf, 2, 2, inf, inf]] # v4
        
vertex = int(input('Введите стартовую вершину: '))
size = len(matrix)

def dijkstra(graph, v, n):
    d, used = [], [False] * n
    [d.append(graph[v][i]) for i in range(n)]
    d[v], u = 0, 1
    for i in range(n):
        dmin, maxint = 1000001, 1000001
        for j in range(n):
          if (not used[j]) and (d[j] < dmin):
            dmin = d[j]
            nom = j
      u =   nom
      used[u] = True
      for j in range(n):
          if (not used[j]) and (graph[u][j] != maxint) and (d[u] + graph[u][j] < d[j]):
              d[j] = d[u] + graph[u][j] 
    return d

print(dijkstra(matrix, vertex, size))