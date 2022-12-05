def read_file():
    
    read_file = open("input_location.txt", "r")
    input_location = read_file.readline()
    # full_input = input_location + "\\X_input.txt"
    full_input = input_location + "\\X_sample.txt"
    full_file = open(full_input, "r")
    lines = full_file.readlines()
    return lines

def part1(lines):
    pass

def main():
    lines = read_file()
    part1(lines)

if __name__ == '__main__':
    main()
    