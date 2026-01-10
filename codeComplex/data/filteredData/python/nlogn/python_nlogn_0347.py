def main(n):
    # Generate deterministic input of size n
    # Interpret n as the length of array a
    # Example pattern: a[i] = i (for i in range(n))
    a = [i for i in range(1, n + 1)]

    d = {}
    power = [2 ** i for i in range(31)]
    ans = []
    for i in a:
        d[i] = 0

    for num in d.keys():
        for p in power:
            if num + p in d:
                ans = [num, num + p]
                if num + p + p in d:
                    print(3)
                    ans.append(num + p + p)
                    print(*ans)
                    return
    if ans:
        print(2)
        print(*ans)
    else:
        print(1)
        print(a[0])


if __name__ == "__main__":
    # Example call for experimentation; adjust n as needed
    main(10)