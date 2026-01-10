from heapq import heappush, heappop

def main(n):
    # n: number of elements
    if n <= 0:
        return

    # Deterministic generation of k, powers, coins
    k = max(1, n // 3)

    # Example deterministic patterns:
    # powers: increasing but with some repetition modulo
    powers = [(i * 3 + 7) % (n // 2 + 1) + i // 2 for i in range(n)]
    # coins: varied values depending on i
    coins = [(i * i + 11) % (2 * n + 5) + 1 for i in range(n)]

    A = []
    ans = [0] * n
    for i in range(n):
        A.append((powers[i], coins[i], i))
    A.sort()
    h = []
    total = 0
    for i in range(n):
        _, c, idx = A[i]
        ans[idx] = total + c
        if len(h) < k:
            heappush(h, c)
            total += c
        elif h and h[0] < c:
            total -= heappop(h)
            heappush(h, c)
            total += c

    for x in ans:
        print(x, end=" ")
    print()


if __name__ == "__main__":
    main(10)