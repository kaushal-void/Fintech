INF = 999

network = [
    [0, 1, INF, 7],
    [1, 0, 1, INF],
    [INF, 1, 0, 2],
    [7, INF, 2, 0]
]

n = 4

dist = [row[:] for row in network]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

print("Final Routing Table:")
print("   N0 N1 N2 N3")

for i in range(n):
    row = " ".join(str(dist[i][j]) if dist[i][j] != 999 else "INF" for j in range(n))
    print(f"N{i} [ {row} ]")