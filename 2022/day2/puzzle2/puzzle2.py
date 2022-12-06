input_file = "day2/puzzle2/input.txt"
# input_file = "day2/puzzle2/test_input.txt"

total_score = 0
with open(input_file, "r") as input_file:
    for line in input_file:
        text_line = line.strip()

        [opponents_choice, result] = text_line.split()
        # Rock =     A/X
        # Paper =    B/Y
        # Sciccors = C/Z

        # X = Lose
        # Y = Draw
        # Z = Win

        # A > Z
        # A = X
        # A < Y

        # B > X
        # B = Y
        # B < Z

        # C > Y
        # C = Z
        # C < X

        if result == "X":
            total_score += 0
            if opponents_choice == "A":
                total_score += 3
            elif opponents_choice == "B":
                total_score += 1
            elif opponents_choice == "C":
                total_score += 2

        if result == "Y":
            total_score += 3
            if opponents_choice == "A":
                total_score += 1
            elif opponents_choice == "B":
                total_score += 2
            elif opponents_choice == "C":
                total_score += 3
        
        if result == "Z":
            total_score += 6
            if opponents_choice == "A":
                total_score += 2
            elif opponents_choice == "B":
                total_score += 3
            elif opponents_choice == "C":
                total_score += 1

print(total_score)

