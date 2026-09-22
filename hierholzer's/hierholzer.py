import sys

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])

    adj = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)

    idx = 2
    for i in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        adj[u].append((v, i))
        adj[v].append((u, i))
        degree[u] += 1
        degree[v] += 1

    # 1. Degree check
    for i in range(1, n + 1):
        if degree[i] % 2 != 0:
            print("IMPOSSIBLE")
            return

    # 2. Hierholzer's Algorithm
    visited_edge = [False] * m
    circuit = []
    st = [1]

    while st:
        u = st[-1]

        while adj[u] and visited_edge[adj[u][-1][1]]:
            adj[u].pop()

        if adj[u]:
            v, edge_id = adj[u].pop()
            visited_edge[edge_id] = True
            st.append(v)
        else:
            circuit.append(u)
            st.pop()

    # 3. Disconnected component check
    if len(circuit) != m + 1:
        print("IMPOSSIBLE")
        return

    # Circuit is in reverse, output reversed
    print(*(circuit[::-1]))

if __name__ == "__main__":
    main()
