import math

def main(n):
    # n controls the number of disks; radius is fixed to 1 for determinism
    if n <= 0:
        return []

    # disks_rad: [number_of_disks, radius]
    disks_rad = [n, 1]
    r = disks_rad[1]

    # nums: x-coordinates of disk centers, deterministically spaced
    # Example: 0, 1, 2, ..., n-1
    nums = [i for i in range(disks_rad[0])]

    ans = []
    ans.append(r)
    for i in range(1, disks_rad[0]):
        y_cord = r
        for j in range(i):
            if (nums[i] - nums[j]) ** 2 <= (r ** 2) * 4:
                y_cord = max(
                    y_cord,
                    ans[j]
                    + math.sqrt(
                        4 * (r ** 2) - (nums[j] - nums[i]) ** 2
                    ),
                )
        ans.append(y_cord)

    return ans


if __name__ == "__main__":
    # Example deterministic call for n = 5
    result = main(5)
    # print(" ".join(str(x) for x in result))
    pass