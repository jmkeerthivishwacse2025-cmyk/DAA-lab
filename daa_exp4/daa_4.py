import heapq


def dijkstra(graph, source):
    """
    Dijkstra's Algorithm using Min-Heap
    Time: O((V + E) log V), Space: O(V)
    graph: dict {u: [(v, weight), ...]}, 0-indexed
    """
    n = len(graph)
    dist = [float('inf')] * n
    prev = [None] * n
    dist[source] = 0

    pq = [(0, source)]  # (distance, vertex)
    visited = set()

    while pq:
        d, u = heapq.heappop(pq)

        if u in visited:
            continue

        visited.add(u)

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))

    return dist, prev


def reconstruct_path(prev, source, target):
    path = []
    node = target

    while node is not None:
        path.append(node)
        node = prev[node]

    path.reverse()

    if path[0] == source:
        return path

    return []


# ---------- Additional Function ----------
def display_graph(graph):
    print("\nGraph Representation")
    print("-" * 35)
    for vertex in graph:
        print(f"{vertex} -> {graph[vertex]}")
    print("-" * 35)


# ---------- Additional Function ----------
def graph_statistics(graph):
    vertices = len(graph)
    edges = sum(len(neighbours) for neighbours in graph.values())

    print("\nGraph Statistics")
    print("-" * 20)
    print("Number of Vertices :", vertices)
    print("Number of Edges    :", edges)
    print("-" * 20)


# ---------- Additional Function ----------
def print_predecessor_table(prev):
    print("\nPredecessor Table")
    print("-" * 25)
    print(f'{"Vertex":>8} {"Previous":>10}')
    print("-" * 25)

    for i in range(len(prev)):
        print(f'{i:>8} {str(prev[i]):>10}')


# --- Graph Definition (Adjacency List) ---
graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: [(4, 3)],
    4: [(5, 2)],
    5: []
}

display_graph(graph)
graph_statistics(graph)

source = 0
dist, prev = dijkstra(graph, source)

print(f'\nShortest paths from vertex {source}:')
print(f'{"Vertex":>8} {"Distance":>10} {"Path":>30}')
print('-' * 55)

for v in range(len(graph)):
    path = reconstruct_path(prev, source, v)
    path_str = ' -> '.join(map(str, path)) if path else 'No path'
    d = dist[v] if dist[v] != float('inf') else 'INF'
    print(f'{v:>8} {str(d):>10} {path_str:>30}')

print_predecessor_table(prev)

# ---------- Additional Summary ----------
reachable = sum(1 for d in dist if d != float('inf'))

print("\nSummary")
print("-" * 20)
print("Source Vertex :", source)
print("Reachable Vertices :", reachable)
print("Algorithm Completed Successfully")
print("-" * 20)