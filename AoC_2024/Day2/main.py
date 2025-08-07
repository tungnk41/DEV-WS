from collections import defaultdict


# part 1
filepath = "AoC_2024\\Day2\\input.txt"
data = [[]]
ans = 0
with open(filepath, "r", encoding="utf-8") as file:
    data = [list(map(int, line.strip().split())) for line in file]


def isSafe(line: list[int]):
    isIncreasing = False
    isDecreasing = False
    isBreak = False
    for i in range(len(line) - 1):
        if line[i] < line[i + 1]:
            isIncreasing = True
            if not (1 <= (line[i + 1] - line[i]) <= 3) or isDecreasing:
                isBreak = True
                break
        elif line[i] > line[i + 1]:
            isDecreasing = True
            if not (1 <= (line[i] - line[i + 1]) <= 3) or isIncreasing:
                isBreak = True
                break
        else:
            isBreak = True
    return not isBreak


for line in data:
    if isSafe(line):
        ans += 1
    else:
        for i in range(len(line) - 1):

            if isSafe(line[:i] + line[i + 1 :]):
                ans += 1
                break

print(ans)
