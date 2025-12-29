import random

def main(n):
    # 生成测试数据
    # 保证 1 <= b <= n，且 1 <= a <= n
    # 为了让区间合理，这里生成 a, b 满足 a + b <= n + 1（与原代码中 n-a+1 有关）
    if n < 2:
        # 对于极小的 n，直接构造一个最小可行例子
        n = 2
    # 随机生成 a, b，使得 1 <= b <= n, 1 <= a <= n, 且有一定概率满足 b <= n - a + 1
    # 为简单起见：固定 a, b，在可行范围内随机
    a = random.randint(1, n)
    b = random.randint(1, n)
    
    # 生成长度为 n 的数组 c，元素随机在 1~100 之间
    c = [random.randint(1, 100) for _ in range(n)]

    # 以下为原始逻辑
    c.sort()
    # 为防止 b-1 越界，这里做一次修正（若测试生成时不保证关系则需防护）
    if b < 1:
        b = 1
    if b > n:
        b = n
    l = c[b - 1]
    r = 0
    ok = False

    # 原循环：for i in range(b, n - a + 1):
    # 为防止 n-a+1 < b 的情况导致 range 为空但仍然兼容逻辑，不做改动
    upper = n - a + 1
    if upper < 0:
        upper = 0  # 防御性处理
    for i in range(b, upper):
        if c[i] > l:
            ok = True
            r = c[i]
            break

    if ok:
        print(r - l)
    else:
        print(0)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)