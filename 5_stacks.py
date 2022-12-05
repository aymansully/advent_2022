def read_file():
    
    read_file = open("input_location.txt", "r")
    input_location = read_file.readline()
    full_input = input_location + "\\5_input.txt"
    # full_input = input_location + "\\5_sample.txt"
    full_file = open(full_input, "r")
    lines = full_file.readlines()
    return lines

def part1(lines):
    stack_count = len(lines[0])//4
    stacks = [[] for i in range(stack_count)]
    # build the stacks top down

    movements_start = 0
    for row in lines:
        if len(row) == 1:
            break
        index = 0
        for i in range(0,len(lines[0]),4):
            if row[i+1] != " ": 
                stacks[index].append(row[i+1])
            index += 1
        movements_start += 1 # to track when movement commands start
    for stacklist in stacks:
        print(stacklist)
    print("start index", movements_start)

    for row in lines[movements_start+1:]:
        commands = row.split(" ")
        move_count = int(commands[1])
        move_from = int(commands[3])
        move_to = int(commands[5])
        for move in range(move_count):
            box = stacks[move_from-1].pop(0) # pop out
            stacks[move_to-1].insert(0, box) # insert
    
    for stacklist in stacks:
        print(stacklist[0], end="")

def part2(lines):
    stack_count = len(lines[0])//4
    stacks = [[] for i in range(stack_count)]
    # build the stacks top down

    movements_start = 0
    for row in lines:
        if len(row) == 1:
            break
        index = 0
        for i in range(0,len(lines[0]),4):
            if row[i+1] != " ": 
                stacks[index].append(row[i+1])
            index += 1
        movements_start += 1 # to track when movement commands start
    for stacklist in stacks:
        print(stacklist)
    print("start index", movements_start)

    for row in lines[movements_start+1:]:
        commands = row.split(" ")
        move_count = int(commands[1])
        move_from = int(commands[3])
        move_to = int(commands[5])

        move_list = stacks[move_from-1][0:move_count] # copy
        del stacks[move_from-1][0:move_count] # delete
        stacks[move_to-1] = move_list + stacks[move_to-1] # insert
    
    for stacklist in stacks:
        print(stacklist[0], end="")

def main():
    lines = read_file()
    # part1(lines)
    part2(lines)

if __name__ == '__main__':
    main()
    