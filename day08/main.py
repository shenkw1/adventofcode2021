# Part 1
input_file = open("input.txt", "r")
entries = input_file.read().strip().split("\n")
for i, entry in enumerate(entries):
    entries[i] = entry.split(" | ")
    
for entry in entries:
    for i, entry_part in enumerate(entry):
        entry[i] = entry_part.split()

count = 0
for entry in entries:
    for output_value in entry[1]:
        if len(output_value) in [2, 4, 3, 7]:
            count += 1

print(count)

# Part 2
total_output = 0

for entry in entries:
    signal_patterns = entry[0]
    output_values = entry[1]
    base_digits = {}
    combined_digits = 0
    for pattern in signal_patterns:
        if len(pattern) == 2: base_digits[1] = set(pattern)
        elif len(pattern) == 4: base_digits[4] = set(pattern)
        elif len(pattern) == 3: base_digits[7] = set(pattern)
        elif len(pattern) == 7: base_digits[8] = set(pattern)
    # Map has 1, 4, 7, 8 and associated sets
    
    for pattern in signal_patterns:
        if len(pattern) == 6:
            if base_digits[7].issubset(pattern):
                if base_digits[4].issubset(pattern): base_digits[9] = set(pattern)
                else: base_digits[0] = set(pattern)
            else: base_digits[6] = set(pattern)
        if len(pattern) == 5:
            if base_digits[1].issubset(pattern): base_digits[3] = set(pattern)
            else:
                if (base_digits[8] - base_digits[4]).issubset(pattern): base_digits[2] = set(pattern)
                else: base_digits[5] = set(pattern)
    # Map has all numbers
    
    multiplier = 1000
    for output in output_values:
        # Compare to map and compute number
        for i in base_digits:
            if base_digits[i] == set(output):
                combined_digits += (multiplier * i)
        multiplier /= 10
    total_output += combined_digits

print(int(total_output))