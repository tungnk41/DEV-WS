import pathlib
from itertools import permutations
import pprint
from collections import defaultdict

# Read the input file
block_1 = []
block_2 = []
m = defaultdict(list)


def init():
    global block_1, block_2, m
    file_path = pathlib.Path(__file__).parent.resolve().joinpath("input.txt")
    with open(file_path, "r", encoding="utf-8") as file:
        data = [line for line in file.read().split("\n") if line.strip()]
        block_1 = [
            list(map(int, sublist))
            for sublist in (line.strip().split("|") for line in data if "|" in line)
        ]
        block_2 = [
            list(map(int, sublist))
            for sublist in (line.strip().split(",") for line in data if "," in line)
        ]
        for item in block_1:
            if item[0] not in m:
                m[item[0]] = []
            if item[1] not in m:
                m[item[1]] = []
            m[item[0]].append(item[1])
        # for k, v in m.items():
        #     print(k)
        #     print(v)
        # print(block_1)
        # print(block_2)


def verify(lst):
    prev = None
    isBreak = False
    for element in lst:
        current = element if element in m else None
        if current == None:
            isBreak = True
            break
        if prev == None:  # first index
            prev = current
        else:
            if current in m[prev]:
                prev = current
            else:
                isBreak = True
    return not isBreak


def part_1():
    list_ans = []
    for lst in block_2:
        if verify(lst):
            list_ans.append(lst)
    ans = 0
    for lst in list_ans:
        idx_med = len(lst) // 2
        ans += lst[idx_med]
    print(ans)


def part_2():
    list_ans = []
    for l in block_2:
        if not verify(l):
            for per in permutations(l):
                if verify(per):
                    list_ans.append(per)
                    break
    print(list_ans)
    ans = 0
    for lst in list_ans:
        idx_med = len(lst) // 2
        ans += lst[idx_med]
    print(ans)


init()
# part_1()
part_2()
