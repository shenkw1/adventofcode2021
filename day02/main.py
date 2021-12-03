# Part 1
input_file = open("input.txt", "r")
full_directions = input_file.readlines()
token_directions = list(map(str.split, full_directions))

horizontal = 0
depth = 0
for token in token_directions:
    if token[0] == 'forward':
        horizontal += int(token[1])
    elif token[0] == 'down':
        depth += int(token[1])
    else:
        depth -= int(token[1])

print(horizontal * depth)


# Part 2
horizontal = 0
depth = 0
aim = 0
for token in token_directions:
    token_int = int(token[1])
    if token[0] == 'forward':
        horizontal += token_int
        depth += aim * token_int
    elif token[0] == 'down':
        aim += token_int
    else:
        aim -= token_int

print(horizontal * depth)