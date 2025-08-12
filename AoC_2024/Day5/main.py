import pathlib


class Node:
    def __init__(self, idx):
        self.idx = idx
        self.next = []

    def __str__(self):
        return str(self.idx)


# Read the input file
block_1 = []
block_2 = []
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
    # print(block_1)
    # print(block_2)


def part_1():
    m = {}
    for list in block_1:
        if list[0] not in m:
            m[list[0]] = Node(list[0])
        if list[1] not in m:
            m[list[1]] = Node(list[1])
        m[list[0]].next.append(m[list[1]])

    list_ans = []
    for list in block_2:
        node = None
        isBreak = False
        for idx, element in enumerate(list):
            current = m[element] if element in m else None
            if current == None:
                isBreak = True
                break
            if node == None:  # first index
                node = current
            else:
                if current in node.next:
                    node = current
                else:
                    isBreak = True
                    break
        if not isBreak:
            list_ans.append(list)
    ans = 0
    for list in list_ans:
        idx_med = len(list) // 2
        ans += list[idx_med]
    print(ans)
