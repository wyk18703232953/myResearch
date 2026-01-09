def main(n):
    # 生成测试数据：t组测试，每组 (n, k)
    # 这里令 t = n，k 从 1 到 n 生成一些分散的值
    tests = []
    t = n
    for i in range(1, t + 1):
        ni = i  # 测试中使用的 n
        # 生成一个相对多样的 k
        if ni <= 5:
            ki = ni  # 小 n 时，k 取和 n 相同

        else:
            # 取几个典型值：中等、较大、很大
            if i % 3 == 1:
                ki = ni // 2 + 1
            elif i % 3 == 2:
                ki = ni

            else:
                ki = 4 * ni
        tests.append((ni, ki))

    # 按原逻辑处理并输出
    for n, k in tests:
        if n == 1:
            ans = 'YES 0' if k == 1 else 'NO'
        elif n == 2:
            if k <= 2:
                ans = 'YES 1'
            elif k == 3 or k > 5:
                ans = 'NO'

            else:
                ans = 'YES 0'
        elif n <= 32 and k > (4 ** n - 1) // 3:
            ans = 'NO'

        else:
            c, x = 0, n
            p2 = 2
            while x > 0:
                if c + p2 - 1 > k:
                    break
                c += p2 - 1
                x -= 1
                p2 *= 2
            ans = 'YES %d' % (x,)
        # print(ans)
        pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)