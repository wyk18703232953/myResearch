from collections import Counter

def main(n):
    # Deterministic data generation:
    # c is a fixed value, and a is of length n with a pattern depending on i
    c = 5
    a = [(i % 10) for i in range(n)]

    tel = Counter()
    target_count_last = Counter()
    targets = 0
    best = 0

    for num in a:
        if num == c:
            targets += 1

        else:
            since_last = targets - target_count_last[num]
            target_count_last[num] = targets
            tel[num] = max(0, tel[num] - since_last)
            tel[num] += 1
            best = max(best, tel[num])

    result = targets + best
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)