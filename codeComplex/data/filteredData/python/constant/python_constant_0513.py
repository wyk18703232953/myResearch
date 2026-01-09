def main(n):
    x = n
    y = n // 2
    z = n // 3 + 1
    t1 = 1 + (n % 5)
    t2 = 2 + (n % 7)
    t3 = 3 + (n % 3)

    ladder = abs(x - y) * t1
    elevator = abs(x - z) * t2 + 3 * t3 + abs(x - y) * t2
    if elevator > ladder:
        # print("NO")
        pass

    else:
        # print("YES")
        pass
if __name__ == "__main__":
    main(1000)