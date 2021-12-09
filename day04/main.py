# Part 1
input_file = open("input.txt", "r")
draw_nums = list(map(int, input_file.readline().strip().split(",")))
boards = input_file.read().strip().split("\n\n")

for i in range(len(boards)):
    boards[i] = boards[i].split("\n")
    for j in range(len(boards[i])):
        boards[i][j] = list(map(int, boards[i][j].split()))

called_nums = set()

def find_bingo(num_set):
    for num in draw_nums:
        num_set.add(num)
        for board in boards:
            for row in board:
                bingo = True
                for val in row:
                    if val not in num_set:
                        bingo = False
                        break
                if bingo: return board, num
            
            for i in range(len(board[0])): # Check ith col
                bingo = True
                for j in range(len(board)): # Check ith col in jth row
                    if board[j][i] not in num_set:
                        bingo = False
                        break
                if bingo: return board, num

board, num = find_bingo(called_nums)
print(called_nums)
sum_unmarked = 0

for row in board:
    for val in row:
        if val not in called_nums:
            sum_unmarked += val

print(sum_unmarked * num)
