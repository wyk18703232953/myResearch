import random

def qtd(u):
    ans = 0
    while u > 0:
        u //= 10
        ans += 1
    return ans


def digitos(u):
    ans = 0
    while u > 0:
        ans += u % 10
        u //= 10
    return ans


def main(n):
    """
    n: 问题规模，用来生成测试数据。
       这里生成：
       - m 为 [1, n] 内随机整数
       - number 为 [m, m + 10*n] 内随机整数
    """
    if n <= 0:
        return 0

    # 生成测试数据
    m = random.randint(1, n)
    number = random.randint(m, m + 10 * n)

    ans = 0
    size_n = qtd(m)
    i = m

    while i < m + (size_n * 9) + 1:
        if i > number:  # n não pode ser maior que m
            break
        if i - digitos(i) >= m:  # verificar digitos
            ans += 1
        i += 1

    if i > number:
        print(ans)
        return ans
    else:
        res = number - i + 1 + ans
        print(res)
        return res


if __name__ == "__main__":
    # 示例：规模 n = 100
    main(100)