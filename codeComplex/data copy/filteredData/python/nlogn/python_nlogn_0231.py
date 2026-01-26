def main(n):
    if n <= 0:
        return

    # Generate deterministic points A of size n
    # A[i] = [i, (i*i) % (max(1, n//2))]
    modv = max(1, n // 2)
    A = [[i, (i * i) % modv] for i in range(n)]

    if n <= 4:
        # print("YES")
        pass
        return

    def is_colinear(a1, a2, a3):
        if a1 == a2 or a2 == a3 or a1 == a3:
            return True

        x1, y1 = a1
        x2, y2 = a2
        x3, y3 = a3

        if x1 == x2 or x1 == x3 or x2 == x3:
            return x1 == x2 == x3
        if y1 == y2 or y1 == y3 or y2 == y3:
            return y1 == y2 == y3
        return (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1)

    X, Y, Z = A[0], A[1], A[2]

    def good(P, Q):
        bad = []
        for i in range(n):
            if not is_colinear(P, Q, A[i]):
                bad.append(A[i])

        if len(bad) <= 2:
            return True

        U, V = bad[0], bad[1]
        for i in range(len(bad)):
            if not is_colinear(U, V, bad[i]):
                return False
        return True

    if good(X, Y) or good(Y, Z) or good(X, Z):
        # print("YES")
        pass
        return

    # print("NO")
    pass
if __name__ == "__main__":
    main(10)