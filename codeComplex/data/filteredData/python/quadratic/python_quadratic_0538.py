memo = {}

def max_splits(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    result = 4 * max_splits(n - 1) + 1
    memo[n] = result
    return result

def run_case(n, k):
    min_splits = 1
    path_count = 3

    if n > 75:
        # print("YES", n - 1)
        pass
        return

    square_size = n - 1
    max_buffer = max_splits(square_size)

    while min_splits + path_count <= k and square_size > 0:
        min_splits += path_count
        max_buffer += (4 * path_count - (2 * path_count + 1)) * max_splits(square_size - 1)
        path_count = 2 * path_count + 1
        square_size -= 1

    if min_splits <= k <= min_splits + max_buffer:
        # print("YES", square_size)
        pass

    else:
        # print("NO")
        pass

def main(n):
    global memo
    memo = {}
    if n <= 0:
        return
    t = n
    for i in range(t):
        ni = i + 1
        ki = 2 * ni + (ni % 5)
        run_case(ni, ki)

if __name__ == "__main__":
    main(10)