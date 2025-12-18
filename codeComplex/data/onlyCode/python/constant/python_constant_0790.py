#   Author: yumtam
#   Created at: 2021-05-02 23:39

def is_square(x):
    sq = int(x**0.5)
    return sq * sq == x

for _ in range(int(input())):
    n = int(input())

    if ((n % 2 == 0 and is_square(n//2))
            or (n % 4 == 0 and is_square(n//4))):
        print("YES")
    else:
        print("NO")
