# Part 1
input_file = open("test.txt", "r")
height_map = input_file.read().strip().split("\n")
for i, height in enumerate(height_map):
    height_map[i] = list(map(int, height))

print(height_map)

x_dim = len(height_map)
y_dim = len(height_map[0])

# Find adjacent points to given point and add to list
def get_adj(x, y):
    adj = []
    if x > 0: adj.append((x - 1, y))
    if x < y_dim - 1: adj.append((x + 1, y))
    if y > 0: adj.append((x, y - 1))
    if y < x_dim - 1: adj.append((x, y + 1))
    return adj

# Find if given point is a low point or not
def low_pt(x, y):
    point = height_map[y][x]
    adj = get_adj(x, y)
    for location in adj:
        x, y = location
        if point >= height[y][x]: return False
    return True

total_risk = 0
for i, row in enumerate(height_map):
    for j, height in enumerate(row):
        if low_pt(j, i):
            total_risk += height + 1

print(total_risk)