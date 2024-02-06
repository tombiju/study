def dfs_iterative(adjacency_list: list, start_node: str) -> list:
    stack = [start_node] # a stack is suitable to keep track of traversal since each direction should be explored as deep as possible
    output = []
    while stack:
        current_node = stack.pop()
        output.append(current_node)
        stack = stack + adjacency_list[current_node]
    return output

def dfs_recursive_without_loop(adjacency_list: list, stack: list, output: list) -> list:
    if stack:
        current_node = stack.pop()
        output.append(current_node)
        stack = stack + adjacency_list[current_node]
        dfs_recursive_without_loop(adjacency_list, stack, output)
    return output

def dfs_recursive_with_loop(adjacency_list: list, current_node: str, output: list) -> list: # this version of the recursive approach uses the call stack as the stack
    output.append(current_node)
    for neighbor in adjacency_list[current_node]:
        dfs_recursive_with_loop(adjacency_list, neighbor, output)
    return output
    

if __name__ == "__main__":
    adjacency_list = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': [],
        'f': [],
    }
    iterative_output = dfs_iterative(adjacency_list, 'a')
    assert iterative_output == ['a', 'c', 'e', 'b', 'd', 'f']
    assert iterative_output == dfs_recursive_without_loop(adjacency_list, ['a'], [])
    assert dfs_recursive_with_loop(adjacency_list, 'a', []) == ['a', 'b', 'd', 'f', 'c', 'e']