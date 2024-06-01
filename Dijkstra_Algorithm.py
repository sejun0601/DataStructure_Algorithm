import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    priorityQ = []
    heapq.heappush(priorityQ,[0, start])

    while priorityQ:
        cost ,curnode = heapq.heappop(priorityQ)
        
        if dist[curnode] < cost:
            continue

        for nextnode, nextweight in graph[curnode].items():
            
            nextcost = cost + nextweight

            if nextcost < dist[nextnode]:
                dist[nextnode] = nextcost
                heapq.heappush(priorityQ, [nextcost, nextnode])
    return dist 





graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

graph2 = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

print(dijkstra(graph2, 'A'))



def dijkstra2(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    visited = {node:False for node in graph}

    while True:
        closest = float('inf')
        for node in dist:
            if dist[node] <closest and visited[node] == False:
                curnode = node
                closest = dist[node]

        if closest == float('inf'): 
            break

        visited[curnode] = True

        for nextnode, nextweight in graph[curnode].items():
            nextcost = closest + nextweight
            if visited[nextnode] == True: continue
            if nextcost < dist[nextnode]:
                dist[nextnode] = nextcost

    return dist 

print(dijkstra2(graph2, 'A'))