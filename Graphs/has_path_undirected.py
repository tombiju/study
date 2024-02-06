def edges_to_adjacency_list(edges: list) -> dict:
    adjacency_list = dict()
    for edge in edges:
        adjacency_list[edge[0]] = adjacency_list.setdefault(edge[0], []) + [edge[1]]
        adjacency_list[edge[1]] = adjacency_list.setdefault(edge[1], []) + [edge[0]]
    return adjacency_list

def has_path_undirected(adjacency_list: list, current_node: str, target_node: str, visited: set) -> bool:
    if current_node == target_node:
        return True
    visited.add(current_node)
    for neighbor in adjacency_list[current_node]:
        if neighbor not in visited and has_path_undirected(adjacency_list, neighbor, target_node, visited):
            return True
    return False

if __name__ == "__main__":
    edges = [
        ['i', 'j'],
        ['k', 'i'],
        ['m', 'k'],
        ['k', 'l'],
        ['o', 'n']
    ]
    adjacency_list = edges_to_adjacency_list(edges)
    assert adjacency_list == {'i': ['j', 'k'], 'j': ['i'], 'k': ['i', 'm', 'l'], 'm': ['k'], 'l': ['k'], 'o': ['n'], 'n': ['o']}
    assert has_path_undirected(adjacency_list, 'm', 'j', set())
    assert not has_path_undirected(adjacency_list, 'k', 'o', set())
