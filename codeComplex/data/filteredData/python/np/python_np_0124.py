import math
import random
from collections import defaultdict

def solve(l, cost):
    n = len(l)
    dp = defaultdict(int)
    dp[0] = 0
    se = {0}
    for i in range(n):
        # snapshot current states to avoid modifying during iteration
        current_states = list(se)
        for j in current_states:
            k = math.gcd(j, l[i])
            new_cost = dp[j] + cost[i]
            if dp[k] == 0:
                dp[k] = new_cost
            else:
                dp[k] = min(dp[k], new_cost)
        se = set(dp.keys())
    if dp[1] == 0:
        return -1
    return dp[1]


def main(n):
    """
    n: problem size (number of elements in l and cost)

    Generates random test data of size n and runs the original logic.
    Returns the result instead of printing.
    """
    if n <= 0:
        return -1

    # Generate l with values between 1 and 1000
    l = [random.randint(1, 1000) for _ in range(n)]
    # Generate costs between 1 and 1000
    cost = [random.randint(1, 1000) for _ in range(n)]

    return solve(l, cost)


if __name__ == "__main__":
    # Example run with n = 5
    print(main(5))