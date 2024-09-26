def dfs(ans, vis, node, adj):
    vis[node] = True
    ans.append(node)

    for neighbor in adj[node]:
        if not vis[neighbor]:
            dfs(ans, vis, neighbor, adj)

def dfs_of_graph(v, adj):
    ans = []
    vis = [False] * v

    for i in range(v):
        if not vis[i]:
            dfs(ans, vis, i, adj)

    return ans
v = 5  
edges = [(0, 1), (0, 2), (1, 3), (1, 4)]

adj = [[] for _ in range(v)]

for u, w in edges:
    adj[u].append(w)
    adj[w].append(u)

dfs_result = dfs_of_graph(len(adj), adj)
print("DFS traversal:", dfs_result)