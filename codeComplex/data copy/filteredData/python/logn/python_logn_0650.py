def main(n: int):
    # 生成测试数据：令 k 为 1 到 n*(n+1)//2 范围内的某个值
    # 这里选取中间偏上的一个值作为示例
    max_sum = (n * (n + 1)) // 2
    if max_sum == 0:
        # n 为 0 的边界情况
        # print(0)
        pass
        return

    k = (max_sum * 2) // 3  # 示例测试数据，可按需要调整生成方式

    if k == max_sum:
        # print(0)
        pass

    else:
        left = 0
        right = n
        while left < right:
            mid = (left + right) // 2
            candies = (mid * (mid + 1)) // 2
            if candies + mid < k + n:
                left = mid + 1

            else:
                right = mid
        # print(n - left)
        pass
if __name__ == "__main__":
    # 示例：调用 main，规模 n 可在此调整
    main(10)