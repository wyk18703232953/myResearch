def main(n):
    # Interpret n as the upper bound b, set a = 1 deterministically
    a = 1
    b = n
    c, d = (((b + 1) // 2) - 1, (b - a - 1))
    result = c if d < 0 else c - d if c > d else 0
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)