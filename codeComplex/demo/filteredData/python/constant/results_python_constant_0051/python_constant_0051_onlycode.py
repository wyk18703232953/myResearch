import math
def lucky(x):
    return (list(set(list(str(x)))) in [["4"],["7"],["4","7"],["7","4"]])
a = int(input())
true = False
for i in range(1, math.ceil(math.sqrt(a))+1):
    if a % i == 0:
        if lucky(i) or lucky(a//i):
            true = True
            break
print("YES" if true else "NO")