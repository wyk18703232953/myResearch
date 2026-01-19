def main(n):
    # Interpret n as number of problems
    if n <= 0:
        return 0

    # Deterministic parameters based on n
    l = n * (n + 1) // 4
    r = n * (n + 1) // 2
    x = max(1, n // 5)

    # Deterministic list of difficulties
    temp = [(i + 1) * 3 for i in range(n)]
    temp.sort()

    ans = 0
    for mask in range(1 << n):
        score = 0
        _min = 10**18
        _max = -10**18
        for j in range(n):
            if mask & (1 << j):
                v = temp[j]
                if v < _min:
                    _min = v
                if v > _max:
                    _max = v
                score += v
        if _min <= _max and l <= score <= r and _max - _min >= x:
            ans += 1
    return ans


if __name__ == "__main__":
    # Example call; adjust n for different input scales
    result = main(5)
    print(result)