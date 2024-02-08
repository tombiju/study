def count_islands(grid: list) -> int:
    visited = set()
    island_count = 0
    for row, _ in enumerate(grid):
        for column, space in enumerate(grid[row]):
            if space == "L" and (row, column) not in visited:
                island_count += 1
                dfs(row, column, grid, visited)
    return island_count

def dfs(row:int, column:int, grid: list, visited: set) -> None:
    if row < 0 or row >= len(grid) or column < 0 or column >= len(grid[0]):
        return
    if grid[row][column] == "L" and (row, column) not in visited:
        visited.add((row, column))
        dfs(row - 1, column, grid, visited)
        dfs(row, column + 1, grid, visited)
        dfs(row + 1, column, grid, visited)
        dfs(row, column - 1, grid, visited)
            


if __name__ == "__main__": 
    grid = [
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'W'],
        ['W', 'W', 'L', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['L', 'L', 'W', 'W', 'W'],
    ]
    assert count_islands(grid) == 3
    grid = [
        ['L', 'W', 'W', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['W', 'L', 'W', 'L', 'W'],
        ['W', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'L', 'L', 'L'],
    ]
    assert count_islands(grid) == 4
    grid = [
        ['L', 'L', 'L'],
        ['L', 'L', 'L'],
        ['L', 'L', 'L'],
    ]
    assert count_islands(grid) == 1
    grid = [
        ['W', 'W'],
        ['W', 'W'],
        ['W', 'W'],
    ]
    assert not count_islands(grid)