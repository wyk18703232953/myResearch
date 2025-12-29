lst = []

def prepare_lst():
    """Precompute lst as in original code."""
    global lst
    lst = [0, 1]
    now = 1
    # original condition: while now <= 1e25
    LIMIT = int(1e25)
    while now <= LIMIT:
        now = now * 4 + 1
        lst.append(now)

def solve_case(n, k):
    """Solve a single test case with given n, k."""
    if n >= 34:
        return "YES " + str(n - 1)

    sek = 0
    ambil = 1
    nyak = 0
    cnt = 0

    while sek < n:
        cnt = cnt + (1 << (sek + 1)) - 1
        if cnt > k:
            return "NO"

        next_ambil = (ambil + 1) * 2 - 1
        sisa = 4 * ambil - next_ambil
        ambil = next_ambil

        sek += 1
        nyak = nyak + sisa * lst[n - sek]
        if (nyak + cnt) >= k:
            return "YES " + str(n - sek)

    return "NO"

def main(n):
    """
    n: problem scale. We generate n test cases:
       for i in range(1, n+1):
           - set test_n = i
           - set k as some function of i (here k = i * i, can be adjusted)
    Prints the result for each generated test case.
    """
    prepare_lst()

    # Generate deterministic test data based on n.
    # Example strategy:
    #   test_n ranges from 1 to n
    #   k = i * i (or any other reasonable function)
    for i in range(1, n + 1):
        test_n = i
        k = i * i
        ans = solve_case(test_n, k)
        print(ans)


if __name__ == "__main__":
    # Example run with scale 10; change as needed.
    main(10)