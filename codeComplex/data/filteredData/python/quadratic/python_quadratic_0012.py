import math

def generate_input(n):
    # disks_rad: [number_of_disks, radius]
    # nums: x-coordinates of disks
    if n <= 0:
        n = 1
    num_disks = n
    r = n // 3 + 1  # keep radius growing slowly with n
    disks_rad = [num_disks, r]
    # deterministic x-coordinates with some spacing pattern
    # ensure some overlap but not all stacked: use i * (r // 2 + 1)
    step = r // 2 + 1
    nums = [i * step for i in range(num_disks)]
    return disks_rad, nums

def main(n):
    ans = []
    disks_rad, nums = generate_input(n)
    r = disks_rad[1]
    ans.append(r)
    for i in range(1, disks_rad[0]):
        y_cord = r
        for j in range(i):
            if ((nums[i] - nums[j]) ** 2) <= ((r ** 2) * 4):
                y_cord = max(
                    y_cord,
                    ans[j] + math.sqrt(
                        4 * (r ** 2) - (nums[j] - nums[i]) ** 2
                    ),
                )
        ans.append(y_cord)
    print(" ".join(str(x) for x in ans))

if __name__ == "__main__":
    # example deterministic call
    main(10)