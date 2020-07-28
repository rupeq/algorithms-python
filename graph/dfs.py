from collections import defaultdict

def dfs(m, start, visited, path):
    path.append(start)
    visited[start] = True
    for neighbour in m[start]:
        if visited[neighbour] == False:
            dfs(m, neighbour, visited, path)
    return path

if __name__ == "__main__":
    start = 'A'
    path = []
    visited = defaultdict(bool)

    graph = {
          'A': ['C', 'D'],
          'B': ['C', 'E'],
          'C': ['A', 'B', 'E'],
          'D': ['A'],
          'E': ['B', 'C'],
            }

    print(dfs(graph, start, visited, path))
