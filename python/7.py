from collections import deque
def bfs_of_graph(V, adj):
    ans = []
    vis = [0] * V
    q = deque([0])
    while q:
        curr = q.popleft()
        if vis[curr] == 0:
            vis[curr] = 1
            ans.append(curr)
            for i in adj[curr]:
                if vis[i] == 0:
                    q.append(i)
    return ans
V = 5  
edges = [(0, 1), (0, 4), (1, 2), (1, 3), (2, 4)]  
adj = [[] for _ in range(V)]
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)
result = bfs_of_graph(V, adj)
print("BFS Traversal:", result)