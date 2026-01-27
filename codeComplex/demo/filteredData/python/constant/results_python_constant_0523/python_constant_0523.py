def main(n):
    x = n
    y = n // 2
    z = n // 3
    t1 = 1
    t2 = 2
    t3 = 3

    tp = abs(x - y) * t1
    pt = (abs(x - y) + abs(x - z)) * t2 + t3 + t3 + t3
    if tp >= pt:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(1000000)