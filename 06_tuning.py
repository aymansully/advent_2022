def read_file():
    read_file = open("input_location.txt", "r")
    input_location = read_file.readline()
    full_input = input_location + "\\6_input.txt"
    # full_input = input_location + "\\6_sample.txt"
    full_file = open(full_input, "r")
    lines = full_file.readlines()
    return lines

def part1(lines):
    # sequence of four characters that are all different.
    linelist = [x for x in lines[0]]
    for i in range(len(linelist)):
        sliding_set = set(linelist[i:i+4])
        if len(sliding_set) == 4:
            print("marker at", i+4)
            return
        
def part2(lines):
    linelist = [x for x in lines[0]]
    for i in range(len(linelist)):
        sliding_set = set(linelist[i:i+14])
        if len(sliding_set) == 14:
            print("marker at", i+14)
            return

def main():
    lines = read_file()
    # part1(lines)
    part2(lines)

if __name__ == '__main__':
    main()