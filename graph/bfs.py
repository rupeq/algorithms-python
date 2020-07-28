from collections import deque, defaultdict

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

    print(bfs(graph, start, visited, path))