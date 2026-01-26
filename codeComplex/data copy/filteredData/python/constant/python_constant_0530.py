def main(n):
    x = n
    y = 0
    z = n // 2
    t1 = 1 + (n % 5)
    t2 = 1 + (n % 3)
    t3 = 1 + (n % 7)

    if abs(x - z) * t2 + abs(x - y) * t2 + t3 * 3 <= t1 * abs(x - y):
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)