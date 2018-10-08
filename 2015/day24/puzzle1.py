from itertools import combinations
from functools import reduce

weights = [1, 2, 3, 7, 11, 13, 17, 19, 23, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
part = sum(weights)
ans1 = 1e20
ans2 = 1e20
for i in range(1,8):
    for c in combinations(weights, i):
        if sum(c) == part / 3:
            ans1 = min(ans1, reduce(lambda a, b: a * b, list(c)))
        if sum(c) == part / 4:
            ans2 = min(ans2, reduce(lambda a, b: a * b, list(c)))
print(ans1)
print(ans2)