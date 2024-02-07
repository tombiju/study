def connected_components_count(adjacency_list:list) -> int:
    visited = set()
    count = 0
    for node in adjacency_list:
        if node not in visited:
            count += 1
            dfs(adjacency_list, node, visited)
    return count


def dfs(adjacency_list:list, current_node: str, visited: set) -> None:
    for neighbor in adjacency_list[current_node]:
        if neighbor not in visited:
            visited.add(neighbor)
            dfs(adjacency_list, neighbor, visited)
    
    
if __name__ == "__main__":
    adjacency_list = {
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2]
    }
    assert connected_components_count(adjacency_list) == 2
    adjacency_list = {
        1: [2],
        2: [1,8],
        6: [7],
        9: [8],
        7: [6, 8],
        8: [9, 7, 2]    
    }
    assert connected_components_count(adjacency_list) == 1
    adjacency_list = {
        3: [],
        4: [6],
        6: [4, 5, 7, 8],
        8: [6],
        7: [6],
        5: [6],
        1: [2],
        2: [1]
    }
    assert connected_components_count(adjacency_list) == 3
    adjacency_list = {}
    assert not connected_components_count(adjacency_list)
    adjacency_list = {
        0: [4,7],
        1: [],
        2: [],
        3: [6],
        4: [0],
        6: [3],
        7: [0],
        8: []
    }
    assert connected_components_count(adjacency_list) == 5