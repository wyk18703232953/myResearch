def mypw2(deg):
    if (deg >= 1500) : return 2 ** 150
    # if (deg >= 60): return 10**18 * 20
    return 2 ** deg

def sol():
    n, k = map(int, input().split())
    if (k == 0):
        print("YES", n)
        return
    for side in range(1, n + 1):
        MIN = mypw2(side + 1) - side - 2
        MAX = mypw2(2 * n) - mypw2(2 * n - side + 1) + mypw2(side + 1) + mypw2(2 * n - 2 * side) - 2;
        MAX //= 3
        # MAX = (mypw2(2*n) - 1) // 3 - ((2**(2*n - 2 * side) - 1) // 3) * (2**(side + 1) - 1)
        # print(k, MIN, MAX)
        if (MIN <= k <= MAX):
            print("YES", n - side)
            return
    print("NO")

def main():
    t = int(input())
    for i in range(t):
        sol()

main()