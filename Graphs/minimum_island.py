def find_minimum_island(grid: list) -> int:
    visited = set()
    minimum_island_size = None
    for row, _ in enumerate(grid):
        for column, space in enumerate(grid[row]):
            if space == "L" and (row, column) not in visited:
                island_size = dfs(row, column, grid, visited)
                if not minimum_island_size or island_size < minimum_island_size:
                    minimum_island_size = island_size
    return minimum_island_size or 0

def dfs(row:int, column:int, grid: list, visited: set) -> int:
    if row < 0 or row >= len(grid) or column < 0 or column >= len(grid[0]):
        return 0
    if grid[row][column] == "L" and (row, column) not in visited:
        island_size = 1
        visited.add((row, column))
        island_size += dfs(row - 1, column, grid, visited)
        island_size += dfs(row, column + 1, grid, visited)
        island_size += dfs(row + 1, column, grid, visited)
        island_size += dfs(row, column - 1, grid, visited)
        return island_size
    return 0

if __name__ == "__main__":
    grid = [
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'W'],
        ['W', 'W', 'L', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['L', 'L', 'W', 'W', 'W'],
    ]
    assert find_minimum_island(grid) == 2
    grid = [
        ['L', 'W', 'W', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['W', 'L', 'W', 'L', 'W'],
        ['W', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'L', 'L', 'L'],
    ]
    assert find_minimum_island(grid) == 1
    grid = [
        ['L', 'L', 'L'],
        ['L', 'L', 'L'],
        ['L', 'L', 'L'],
    ]
    assert find_minimum_island(grid) == 9
    grid = [
        ['W', 'W', 'W'],
        ['W', 'W', 'W'],
        ['W', 'W', 'W'],
    ]
    assert not find_minimum_island(grid)
    grid = [
        ['W', 'W'],
        ['L', 'L'],
        ['W', 'W'],
        ['W', 'L']
    ]
    assert find_minimum_island(grid) == 1