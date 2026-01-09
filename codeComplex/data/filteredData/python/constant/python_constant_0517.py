def main(n):
    x = n
    y = n // 2
    z = 0
    t1 = 1 + (n % 5)
    t2 = 1 + (n % 3)
    t3 = 1 + (n % 4)
    stair = t1 * abs(x - y)
    lift = t2 * (abs(z - x) + abs(x - y)) + t3 * 3
    # print("YES" if lift <= stair else "NO")
    pass
if __name__ == "__main__":
    main(10)