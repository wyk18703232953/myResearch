def main(n):
    # 这里根据 n 生成一个 k，保证 0 <= k <= 2*(n-2)
    # 可以按需要修改生成策略
    k = min(2 * (n - 2), max(0, n))  # 示例：k 与 n 同阶，可自行调整

    if k % 2 == 0:
        # print("YES")
        pass
        # print('.' * n)
        pass
        # print('.' + '#' * (k // 2) + '.' * (n - 1 - k // 2))
        pass
        # print('.' + '#' * (k // 2) + '.' * (n - 1 - k // 2))
        pass
        # print('.' * n)
        pass

    else:
        # print("YES")
        pass
        # print('.' * n)
        pass

        if k <= n - 2:
            # print('.' * ((n - k) // 2) + '#' * k + '.' * ((n - k) // 2))
            pass
            # print('.' * n)
            pass

        else:
            # print('.' + '#' * (n - 2) + '.')
            pass
            # 根据原式整理：中间的点数为 (2n - 4 - k)
            mid_dots = 2 * n - 4 - k
            left_hash = (k - n + 2) // 2
            right_hash = left_hash
            print(
                '.' +
                '#' * left_hash +
                '.' * mid_dots +
                '#' * right_hash +
                '.'
            )
        # print('.' * n)
        pass
if __name__ == "__main__":
    # 示例调用：可修改 n 测试不同规模
    main(7)