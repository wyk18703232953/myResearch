def main(n):
    # Deterministic data generation based on n
    # L[i]: number of greater elements to the left
    # R[i]: number of greater elements to the right
    L = [i % (n // 2 + 1) for i in range(n)]
    R = [(n - 1 - i) % (n // 2 + 1) for i in range(n)]

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
            return "NO"

        x = L[i]
        for j in range(n):
            if x > 0:
                if E[j][1] < i:
                    otv[E[j][1]] += 1
                    x -= 1

            else:
                break

        if x > 0:
            return "NO"

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
            return "NO"

    result = ["YES"]
    result.append(" ".join(str(otv[i] + 1) for i in range(n)))
    return "\n".join(result)


if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    n = 10
    output = main(n)
    # print(output)
    pass