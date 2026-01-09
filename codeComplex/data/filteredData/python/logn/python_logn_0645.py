def main(n):
    # 生成测试数据：根据规模 n 构造 n, k
    # 这里设定 k 为一个与 n 有关的值，便于测试
    # 你可以根据需要自行调整生成规则
    N = n
    k = n * (n + 1) // 4  # 示例：约为前 n 项和的一半

    left = -1
    right = int(1e10 - 1)
    f = True

    while right - left > 1:
        mid = (left + right) // 2
        val = (N - mid + 1) * abs(N - mid) // 2 - mid
        if val > k:
            left = mid

        else:
            if val == k:
                # print(round(mid))
                pass
                f = False
                break

            else:
                right = mid

    if f:
        # print(round(left))
        pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(1000)