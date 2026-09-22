import sys

# Increase recursion depth just in case for backtracking search on deeper paths
sys.setrecursionlimit(2000)

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

    # 2. Naive / Backtracking Search Algorithm
    visited_edge = [False] * m
    path = [1]

    def backtrack(u, edges_left):
        # Base case: if all edges are visited, check if we successfully returned to start node 1
        if edges_left == 0:
            return u == 1

        # Try exploring available unused edges from current node u
        for v, edge_id in adj[u]:
            if not visited_edge[edge_id]:
                visited_edge[edge_id] = True
                path.append(v)

                # Recursively search down this branch
                if backtrack(v, edges_left - 1):
                    return True

                # Backtrack: undo the choice if it didn't lead to a valid full circuit
                path.pop()
                visited_edge[edge_id] = False

        return False

    success = backtrack(1, m)

    # 3. Completion check
    if not success:
        print("IMPOSSIBLE")
        return

    # Output the final Eulerian circuit path
    print(*path)

if __name__ == "__main__":
    main()
