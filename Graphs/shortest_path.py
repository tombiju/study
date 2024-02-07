def shortest_path(adjacency_list: list, start_node: str, target_node: str) -> int:
    queue = [(start_node, 0)]
    visited = set()
    while queue:
        current_node = queue.pop(0)
        visited.add(current_node)
        if current_node[0] == target_node:
            return current_node[1]
        unvisited_neighbors = []
        for neighbor in adjacency_list[current_node[0]]:
            if neighbor not in visited:
                unvisited_neighbors.append((neighbor, current_node[1] + 1))
        queue = queue + unvisited_neighbors
    return -1 # item doesn't exist or is not part of the connected graph of the start node

def edges_to_adjacency_list(edges: list) -> dict:
    adjacency_list = dict()
    for edge in edges:
        adjacency_list[edge[0]] = adjacency_list.setdefault(edge[0], []) + [edge[1]]
        adjacency_list[edge[1]] = adjacency_list.setdefault(edge[1], []) + [edge[0]]
    return adjacency_list

if __name__ == "__main__":
    edges = [
        ['w', 'x'],
        ['x', 'y'],
        ['z', 'y'],
        ['z', 'v'],
        ['w', 'v']
    ]
    adjacency_list = edges_to_adjacency_list(edges)
    assert shortest_path(adjacency_list, 'w', 'z') == 2
    assert shortest_path(adjacency_list, 'y', 'x') == 1