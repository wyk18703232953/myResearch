import random

def main(n: int) -> str:
    # 生成测试数据：随机选择 k，保证 0 <= k <= n
    if n < 0:
        raise ValueError("n must be non-negative")
    k = random.randint(0, n)

    # 下面是原始逻辑（去掉 input），用局部变量复制一份
    nn = n
    kk = k

    d = nn - kk
    d = d // 2

    l = []
    while nn > 0:
        i = min(nn, d)
        while i > 0:
            l.append('1')
            i -= 1
            nn -= 1
        if nn > 0:
            l.append('0')
            nn -= 1

    return "".join(l)


if __name__ == "__main__":
    # 示例：调用 main(10)，真实使用时按需调用 main(n)
    print(main(10))