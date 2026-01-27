def main(n):
    # 生成 n 组测试数据 (n, m, k)，这里给出一种简单的生成方式：
    # 第 i 组数据：n = i, m = 2*i, k = 3*i + 1
    # 你可以根据实际需要更改生成逻辑。
    q = n
    for i in range(1, q + 1):
        ni = i
        mi = 2 * i
        ki = 3 * i + 1

        m = abs(mi)
        nn = abs(ni)
        k = ki

        mx = max(m, nn)
        remaining = k - mx

        if remaining < 0:
            # print(-1)
            pass
        elif m == 0 and nn == 0:
            if k == 1:
                # print(-1)
                pass
            elif k % 2:
                # print(k - 1)
                pass

            else:
                # print(k)
                pass
        elif abs(m - nn) % 2 == 0:
            if remaining % 2 == 0:
                # print(k)
                pass

            else:
                # print(k - 2)
                pass

        else:
            if remaining == 0:
                # print(k - 1)
                pass
            elif remaining % 2 == 0:
                # print(k - 1)
                pass

            else:
                # print(k - 1)
                pass
if __name__ == "__main__":
    # 示例运行：规模 n = 5
    main(5)