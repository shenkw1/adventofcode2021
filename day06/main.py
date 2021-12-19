# Part 1
input_file = open("input.txt", "r")
fish_timers = list(map(int, input_file.read().strip().split(",")))

for i in range(80):
    for i in range(len(fish_timers)):
        if fish_timers[i] == 0:
            fish_timers[i] = 6
            fish_timers.append(8)
        else:
            fish_timers[i] -= 1

print(len(fish_timers))

# Part 2
timer_dict = dict.fromkeys(range(9), 0)
for timer in fish_timers: # Starting from 80
    timer_dict[timer] += 1

for i in range(256 - 80):
    new_times = dict.fromkeys(range(9), 0)
    for key in timer_dict:
        if key == 0:
            new_times[6] += timer_dict[key]
            new_times[8] += timer_dict[key]
        else:
            new_times[key - 1] += timer_dict[key]
    timer_dict = new_times

cum_sum = 0
for key in timer_dict:
    cum_sum += timer_dict[key]
print(cum_sum)