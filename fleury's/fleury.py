from collections import defaultdict

def solve():
    print("Enter number of crossings (n) and streets (m):")
    n, m = map(int, input().split())

    adj = defaultdict(list)   # adj[u] = list of (neighbor, edge_id)
    degree = [0] * (n + 1)

    print(f"Enter {m} streets, one per line, as: a b")
    for eid in range(m):
        a, b = map(int, input().split())
        adj[a].append((b, eid))
        adj[b].append((a, eid))
        degree[a] += 1
        degree[b] += 1

    used_edge = [False] * m

    # eulerian circuit existence check
    for v in range(1, n + 1):
        if degree[v] % 2 != 0:
            print("IMPOSSIBLE")
            return

    start = 1
    if degree[start] == 0:
        if m == 0:
            print(1)
        else:
            print("IMPOSSIBLE")
        return

    visited = [False] * (n + 1)
    stack = [start]
    visited[start] = True
    while stack:
        u = stack.pop()
        for v, _ in adj[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)

    for v in range(1, n + 1):
        if degree[v] > 0 and not visited[v]:
            print("IMPOSSIBLE")
            return

    #helper functions for Fleury's algorithm
    def count_reachable(u, skip_edge):
        vis = [False] * (n + 1)
        stack = [u]
        vis[u] = True
        cnt = 0
        while stack:
            x = stack.pop()
            cnt += 1
            for y, eid in adj[x]:
                if eid == skip_edge or used_edge[eid]:
                    continue
                if not vis[y]:
                    vis[y] = True
                    stack.append(y)
        return cnt

    def is_bridge(u, eid):
        before = count_reachable(u, -1)
        after = count_reachable(u, eid)
        return after < before

    #fleury's algorithm main loop
    circuit = [start]
    current = start

    while True:
        remaining = [(v, eid) for v, eid in adj[current] if not used_edge[eid]]
        if not remaining:
            break

        if len(remaining) == 1:
            next_v, eid = remaining[0]
        else:
            next_v, eid = None, None
            for v, e in remaining:
                if not is_bridge(current, e):
                    next_v, eid = v, e
                    break
            if next_v is None:
                next_v, eid = remaining[0]

        used_edge[eid] = True
        circuit.append(next_v)
        current = next_v

    print("Route:")
    if len(circuit) == m + 1:
        print(' '.join(map(str, circuit)))
    else:
        print("IMPOSSIBLE")

solve()
