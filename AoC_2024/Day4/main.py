def count_xmas_occurrences(grid):
    rows = len(grid)
    if rows == 0:
        return 0
    cols = len(grid[0])

    directions = [
        (0, 1),  # Right
        (0, -1),  # Left
        (1, 0),  # Down
        (-1, 0),  # Up
        (1, 1),  # Down-Right
        (1, -1),  # Down-Left
        (-1, 1),  # Up-Right
        (-1, -1),  # Up-Left
    ]

    count = 0

    for i in range(rows):
        for j in range(cols):
            for di, dj in directions:
                i3 = i + 3 * di
                j3 = j + 3 * dj
                if 0 <= i3 < rows and 0 <= j3 < cols:
                    # Check for "XMAS"
                    if (
                        grid[i][j] == "X"
                        and grid[i + di][j + dj] == "M"
                        and grid[i + 2 * di][j + 2 * dj] == "A"
                        and grid[i + 3 * di][j + 3 * dj] == "S"
                    ):
                        count += 1
    return count


# Read the input file
filepath = "AoC_2024\\Day4\\input.txt"
with open(filepath, "r", encoding="utf-8") as file:
    grid = [line.strip() for line in file.readlines()]

print(count_xmas_occurrences(grid))
