def main(n):
    # Deterministically generate K and array A based on n
    K = max(1, n // 3)
    A = [(3 * i + 1) % (5 * n + 7) for i in range(n)]
    A.sort()
    s = []
    for a in A:
        if not s:
            s.append(a)
            continue
        while s:
            if a - K <= s[-1] < a:
                s.pop()

            else:
                break
        s.append(a)
    return len(s)


if __name__ == "__main__":
    result = main(1000)
    # print(result)
    pass