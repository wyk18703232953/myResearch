def main(n):
    # 生成测试数据：构造 t 个测试用例，每个用例为 (n_i, k_i)
    # 这里简单设定：
    #   t = n
    #   n_i = i+1
    #   k_i = i+1
    # 你可以根据需要自行调整生成规则
    t = n
    tests = []
    for i in range(t):
        ni = i + 1
        ki = i + 1
        tests.append((ni, ki))

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
        print(ans)


if __name__ == "__main__":
    # 示例运行：规模参数可以在此修改
    main(10)