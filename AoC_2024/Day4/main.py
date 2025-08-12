
from collections import defaultdict
import pathlib

file_path = pathlib.Path(__file__).parent.resolve().joinpath("input.txt")
def part_1(r, c, grid):
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
    word = "XMAS"
    count = 0
    for dir in dirs:
        match_idx = 0
        for idx in range(len(word)):
            x = r + idx * dir[0]
            y = c + idx * dir[1]
            if ((0 <= x < len(grid)) and (0 <= y < len(grid[0]))) and (
                grid[x][y] == word[idx]
            ):
                match_idx += 1
        if match_idx == len(word):
            count += 1
    return count

def part_2(r,c, grid):
    dirs = [ [-1, -1], [-1, 1],[1, -1], [1, 1]]
    m = defaultdict(int)
    for dir in dirs:
        x = r + dir[0]
        y = c + dir[1]
        if ((0 <= x < len(grid)) and (0 <= y < len(grid[0]))):
            m[grid[x][y]] += 1
        else: return 0
    if (m['S'] == 2 and m['M'] == 2) and (grid[r-1][c-1] != grid[r+1][c+1]):
        return 1
    return 0


# Read the input file
with open(file_path, "r", encoding="utf-8") as file:
    grid = [line.strip() for line in file.readlines()]
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            # count += part_1(r, c, grid)
            if (grid[r][c] == 'A'):
                count += part_2(r,c,grid)
    print(count)
