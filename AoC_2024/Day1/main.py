from collections import defaultdict
import pathlib

file_path = pathlib.Path(__file__).parent.resolve().joinpath("input.txt")
def input():
    
    with open(file_path, "r", encoding="utf-8") as file:
        data = file.readlines()
        for line in data:
            a, b = map(int, line.strip().split())
            left.append(a)
            right.append(b)


left = []
right = []
input()

# part 1
# left.sort()
# right.sort()
# ans = 0
# for i in range(len(left)):
#     ans += abs(left[i] - right[i])
# print(ans)

# part 2
ans = 0
m = defaultdict(int)
for k in right:
    m[k] += 1
for l in left:
    ans += l * m[l]
print(ans)
