def main(n):
    # 映射规则：
    # 使用 n 生成一对整数 (a, b)，并保证 a <= b 且区间有一定规模
    # 设 a = n，b = 2n（当 n >= 1 时），这样区间长度随 n 线性增长
    if n < 1:
        # 对于非正规模，直接返回不做任何输出
        return

    a = n
    b = 2 * n

    if max(a, b) - min(a, b) + 1 <= 2:
        # print(-1)
        pass
    elif max(a, b) - min(a, b) + 1 == 3:
        if a % 2 == 1 and b % 2 == 1:
            # print(-1)
            pass

        else:
            m = min(a, b)
            # print(m, m + 1, m + 2)
            pass

    else:
        ans = 0
        for i in range(a, b + 1):
            if i % 2 == 0:
                ans = i
                break
        # print(ans, ans + 1, ans + 2)
        pass
if __name__ == "__main__":
    main(10)