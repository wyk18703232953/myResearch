import random

def main(n: int):
    """
    n 作为规模参数，用来控制生成测试数据的范围：
    这里约定：a, b 在 [0, 2^n - 1] 范围内随机生成（n 至少为 1）。
    """

    if n <= 0:
        raise ValueError("n must be positive")

    # 生成测试数据 a, b
    max_val = (1 << n) - 1
    a = random.randint(0, max_val)
    b = random.randint(0, max_val)

    K = 60
    if a == b:
        ans = 0
    else:
        curr = K
        while (b & (1 << curr)) == (a & (1 << curr)) and curr >= 0:
            curr -= 1
        if curr < 0:
            # 所有位都相同
            ans = 0
        else:
            ans = (1 << curr)
            curr -= 1
            lb = False
            ga = False
            for i in range(curr, -1, -1):
                if (b & (1 << i)) == 0 and (a & (1 << i)) == 0:
                    if not lb:
                        ans += (1 << i)
                        ga = True
                    else:
                        ans += (1 << i)
                elif (b & (1 << i)) == 0 and (a & (1 << i)) == 1:
                    ans += (1 << i)
                elif (b & (1 << i)) == 1 and (a & (1 << i)) == 0:
                    if not lb:
                        ans += (1 << i)
                        ga = True
                        lb = True
                    else:
                        ans += (1 << i)
                else:
                    if not lb:
                        ans += (1 << i)
                        lb = True
                    else:
                        ans += (1 << i)

    print(ans)


if __name__ == '__main__':
    # 示例：使用规模 n = 10 运行一次
    main(10)