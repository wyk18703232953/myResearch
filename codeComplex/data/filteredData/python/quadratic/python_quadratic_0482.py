def main(n):
    # Generate deterministic L and R based on n
    # L[i] and R[i] are bounded by n-1 and constructed deterministically
    L = [i % n for i in range(n)]
    R = [(n - 1 - i) % n for i in range(n)]

    E = []
    otv = [0] * n

    for i in range(n):
        sum_ = L[i] + R[i]
        E.append([sum_, i])
    E.sort()

    for i in range(n):
        x = R[i]
        for j in range(n):
            if x > 0:
                if E[j][1] > i:
                    otv[E[j][1]] += 1
                    x -= 1
            else:
                break

        if x > 0:
            print("NO")
            return

        x = L[i]
        for j in range(n):
            if x > 0:
                if E[j][1] < i:
                    otv[E[j][1]] += 1
                    x -= 1
            else:
                break

        if x > 0:
            print("NO")
            return

    for i in range(n):
        r = 0
        l = 0
        for j in range(i + 1, n):
            if otv[j] > otv[i]:
                r += 1
        for z in range(i - 1, -1, -1):
            if otv[z] > otv[i]:
                l += 1
        if (r != R[i]) or (l != L[i]):
            print("NO")
            return

    print("YES")
    for i in range(n):
        print(otv[i] + 1, end=' ')
    print()


if __name__ == "__main__":
    # Example deterministic calls for time complexity experiments
    main(5)
    main(10)