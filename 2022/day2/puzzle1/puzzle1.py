input_file = "day2/puzzle1/input.txt"
# input_file = "day2/puzzle1/test_input.txt"

total_score = 0
with open(input_file, "r") as input_file:
    for line in input_file:
        text_line = line.strip()

        [opponents_choice, your_choice] = text_line.split()
        # Rock =     A/X
        # Paper =    B/Y
        # Sciccors = C/Z
        
        if your_choice == "X":
            total_score += 1
            if opponents_choice == "A":
                total_score += 3
            elif opponents_choice == "B":
                total_score += 0
            elif opponents_choice == "C":
                total_score += 6

        if your_choice == "Y":
            total_score += 2
            if opponents_choice == "A":
                total_score += 6
            elif opponents_choice == "B":
                total_score += 3
            elif opponents_choice == "C":
                total_score += 0
        
        if your_choice == "Z":
            total_score += 3
            if opponents_choice == "A":
                total_score += 0
            elif opponents_choice == "B":
                total_score += 6
            elif opponents_choice == "C":
                total_score += 3

print(total_score)

