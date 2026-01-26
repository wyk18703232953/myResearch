import itertools

def main(n):
    # n controls the number of problems; ensure at least 1
    if n < 1:
        n = 1

    # Deterministic generation of parameters based on n
    # Ensure l <= r and x non-negative
    l = n
    r = 3 * n
    x = max(1, n // 3)

    # Deterministic list of problem difficulties
    problems = [i * 2 + (i % 3) for i in range(n)]

    result = 0
    for i in range(2, n + 1):
        for comb in itertools.combinations(problems, i):
            summ = sum(comb)
            mini = min(comb)
            maxx = max(comb)
            if l <= summ <= r and maxx - mini >= x:
                result += 1
    print(result)


if __name__ == "__main__":
    main(10)