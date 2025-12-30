import random

def main(n: int):
    # 1. 生成测试数据
    # 这里根据规模 n 来生成 n, m, k 以及数组 p
    # 可以根据需要调整生成规则
    #
    # 约定：
    #   n: 数组长度
    #   m: 最大值范围（取 n 的若干倍）
    #   k: 每一块的“页大小”，至少为 1
    #
    # 为了与原题逻辑相符，p 为 1..m 范围内的随机递增位置
    if n <= 0:
        return

    m = n * 5                # 最大位置
    k = max(1, n // 3)       # 块大小

    # 生成一个严格递增的数组 p，长度为 n，元素在 [1, m]
    p = sorted(random.sample(range(1, m + 1), n))

    # 2. 原始逻辑（去除 input，封装到 main 里）
    reduced = 1
    p = p[:]      # 复制以防副作用
    p.reverse()
    cnt = 0

    while len(p):
        cnt1 = 1
        first = p.pop()
        fack = ((first - reduced) // k) * k
        while len(p) and p[-1] - fack - reduced < k:
            cnt1 += 1
            p.pop()
        reduced += cnt1
        cnt += 1

    # 3. 输出结果（以及可选的测试数据，若只想要结果，可以只 print(cnt)）
    print(cnt)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)