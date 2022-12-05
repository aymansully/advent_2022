"""
1 
"""
def read_file():

    read_file = open("input_location.txt", "r")
    input_location = read_file.readline()
    full_input = input_location + "\\2_input.txt"
    full_file = open(full_input, "r")
    lines = full_file.readlines()
    return lines

def main():
    # 1 rock, 2 paper, 3 scissors
    # A rock, B paper, C scissors opponent
    # X rock, Y paper, Z scissors you
    # 0 for loss, 3 for draw, 6 for win
    points = {"A":1, "B":2, "C":3}
    lines = read_file()
    # part1(lines)
    part2(lines)
    
def part2(lines):
    # X you need to lose, Y Draw, Z Win
    wins = ["A Y", "B Z", "C X"]
    loss = ["A Z", "B X", "C Y"]
    draw = ["A X", "B Y", "C Z"]
    choice = {
        "A X": "Z",
        "A Y": "X",
        "A Z": "Y",
        "B X": "X",
        "B Y": "Y",
        "B Z": "Z",
        "C X": "Y",
        "C Y": "Z",
        "C Z": "X"
                    }
    total_points = 0
    for row in lines:
        row = row[:3]
        new_symbol = choice[row]
        row = row[:2] + new_symbol
        if row in wins:
            total_points += 6
        elif row in draw:
            total_points += 3
        if row[2] == "X":
            total_points += 1
        elif row[2] == "Y":
            total_points += 2
        elif row[2] == "Z":
            total_points += 3
    print("total:" + str(total_points))
    return total_points

def part1(lines):
    total_points = 0
    wins = ["A Y", "B Z", "C X"]
    loss = ["A Z", "B X", "C Y"]
    draw = ["A X", "B Y", "C Z"]
    for row in lines:
        row = row[:3]
        if row in wins:
            # print("win found")
            total_points += 6
        elif row in draw:
            # print("draw found")
            total_points += 3
        if row[2] == "X":
            total_points += 1
        elif row[2] == "Y":
            total_points += 2
        elif row[2] == "Z":
            total_points += 3
    print("total:" + str(total_points))
    return total_points


if __name__ == '__main__':
    main()