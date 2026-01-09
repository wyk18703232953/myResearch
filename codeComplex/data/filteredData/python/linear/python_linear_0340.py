def main(n):
    # Deterministic generation of d and lst based on n
    d = (n // 3) + 1
    lst = [i * (d + 1) for i in range(n)]
    lst.sort()

    Ans = 2
    for i in range(1, n):
        if lst[i] - lst[i - 1] > 2 * d:
            Ans += 2
        elif lst[i] - lst[i - 1] == 2 * d:
            Ans += 1
    # print(Ans)
    pass
if __name__ == "__main__":
    main(10)