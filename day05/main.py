# Part 1
input_file = open("input.txt", "r")
vents = input_file.read().strip().split("\n")
for i, vent in enumerate(vents):
    vents[i] = vent.split(" -> ")
    for j, coord in enumerate(vents[i]):
        vents[i][j] = list(map(int, coord.split(",")))

# Find grid dimensions
x_max = y_max = 0
for line in vents:
    for coord in line:
        x_max = max(coord[0], x_max)
        y_max = max(coord[1], y_max)

x_max += 1
y_max += 1

# Make and fill grid
grid = [[0] * x_max for _ in range(y_max)]
for [[x1, y1],[x2, y2]] in vents:
    if x1 == x2: # Vertical line
        min_y = min(y1, y2)
        max_y = max(y1, y2)
        for i in range(min_y, max_y + 1): grid[i][x1] += 1
    
    if y1 == y2: # Horizontal line
        min_x = min(x1, x2)
        max_x = max(x1, x2)
        for i in range(min_x, max_x + 1): grid[y1][i] += 1

# Counting overlaps
count = 0
for row in grid:
    for col in row:
        if col >= 2:
            count += 1

print(count)

# Part 2
# Filling diagonals
for [[x1, y1],[x2, y2]] in vents:
    if x1 != x2 and y1 != y2:
        dist = abs(x1 - x2)
        for i in range(dist + 1):
            if (y1 > y2): # Going up
                # Going right
                if (x1 < x2): grid[y1 - i][x1 + i] += 1
                # Going left
                else:         grid[y1 - i][x1 - i] += 1
            else: # Going down
                # Going right
                if (x1 < x2): grid[y1 + i][x1 + i] += 1
                # Going left
                else:         grid[y1 + i][x1 - i] += 1

# Counting overlaps with diagonals
count = 0
for row in grid:
    for col in row:
        if col >= 2: count += 1

print(count)