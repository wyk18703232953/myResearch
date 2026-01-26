import sys

maxN = 10**6 + 5
dp = [0] * maxN
b = [0] * maxN

def main(n):
    # reset arrays for deterministic repeated runs
    for i in range(maxN):
        dp[i] = 0
        b[i] = 0

    # map n to number of beacons N and their positions
    # use N = min(n, maxN - 1) to keep indices in range
    N = n if n < maxN else maxN - 1

    # deterministic construction of beacons:
    # place beacons at positions 1..N with radius depending on i and N
    # ensure 0 <= radius < maxN
    for i in range(1, N + 1):
        # simple deterministic radius: min(i // 2, i - 1) so that radius < position
        radius = i // 2
        if radius >= i:
            radius = i - 1
        # store in b
        b[i] = radius

    if b[0] > 0:
        dp[0] = 1

    for i in range(1, maxN):
        if b[i] == 0:
            dp[i] = dp[i - 1]

        else:
            if b[i] >= i:
                dp[i] = 1

            else:
                dp[i] = dp[i - b[i] - 1] + 1

    result = N - max(dp)
    # print(result)
    pass
    return result

if __name__ == "__main__":
    # example scalable call; change n as needed for experiments
    main(10**5)