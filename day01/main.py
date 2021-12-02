# Part 1
input_file = open("input.txt", "r")
depths = input_file.readlines()
int_depths = list(map(int, depths))

num_increase = 0
prev = int_depths[0]
for depth in int_depths[1:]:
    if depth > prev:
        num_increase += 1
    prev = depth

print(num_increase)

# Part 2
num_increase = 0
for i in range(len(int_depths) - 3):
    prev_window = int_depths[i] + int_depths[i + 1] + int_depths[i + 2]
    curr_window = int_depths[i + 1] + int_depths[i + 2] + int_depths[i + 3]
    if curr_window > prev_window:
        num_increase += 1

print(num_increase)