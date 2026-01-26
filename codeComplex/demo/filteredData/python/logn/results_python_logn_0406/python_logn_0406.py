def main(n):
    # 解释输入结构：
    # 原程序：
    # t
    # n1 k1
    # n2 k2
    # ...
    # 这里我们用 main(n) 构造 t 组数据
    # 将 t 定义为 n
    t = n

    # 为了体现规模变化，同时保持确定性：
    # 第 i 组用：
    #   ni 在 [1, 60] 周期变化：ni = (i % 60) + 1
    #   ki 为与 ni 相关的一个确定性整数：ki = i*i + ni
    for ca in range(t):
        ni = (ca % 60) + 1
        ki = ca * ca + ni

        if ni >= 40:
            # print("YES " + str(ni - 1))
            pass

        else:
            ans = -1
            for m in range(1, ni + 1):
                asd = (4 ** m - 1) // 3
                asd2 = (2 ** m - 1) ** 2
                asd2 *= (4 ** (ni - m) - 1) // 3
                asd += asd2
                if asd >= ki and m * m <= ki:
                    ans = ni - m
                    break
            if ans == -1:
                # print("NO")
                pass

            else:
                # print("YES " + str(ans))
                pass
if __name__ == "__main__":
    # 示例：用 n=5 运行 5 组数据
    main(5)