input_file = "day1/puzzle2/input.txt"


total_calories = 0
current_total = 0
elfs_calories = []
with open(input_file, "r") as input_file:
    for line in input_file:
        stripped_line = line.strip()
        if stripped_line == "":
            elfs_calories.append(current_total)
            current_total = 0
        else:
            current_total += int(stripped_line)


elfs_calories.sort(reverse=True)

print(sum(elfs_calories[:3]))