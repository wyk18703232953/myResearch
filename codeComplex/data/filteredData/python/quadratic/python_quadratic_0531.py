def main(n):
    # Deterministically generate a and b based on n
    # a is a permutation [1..n]
    a = list(range(1, n + 1))[::-1]  # original code reverses input immediately
    # b is another permutation: rotate by 1
    b = [(i % n) + 1 for i in range(1, n + 1)]

    # Core logic from original program
    ans = [0] * n
    marked = [True] * (n + 1)
    for i in range(n):
        if marked[b[i]]:
            while True:
                marked[a[-1]] = False
                ans[i] += 1
                if a[-1] == b[i]:
                    a.pop()
                    break
                a.pop()

        else:
            continue

    # print(*ans)
    pass
if __name__ == "__main__":
    main(10)