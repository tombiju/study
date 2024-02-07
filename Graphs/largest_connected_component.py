def largest_component(adjacency_list: list) -> int:
    visited = set()
    largest_length = 0
    for node in adjacency_list:
        if node not in visited:
            current_length = dfs(adjacency_list, node, visited)
            if current_length > largest_length:
                largest_length = current_length
    return largest_length

def dfs(adjacency_list: list, node: str, visited: set) -> int:
    visited.add(node)
    length = 1
    for neighbor in adjacency_list[node]:
        if neighbor not in visited:
            length += dfs(adjacency_list, neighbor, visited)
    return length

if __name__ == "__main__":
    adjacency_list = {
        '0': ['8', '1', '5'],
        '1': ['0'],
        '5': ['0', '8'],
        '8': ['0', '5'],
        '2': ['3', '4'],
        '3': ['2', '4'],
        '4': ['3', '2']
    }
    assert largest_component(adjacency_list) == 4