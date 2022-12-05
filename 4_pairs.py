def read_file():

    read_file = open("input_location.txt", "r")
    input_location = read_file.readline()
    full_input = input_location + "\\4_input.txt"
    # full_input = input_location + "\\4_sample.txt"
    full_file = open(full_input, "r")
    lines = full_file.readlines()
    return lines

def part1(lines):
    overlaps = 0
    numbers = list(range(100))
    for row in lines:
        row = row.strip()
        pairs = row.split(",")
        left_from_to = pairs[0].split("-")
        right_from_to = pairs[1].split("-")
        left = numbers[int(left_from_to[0]):int(left_from_to[1])+1]
        right = numbers[int(right_from_to[0]):int(right_from_to[1])+1]
        left_set = set(left)
        right_set = set(right)
        if left_set.issubset(right_set) or right_set.issubset(left_set):
            overlaps += 1
    print(overlaps)

def part2(lines):
    overlaps = 0
    numbers = list(range(100))
    for row in lines:
        row = row.strip()
        pairs = row.split(",")
        left_from_to = pairs[0].split("-")
        right_from_to = pairs[1].split("-")
        left = numbers[int(left_from_to[0]):int(left_from_to[1])+1]
        right = numbers[int(right_from_to[0]):int(right_from_to[1])+1]
        left_set = set(left)
        right_set = set(right)
        if not left_set.isdisjoint or not right_set.isdisjoint(left_set):
            overlaps += 1
    print(overlaps)

def main():
    lines = read_file()
    # part1(lines)
    part2(lines)

if __name__ == '__main__':
    main()
    