def bellmanFord(graph, start):
    upper = {node: float('inf') for node in graph}
    upper[start] = 0

    for i in range(len(graph)):
        updated = False
        for here in graph:
            for there, cost in graph[here].items():
                if upper[there] > upper[here] + cost:
                    upper[there] = upper[here] + cost
                    updated = True
        if updated == False: break

    if updated == True:
        upper = None
        
    return upper


graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

print(bellmanFord(graph, 'A'))