"""
--- Day 17: No Such Thing as Too Much ---
The elves bought too much eggnog again - 150 liters this time. To fit it 
all into your refrigerator, you'll need to move it into smaller containers. 
You take an inventory of the capacities of the available containers.

For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. 
If you need to store 25 liters, there are four ways to do it:

15 and 10
20 and 5 (the first 5)
20 and 5 (the second 5)
15, 5, and 5
Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog?
"""

from itertools import combinations

containers_int = [33, 14, 18, 20, 45, 35, 16, 35, 1, 13, 18, 13, 50, 44, 48, 6, 24, 41, 30, 42]
containers = [str(x) for x in containers_int]

total = 0
for i in [4]:
    combs = combinations(containers, i)

    for comb in combs:
        if sum([int(x) for x in comb]) == 150:
            total += 1

print(total)