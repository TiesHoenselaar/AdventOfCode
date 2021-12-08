with open('input.txt', 'r') as f:
    input_lines = [int(x) for x in f.read().split(',')]

fishes = input_lines

counts = [0, 0, 0, 0, 0, 0]

for i in range(len(fishes)):
    counts[fishes[i]] += 1

#print(counts)



days = 256

total_amount = 0

amounts2 = []
amounts = []

grande_total = 0


for age in range(1,6):
    print("age:",age)
##for age in [3]:
    fishes = [age]
    amount = 0
    #print(counts)
    #print("Checking age",age,'which occurs',counts[age])
    for day in range(int(days / 2)):
        #print("Age:",age,"Day:",day)
        new_fishes = []
        new_born_fishes = []
        for i in range(len(fishes)):
            if fishes[i] > 0:
                new_fishes.append(fishes[i]-1)
            else:
                new_fishes.append(6)
                new_born_fishes.append(8)

        fishes = new_fishes + new_born_fishes

        #print(fishes)
##    count sub fishes
    counts2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    
    for i in range(len(fishes)):
        counts2[fishes[i]] += 1


    amounts.append(counts2)
    #print(fishes)
    #print("counts2",age,counts2)

    #sub_amounts = [0, 0, 0, 0, 0, 0]
    for sub_age in range(9):
        if counts2[sub_age] != 0:
            sub_fishes = [sub_age]
            #print("\t Checking age",age, 'Sub age', sub_age,'which occurs',counts[counts2[sub_age]])
            for sub_day in range(int(days / 2), days):
                #print(day)
                #print("Age:",age,"Sub_age:", sub_age, "Day:",day)        

                new_sub_fishes = []
                new_born_sub_fishes = []
                for j in range(len(sub_fishes)):
                    if sub_fishes[j] > 0:
                        new_sub_fishes.append(sub_fishes[j]-1)
                    else:
                        new_sub_fishes.append(6)
                        new_born_sub_fishes.append(8)

                sub_fishes = new_sub_fishes + new_born_sub_fishes
            

        if counts2[sub_age] != 0:
            #print("log", age, sub_age, sub_fishes)

            grande_total += counts[age] *counts2[sub_age] * len(sub_fishes)

print(grande_total)
            
    #sub_amounts = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    #for i in range(len(fishes)):
    #    sub_amounts[fishes[i]] += 1

    #total = 0
    #for j, c in enumerate(counts2):
    #    total += sub_amounts[j]*c
    #print(age, total)

    #amounts2.append(sub_amounts)

