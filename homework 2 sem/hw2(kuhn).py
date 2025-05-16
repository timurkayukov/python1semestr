def bip(graph):
    n = len(graph)
    color = [-1 for _ in range(n)]
    for start in range(n):
        if color[start] == -1:
            queue = [start]
            color[start] = 0
            while queue:
                u = queue.pop(0)
                for v in graph[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return False, []
    left = [i for i in range(n) if color[i] == 0]
    right = [i for i in range(n) if color[i] == 1]
    return True, (left, right)


def kuhn(graph, left_part):
    n = len(graph)
    match_to = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    def dfs(u):
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                if match_to[v] == -1 or dfs(match_to[v]):
                    match_to[v] = u
                    return True
        return False
    max_matching = 0
    for u in left_part:
        visited = [False for _ in range(n)]
        if dfs(u):
            max_matching += 1
    return match_to

def min_vertex_cover(graph):
    is_bip, parts = bip(graph)
    if not is_bip:
        return []
    left, right = parts
    match = kuhn(graph, left)
    dir_gr= {u: [] for u in range(len(graph))}
    f_right = []
    for v in right:
        if match[v] != -1:
            dir_gr[match[v]].append(v)
            for u in graph[v]:
                if u != match[v]:
                    dir_gr[v].append(u)
        else:
            f_right.append(v)
    visited = [False for _ in range(len(graph))]
    def dfs(u, is_left):
        if visited[u]:
            return
        visited[u] = True
        if is_left:
            for v in dir_gr[u]:
                dfs(v, False)
        else:
            for v in dir_gr[u]:
                dfs(v, True)
    for v in f_right:
        dfs(v, False)
    mvc = []
    for u in left:
        if not visited[u]:
            mvc.append(u)
    for v in right:
        if visited[v]:
            mvc.append(v)

    return mvc
