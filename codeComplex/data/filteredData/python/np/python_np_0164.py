from math import gcd

def main(n):
    # Map n to problem parameters
    # Use n as the number of elements
    n = max(1, int(n))

    # Deterministically construct l, r, x based on n
    # l roughly ~ n, r ~ 3*n, x ~ 2 but all deterministic
    l = n
    r = 3 * n
    x = 2 if n >= 2 else 0

    # Deterministically construct arr of length n
    # Example: arr[i] = (i * 3) % (n + 5) + 1
    arr = [((i * 3) % (n + 5)) + 1 for i in range(n)]

    cnt = 0
    # Enumerate all non-empty subsets with at least 2 elements (same as original starting from 2)
    for mask in range(1, 1 << n):
        # Count bits to ensure subset size >= 2 (original code implicitly enforced by mask>=2)
        if mask & (mask - 1) == 0:
            continue  # only one bit set → size 1, skip

        s = 0
        mx = float('-inf')
        mi = float('inf')
        for j in range(n):
            if mask & (1 << j):
                v = arr[j]
                if v > mx:
                    mx = v
                if v < mi:
                    mi = v
                s += v
        if l <= s <= r and mx - mi >= x:
            cnt += 1

    print(cnt)
    return cnt


if __name__ == "__main__":
    # Example deterministic call for experimentation
    main(10)