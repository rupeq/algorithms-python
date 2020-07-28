from collections import deque, defaultdict

graph = {
          'A': ['C', 'D'],
          'B': ['C', 'E'],
          'C': ['A', 'B', 'E'],
          'D': ['A'], 
          'E': ['B', 'C'],
          }

# graph
# a - c - b
# |   \   /
# d     e

start = 'A'
path = []
visited = defaultdict(bool)

def bfs(m, start, visited, path):
    queue = deque()
    path.append(start)
    queue.append(start)
    visited[start] = True
    while len(queue) != 0:
        tmpnode = queue.popleft() 
        for neighbour in m[tmpnode]:
            if visited[neighbour] == False:
                path.append(neighbour)
                queue.append(neighbour)
                visited[neighbour] = True
    return path

print(bfs(graph, start, visited, path))

# another with input

# graph = defaultdict(list)
# vertex, edges = map(int, input().split())
# for i in range(edges):
#     u, v = map(str, input().split())
#     graph[u].append(v)
#     graph[v].append(u)

# input example
# input: 5 5 | A C | A D | B C | B E | C E
