# Converted version with main(n) and generated test data, no input()

import random

MOD = 10**9 + 7

#---------------------------------running code logic as a function------------------------------------------

def solve_instance(n, k, l, f, h):
    # Build frequency dictionaries
    d1 = dict({(a, 0) for a in f})
    d2 = dict({(a, 0) for a in f})

    for a in l:
        if a in d1:
            d1[a] += 1
    for a in f:
        d2[a] += 1

    # Original dp array is fixed size: 520 x (520*12)
    # We keep the same size to preserve original behavior.
    max_x = 520
    max_y = 520 * 12
    dp = [[0 for _ in range(max_y)] for _ in range(max_x)]

    # Triple loop from original code
    # Note: x+1 and y+i must stay within dp bounds; original code assumes n,k small.
    for x in range(n + 1):
        if x + 1 >= max_x:
            break
        for y in range(n * k + 1):
            if y >= max_y:
                break
            base = dp[x][y]
            for i in range(k + 1):
                ny = y + i
                if ny >= max_y:
                    break
                gain = 0 if i == 0 else h[i - 1]
                if dp[x + 1][ny] < base + gain:
                    dp[x + 1][ny] = base + gain

    ss = 0
    for key in d1:
        x = d2[key]
        y = d1[key]
        if x < max_x and y < max_y:
            ss += dp[x][y]
    return ss


#---------------------------------test-data-driven main------------------------------------------

def main(n: int):
    """
    n: problem size parameter (controls length of arrays).
    We generate:
      - k in [1, min(10, n)]
      - arrays l, f of length n with values in [1, n]
      - h of length k with values in [1, 10]
    Then run the original logic and print the result.
    """
    if n <= 0:
        print(0)
        return

    # Choose k based on n but bounded to keep DP reasonable
    k = max(1, min(10, n))

    # Generate test arrays
    # l and f share the same value range so that intersections exist
    l = [random.randint(1, n) for _ in range(n)]
    f = [random.randint(1, n) for _ in range(n)]
    h = [random.randint(1, 10) for _ in range(k)]

    ans = solve_instance(n, k, l, f, h)
    print(ans)


if __name__ == "__main__":
    # Example: run with n = 10
    main(10)