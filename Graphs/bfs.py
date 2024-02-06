def bfs(adjacency_list: list, start_node: str) -> list:
    output = []
    queue = [start_node]
    while queue:
        current_node = queue.pop(0)
        output.append(current_node)
        queue =  queue + adjacency_list[current_node]
    return output

# BFS should not use recursion since the call stack goes against the queue logic that a BFS needs to work properly
if __name__ == "__main__":
    adjacency_list = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': [],
        'f': [],
    }

assert bfs(adjacency_list, 'a') == ['a', 'b', 'c', 'd', 'e', 'f']