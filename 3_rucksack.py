

def read_file():

    read_file = open("input_location.txt", "r")
    input_location = read_file.readline()
    # full_input = input_location + "\\3_sample.txt"
    full_input = input_location + "\\3_input.txt"
    full_file = open(full_input, "r")
    lines = full_file.readlines()
    return lines

def part1(lines, priorities):
    total_priority = 0
    for row in lines:
        left_set = set()
        right_set = set()
        same_set = set()
        row = row.strip()
        # print(row)
        left = row[:len(row)//2]
        right = row[len(row)//2:]
        # print(left)
        # print(right)
        for char in left:
            left_set.add(char)
        for char in right:
            right_set.add(char)
        # print(left_set)
        same_set = left_set.intersection(right_set)
        # print(samechar)

        for char in same_set:
            total_priority += priorities[char]
    print(total_priority)

def part2(lines, priorities):
    total_priority = 0
    count_to_3 = 0
    for row in lines:
        if count_to_3 == 0:
            set_1 = set()
            set_2 = set()
            set_3 = set()
            badge = set()
        row = row.strip()
        print(row)
        if count_to_3 == 0:
            for char in row:
                set_1.add(char)
            count_to_3 += 1
            continue
        elif count_to_3 == 1:
            for char in row:
                set_2.add(char)
            count_to_3 += 1
            continue
        elif count_to_3 == 2:
            for char in row:
                set_3.add(char)
            count_to_3 = 0
        one_two = set_1.intersection(set_2)
        badge = one_two.intersection(set_3)
        print(badge)
        for i in badge:
            total_priority += priorities[i]

    print(total_priority)



def main():
    priorities = {
        "a":1,
        "b":2,
        "c":3,
        "d":4,
        "e":5,
        "f":6,
        "g":7,
        "h":8,
        "i":9,
        "j":10,
        "k":11,
        "l":12,
        "m":13,
        "n":14,
        "o":15,
        "p":16,
        "q":17,
        "r":18,
        "s":19,
        "t":20,
        "u":21,
        "v":22,
        "w":23,
        "x":24,
        "y":25,
        "z":26,
        "A":27,
        "B":28,
        "C":29,
        "D":30,
        "E":31,
        "F":32,
        "G":33,
        "H":34,
        "I":35,
        "J":36,
        "K":37,
        "L":38,
        "M":39,
        "N":40,
        "O":41,
        "P":42,
        "Q":43,
        "R":44,
        "S":45,
        "T":46,
        "U":47,
        "V":48,
        "W":49,
        "X":50,
        "Y":51,
        "Z":52,
    }
    lines = read_file()
    # part1(lines, priorities)
    part2(lines, priorities)

if __name__ == '__main__':
    main()
    