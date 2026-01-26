import sys

def pprint(s):
    sys.stdout.write(str(s) + "\n")

def solve(n, d, k):
    for i in range(1, d + 1):
        pprint(str(i) + ' ' + str(i + 1))
        if i + 1 == n:
            return

    q = d + 2
    for i in range(2, d + 1):
        for j in range(k - 2):
            pprint(str(i) + ' ' + str(q))
            if q == n:
                return
            q += 1

            def rec(depth, current, head):
                # keep recursion and edge-printing logic identical, but return instead of exit
                if depth == 0:
                    return current
                for _ in range(k - 1):
                    pprint(str(head) + ' ' + str(current))
                    if current == n:
                        return current
                    current += 1
                    current = rec(depth - 1, current, current - 1)
                    if current >= n:
                        return current
                return current

            if i <= (d + 2) / 2:
                depth = i - 2

            else:
                depth = d - i

            q = rec(depth, q, q - 1)
            if q >= n:
                return

def main(n):
    # Deterministically map n to parameters (n_param, d, k) preserving original constraints.
    # We choose:
    #   k in [2..5], cycling with n
    #   d in [2..(n_param-1)], but also small enough to keep maxi reasonably sized
    if n < 4:
        n_param = 4

    else:
        n_param = n

    k = 2 + (n_param % 4)  # 2,3,4,5 cycle
    if k < 2:
        k = 2

    # ensure d >= 2 and d < n_param
    d = 2 + (n_param % max(1, (n_param - 3)))
    if d >= n_param:
        d = n_param - 1
    if d < 2:
        d = 2

    q = k - 1
    maxi = 0
    if k == 2:
        maxi = d + 1

    else:
        if d % 2:
            maxi = (q * (1 - q ** (d // 2)) // (1 - q) + 1) * 2

        else:
            maxi = (q * (1 - q ** (d // 2 - 1)) // (1 - q) + 1) * 3 + 1

    if d == 2:
        maxi = k + 1

    # Clamp n_param into (d, maxi] if needed to satisfy original feasibility condition
    if n_param <= d:
        n_param = d + 1
    if n_param > maxi:
        n_param = maxi

    if n_param > maxi or n_param <= d:
        # print("NO")
        pass

    else:
        # print("YES")
        pass
        solve(n_param, d, k)

if __name__ == "__main__":
    # Example deterministic call; change the argument to test different scales.
    main(10)