def hasPathDFS(adjacency_list: list, current_node: str, target_node: str) -> bool:
    if current_node == target_node:
        return True
    for neighbor in adjacency_list[current_node]:
        if hasPathDFS(adjacency_list, neighbor, target_node): # this if statement return is necessary to bubble up the truthy value to the top level call
            return True
    return False

def hasPathBFS(adjacency_list:list, start_node: str, target_node: str) -> bool:
    queue = [start_node]
    while queue:
        current_node = queue.pop(0)
        if current_node == target_node:
            return True
        queue = queue + adjacency_list[current_node]
    return False
        
if __name__ == "__main__":
    adjacency_list = {
        'f': ['g', 'i'],
        'g': ['h'],
        'h': [],
        'i': ['g', 'k'],
        'j': ['i'],
        'k': []
    }
    assert hasPathDFS(adjacency_list, 'i', 'h') == True
    assert hasPathBFS(adjacency_list, 'f', 'j') == False
    assert hasPathBFS(adjacency_list, 'i', 'h') == True
    assert hasPathBFS(adjacency_list, 'f', 'j') == False