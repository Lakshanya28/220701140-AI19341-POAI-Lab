import heapq

def a_star_search(graph, start, goal):
    # Priority queue
    open_set = []
    heapq.heappush(open_set, (0, start))  # (priority, node)
    
    # Tracking the shortest path
    came_from = {}
    
    # Costs
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic(start, goal)
    
    while open_set:
        # Get node with the lowest f_score
        _, current = heapq.heappop(open_set)
        
        if current == goal:
            return reconstruct_path(came_from, current)
        
        for neighbor, cost in graph[current]:
            tentative_g_score = g_score[current] + cost
            
            if tentative_g_score < g_score[neighbor]:
                # Update the best path to the neighbor
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                
                # Push neighbor to the open set if not already there
                if neighbor not in [i[1] for i in open_set]:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None  # No path found

def heuristic(node, goal):
    # Simple heuristic: Manhattan distance (for grid-based graphs)
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

# Example graph (grid-based with nodes and costs)
graph = {
    (0, 0): [((0, 1), 1), ((1, 0), 1)],
    (0, 1): [((0, 0), 1), ((1, 1), 1)],
    (1, 0): [((0, 0), 1), ((1, 1), 1)],
    (1, 1): [((1, 0), 1), ((0, 1), 1)],
}

start = (0, 0)
goal = (1, 1)

path = a_star_search(graph, start, goal)
print("Shortest path:", path)
