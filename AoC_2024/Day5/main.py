import pathlib

file_path = pathlib.Path(__file__).parent.resolve().joinpath("input.txt")
# Read the input file
with open(file_path, "r", encoding="utf-8") as file:
    data = [line for line in file.read().split("\n") if line.strip()]
    block_1 = [line for line in data if '|' in line]
    block_2 = [line for line in data if ',' in line]

    print(data)
    print(block_1)
    print(block_2)

