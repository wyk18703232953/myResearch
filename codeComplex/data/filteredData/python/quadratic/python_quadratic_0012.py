# Collaborated with no one
# Problem C (refactored to main(n) with generated test data)

import math
import random

def main(n):
    """
    n: number of disks to generate test data for.
    We fix the radius r = 1 and generate n x-coordinates.
    """
    # Generate test data
    # disks_rad[0] = number of disks, disks_rad[1] = radius
    disks_rad = [n, 1]
    r = disks_rad[1]

    # Generate n distinct x-coordinates (you can adjust generation logic as needed)
    # Here we space them out randomly in range [0, 3*n]
    nums = sorted(random.sample(range(0, 3 * n + 1), n))

    # Original logic
    ans = []
    ans.append(r)
    for i in range(1, disks_rad[0]):
        y_cord = r
        for j in range(i):
            if (nums[i] - nums[j]) ** 2 <= (r ** 2) * 4:
                y_cord = max(
                    y_cord,
                    ans[j] + math.sqrt(4 * (r ** 2) - (nums[j] - nums[i]) ** 2),
                )
        ans.append(y_cord)

    print(" ".join(str(x) for x in ans))


if __name__ == "__main__":
    # Example: run with n = 5
    main(5)