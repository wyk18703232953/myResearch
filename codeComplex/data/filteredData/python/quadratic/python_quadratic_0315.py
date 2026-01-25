def main(n):
    # Map n to original input structure:
    # - first line: n k
    # - second line: n integers
    # Here we set k deterministically as max(1, n // 3)
    if n <= 0:
        print(0.0)
        return

    k = max(1, n // 3)

    # Deterministic generation of li with size n
    # Example pattern: li[i] = (i * 2 + 1)
    li = [(i * 2 + 1) for i in range(n)]

    ans = []
    for i in range(0, n):
        su = 0
        for j in range(i, n):
            su += li[j]
            if (j - i + 1 >= k):
                ans.append(su / (j - i + 1))
    if ans:
        print(max(ans))
    else:
        print(0.0)


if __name__ == "__main__":
    # Example deterministic call
    main(10)