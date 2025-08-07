import re

filepath = "AoC_2024\\Day3\\input.txt"
with open(filepath, "r", encoding="utf-8") as file:
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|don't\(\)|do\(\)")
    matches = list(pattern.finditer(file.read()))
    isActive = True
    ans = 0
    for match in matches:
        if "do()" in match.group(0):
            isActive = True
        elif "don't()" in match.group(0):
            isActive = False
        else:
            if isActive:
                print(match.group(0))
                ans += int(match.group(1)) * int(match.group(2))
    print(ans)
