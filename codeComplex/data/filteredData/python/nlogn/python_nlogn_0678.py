import random

def main(n, m=None, seed=0):
    """
    n: 规模，用于生成测试数据
    m: 第二个参数规模，如不指定则设为 n
    seed: 随机种子，保证可复现
    """
    if m is None:
        m = n

    random.seed(seed)

    # 生成测试数据：
    # b 长度为 n，g 长度为 m，取值范围自行设定为 [1, 100]
    b = [random.randint(1, 100) for _ in range(n)]
    g = [random.randint(1, 100) for _ in range(m)]

    # 原始逻辑
    ans = 0
    # 需要至少两个元素才能取倒数第二大和最大
    if n < 2:
        # 不满足原始算法的前提条件时，这里直接输出 -1
        # 或者根据需要改为其他逻辑
        print(-1)
        return

    maxb2, maxb = sorted(b)[-2:]
    ming = min(g)
    if maxb > ming:
        ans = -1
    else:
        ans += sum(b) * m
        ans += (sum(g) - ming) - (maxb * (m - 1))
        if ming > maxb:
            ans += ming - maxb2
    print(ans)


if __name__ == "__main__":
    # 示例：规模 n=5, m 不传则等于 n
    main(5)