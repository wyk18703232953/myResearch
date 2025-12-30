import random

def main(n):
    # 生成测试数据：
    # n: 列表 a 的长度
    # m: 列表 s 的长度，设为与 n 相同，也可按需调整
    m = n

    # 生成随机正整数数据，保证有解的概率较大
    # a 中元素范围 [1, 100]
    # s 中元素范围 [1, 100]
    a = sorted(random.randint(1, 100) for _ in range(n))
    s = sorted(random.randint(1, 100) for _ in range(m))

    # 原逻辑
    if a[-1] > s[0]:
        ans = -1
    else:
        if a[-1] == s[0]:
            ans = sum(a[:-1]) * m + sum(s)
        else:
            if n >= 2:
                ans = sum(a[:-2]) * m + a[-2] * (m - 1) + sum(s) + a[-1]
            else:
                # 当 n == 1 时，原逻辑中 a[:-2] 和 a[-2] 不合法
                # 这里做一个合理的降级处理（本情况很少用于原题）
                # 仅用原最大值参与计算
                ans = a[-1] * m + sum(s)

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)