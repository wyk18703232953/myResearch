from bisect import bisect_right as br
from collections import deque

def main(n):
    # Interpret n as the number of elements in the list s
    # Generate deterministic parameters and data
    if n <= 0:
        # print(0)
        pass
        return

    m = n  # unused in original logic but kept for structure
    k = max(1, n // 3)

    # Generate a strictly increasing sequence similar to common problem inputs
    # s[i] = (i + 1) * k ensures increasing order and interaction with k
    arr = [(i + 1) * k for i in range(m)]
    s = deque(arr)

    lim = k
    ans = 0
    while len(s) != 0:
        x = br(arr, lim)
        # x is the count of elements <= lim among the original array arr
        # but we must only pop up to the current remaining size of s
        x = min(x, len(s))
        for _ in range(x):
            s.popleft()
        if x != 0:
            ans += 1
            lim += x

        else:
            if len(s) > 0:
                diff = s[0] - lim
                if diff % k == 0:
                    x = diff // k

                else:
                    x = diff // k + 1
                lim += x * k

    # print(ans)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n here when running experiments
    main(10)