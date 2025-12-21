import math
import random

def main(n):
    disks_rad = [n, max(1, n // 10)]
    nums = sorted(random.sample(range(1, n * 10 + 1), n))
    ans = []
    r = disks_rad[1]
    ans.append(r)
    for i in range(1, disks_rad[0]):
        y_cord = r
        for j in range(i):
            if (nums[i] - nums[j]) ** 2 <= (r ** 2) * 4:
                y_cord = max(
                    y_cord,
                    ans[j] + math.sqrt(
                        4 * (r ** 2) - (nums[j] - nums[i]) ** 2
                    ),
                )
        ans.append(y_cord)
    print(" ".join(str(x) for x in ans))
    return ans

if __name__ == "__main__":
    main(10)