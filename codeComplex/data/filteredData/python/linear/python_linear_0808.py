from bisect import bisect_right as br
from collections import deque

def main(n):
    # Deterministically generate m, k based on n
    m = n
    if m <= 0:
        return 0
    k = max(1, n // 3)

    # Deterministically generate s as a non-decreasing sequence of length m
    # Example: s[i] = (i+1)*2 to ensure sorted and spaced values
    s = deque((i + 1) * 2 for i in range(m))

    lim = k
    ans = 0
    while len(s) != 0:
        x = br(s, lim)
        for _ in range(x):
            s.popleft()
        if x != 0:
            ans += 1
            lim += x

        else:
            if len(s) > 0:
                diff = s[0] - lim
                if diff % k == 0:
                    step = diff // k

                else:
                    step = (diff // k) + 1
                lim += step * k

    # print(ans)
    pass
    return ans

if __name__ == "__main__":
    main(10)