# https://en.wikipedia.org/wiki/Josephus_problem
from math import log, floor
n = 3017957

a = 2*(n-2**floor(log(n)/log(2)))+1
print(a)