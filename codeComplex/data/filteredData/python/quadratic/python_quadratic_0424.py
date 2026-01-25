def main(n):
    # n is the length of the list / string of digits
    if n <= 0:
        print("NO")
        return

    # Deterministic generation of ls: alternating 1 and 2 for example
    # This keeps values small while allowing varying prefix sums
    ls = [(i % 3) for i in range(1, n + 1)]  # sequence: 1,2,0,1,2,0,...

    pre = []
    s = 0
    for i in ls:
        s += i
        pre.append(s)

    for i in range(n - 1):
        cnt = 0
        su = 0
        for j in range(i + 1, n):
            su += ls[j]
            if su == pre[i]:
                cnt += 1
                su = 0
        if cnt and su == 0:
            print("YES")
            return
    print("NO")


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)