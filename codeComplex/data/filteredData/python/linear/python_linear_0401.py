def main(n):
    # Deterministically generate input data based on n
    # n: number of segments
    if n <= 0:
        return

    global EPS, N, M, A, B

    EPS = 1e-6

    # Define fuel weight and base weight deterministically from n
    # Keep M reasonably large but bounded
    M = 1000 + (n * 7)  # base mass

    N = n

    # Generate arrays A and B with reasonable positive values ≥ 1
    # Use simple arithmetic functions; avoid zeros
    A = [(i % 9) + 1 + (i // 3) % 5 for i in range(N)]
    B = [((i * 2) % 11) + 1 + (i // 4) % 6 for i in range(N)]
    B.append(B[0])

    def check(f):
        fuel_left = f
        total_weight = float(M + fuel_left)
        for i in range(N):
            cost = total_weight / A[i]
            fuel_left -= cost
            total_weight -= cost

            cost = total_weight / B[i + 1]
            fuel_left -= cost
            total_weight -= cost
            if fuel_left < 0:
                return False
        return True

    def binary_search(left, right):
        mid = (left + right) / 2
        if abs(left - right) < EPS:
            return mid
        if check(mid):
            return binary_search(left, mid)
        else:
            return binary_search(mid, right)

    res = binary_search(0, 1e9 + 1)
    if res - 1e9 > EPS:
        print(-1)
    else:
        print("{:.10f}".format(res))


if __name__ == "__main__":
    # Example: run with a specific scale n
    main(200)