def mypw2(deg):
    if deg >= 1500:
        return 2 ** 150
    return 2 ** deg

def sol(n, k):
    if k == 0:
        # print("YES", n)
        pass
        return
    for side in range(1, n + 1):
        MIN = mypw2(side + 1) - side - 2
        MAX = mypw2(2 * n) - mypw2(2 * n - side + 1) + mypw2(side + 1) + mypw2(2 * n - 2 * side) - 2
        MAX //= 3
        if MIN <= k <= MAX:
            # print("YES", n - side)
            pass
            return
    # print("NO")
    pass

def main(n):
    t = n
    for i in range(1, t + 1):
        ni = i
        ki = i * i
        sol(ni, ki)

if __name__ == "__main__":
    main(10)