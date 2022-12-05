def main():
    calorie_per_elf = []
    
    read_file = open("input_location.txt", "r")
    input_location = read_file.readline()
    full_input = input_location + "\\1_input.txt"
    full_file = open(full_input, "r")
    lines = full_file.readlines()

    total_cal = 0
    for row in lines:
        row = row.strip()
        try:
            total_cal += int(row)
        except ValueError:
            calorie_per_elf.append(total_cal)
            total_cal = 0

    print("highest cal: " + str(max(calorie_per_elf)))

    # Part 2: find the total of the top 3

    calorie_per_elf.sort(reverse=True)
    highest_3 = calorie_per_elf[0]+calorie_per_elf[1]+calorie_per_elf[2]

    print("highest top3: " + str(highest_3))

if __name__ == '__main__':
    main()