INF = float('inf')

matrix = [[0, INF, 3, 1, INF],
          [INF, 0, 4, INF, 2],
          [3, 4, 0, INF, 2],
          [1, INF, INF, 0, INF],
          [INF, 2, 2, INF, 0]]

length = len(matrix)

def FloydWarchall(m, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if m[i][k] + m[k][j] < m[i][j]:
                    m[i][j] = m[i][k] + m[k][j]
    return m

print(FloydWarchall(matrix, length))
