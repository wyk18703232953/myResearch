def main(n):
    # Generate deterministic nums of length n
    nums = [(i + 1) * 2 for i in range(n)]
    ans = 10 ** 12
    for idx, num in enumerate(nums):
        dist = max(idx, n - idx - 1)
        if dist == 0:
            continue
        curr = num // dist
        if curr < ans:
            ans = curr
    return ans


if __name__ == "__main__":
    # Example deterministic call
    # print(main(10))
    pass