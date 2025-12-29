from bisect import bisect_right as br
from collections import deque
import random


def main(n: int):
    """
    n: problem scale, used to generate test data.
       We generate:
       - m = n
       - k in [1, max(1, n//3)]
       - s: m sorted integers in [1, 3*n]
    """
    # Generate test data based on n
    m = n
    k = max(1, n // 3)
    # Generate a sorted list s
    s_list = sorted(random.randint(1, 3 * n) for _ in range(m))

    # Core logic from original program
    s = deque(s_list)
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
                    steps = diff // k
                else:
                    steps = diff // k + 1
                lim += steps * k

    print(ans)


if __name__ == "__main__":
    # Example: run with n = 10
    main(10)