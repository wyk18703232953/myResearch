def main(n):
    # Interpret n as the length of the input list, capped at 14 since the algorithm uses 14 positions
    length = 14 if n >= 14 else max(1, n)

    # Deterministically generate the input array 'a' of size 14 as in the original logic
    # Fill first `length` elements with a simple pattern, rest with zeros
    a = [0] * 14
    for i in range(length):
        a[i] = (i * 3 + 5) % 100 + 1  # simple deterministic positive integers

    ans = 0
    for i in range(len(a)):
        x = a[i]
        b = [j for j in a]
        b[i] = 0
        for j in range(len(a)):
            b[j] += x // 14

        for j in range(1, x % 14 + 1):
            b[(i + j) % 14] += 1

        ans_now = 0
        for j in b:
            if j % 2 == 0:
                ans_now += j
        ans = max(ans_now, ans)

    return ans


if __name__ == "__main__":
    # Example deterministic call for scaling experiment
    result = main(20)
    # print(result)
    pass