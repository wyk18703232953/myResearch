def main(n):
    # 将 n 映射为原程序中的 n 和 k，以及生成 nums
    # 这里令原 n = n，k = max(1, n // 2)，nums 为长度 n 的确定性递增序列
    orig_n = n
    if orig_n <= 0:
        # print(0)
        pass
        return
    k = orig_n // 2
    if k <= 0:
        k = 1
    nums = [i * 2 for i in range(orig_n)]  # 确定性递增整数序列

    diff = []
    for i, j in zip(nums, nums[1:]):
        diff.append(j - i)

    diff.sort()
    # 防御性处理：当 orig_n - k 可能为负或超过长度时进行裁剪
    take = orig_n - k
    if take < 0:
        take = 0
    if take > len(diff):
        take = len(diff)
    # print(sum(diff[:take]))
    pass
if __name__ == "__main__":
    main(10)