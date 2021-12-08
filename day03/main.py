# Part 1
input_file = open("input.txt", "r")
binary_nums = input_file.read().strip().split("\n")
gamma = epsilon = ""

for i in range(len(binary_nums[0])):
    count_0 = count_1 = 0
    for binary_num in binary_nums:
        if binary_num[i] == "0":
            count_0 += 1
        else:
            count_1 += 1

    gamma += "1" if count_0 > count_1 else "0"
    epsilon += "0" if count_0 > count_1 else "1"

gamma_int = int(gamma, 2)
epsilon_int = int(epsilon, 2)
print(gamma_int * epsilon_int)

# Part 2
oxygen_bits = binary_nums[:]
co2_bits    = binary_nums[:] 

i = 0
while len(oxygen_bits) != 1:
    count_0 = count_1 = 0
    list_0 = []
    list_1 = []
    for bit in oxygen_bits:
        if bit[i] == "0":
            count_0 += 1
            list_0.append(bit)
        else:
            count_1 += 1
            list_1.append(bit)
    oxygen_bits = list_0 if count_0 > count_1 else list_1
    i += 1
oxygen_rating = int(oxygen_bits[0], 2)

i = 0
while len(co2_bits) != 1:
    count_0 = count_1 = 0
    list_0 = []
    list_1 = []
    for bit in co2_bits:
        if bit[i] == "0":
            count_0 += 1
            list_0.append(bit)
        else:
            count_1 += 1
            list_1.append(bit)
    co2_bits = list_0 if count_0 <= count_1 else list_1
    i += 1
co2_rating = int(co2_bits[0], 2)

print(oxygen_rating * co2_rating)