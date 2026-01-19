def combinations(arr, n):
    if n == 0:
        return [[]]
    result = []
    for i in range(len(arr)):
        first = arr[i]
        rest = arr[i + 1:]
        for comb in combinations(rest, n - 1):
            result.append([first] + comb)
    return result


def solve(arr, n, l, r, x):
    subset = []
    for size in range(2, n + 1):
        for comb in combinations(arr, size):
            s = sum(comb)
            if l <= s <= r:
                subset.append(comb)
    count = 0
    for sub in subset:
        mn = min(sub)
        mx = max(sub)
        if mx - mn >= x:
            count += 1
    return count


def main(n):
    # n controls the size of the input array
    if n < 2:
        n = 2
    # deterministic construction of parameters
    # arr: increasing integers, not strictly necessary but simple
    arr = [i + 1 for i in range(n)]
    # choose l, r, x deterministically based on n
    # l is about 1/3 of total sum, r is total sum
    total_sum = n * (n + 1) // 2
    l = total_sum // 3
    r = total_sum
    # x grows slowly with n
    x = max(1, n // 4)
    result = solve(arr, n, l, r, x)
    print(result)


if __name__ == "__main__":
    main(10)