# Part 1
input_file = open("input.txt", "r")
crab_positions = list(map(int, input_file.read().strip().split(",")))

# Sort list and find median
crab_positions.sort()
if len(crab_positions) % 2 != 0:
    median = crab_positions[len(crab_positions) // 2]
else:
    med_1 = crab_positions[len(crab_positions) // 2]
    med_2 = crab_positions[len(crab_positions) // 2 - 1]
    median = int((med_1 + med_2) / 2)

# Iterate thru positions and subtract median from each element, sum differences
total_fuel = 0
for position in crab_positions:
    total_fuel += abs(position - median)

print(total_fuel)

# Part 2
# Find mean
mean = int(sum(crab_positions) / len(crab_positions))

# Iterate thru positions and subtract mean from each element, sum differences using (n * (n + 1)) / 2
total_fuel = 0
for position in crab_positions:
    n = abs(position - mean)
    total_fuel += (n * (n + 1)) // 2

print(total_fuel)