

# Read the input file
filepath = "AoC_2024\\Day5\\input.txt"
with open(filepath, "r", encoding="utf-8") as file:
    data = [line for line in file.read().split("\n") if line.strip()]
    block_1 = [line for line in data if '|' in line]
    block_2 = [line for line in data if ',' in line]

    print(data)
    print(block_1)
    print(block_2)

