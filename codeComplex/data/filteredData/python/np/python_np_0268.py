import random

mod = 10**9 + 7

def bit(n):
    if n == 0:
        return 0
    val = 1
    while (val & n) == 0:
        val *= 2
    return val

def main(n):
    """
    n: 树规模参数，对应原代码中的 n（树节点数）。
       我们令 q = n，生成 n 个随机查询。
    """
    q = n  # 随机生成 q = n 组查询
    results = []

    for _ in range(q):
        # t1 为 [1, n] 的随机节点编号
        t1 = random.randint(1, n)

        # 随机生成操作串，长度在 0~20 之间，由 'U','L','R' 组成
        length = random.randint(0, 20)
        ops = ''.join(random.choice('ULR') for _ in range(length))

        # 模拟原逻辑
        for j in ops:
            val = bit(t1)

            if j == "U":
                tem = (t1 - val) | (val * 2)
                if tem < n:
                    t1 = tem
            elif j == "L" and val > 1:
                t1 -= val // 2
            elif j == "R" and val > 1:
                t1 += val // 2

        results.append(t1)

    # 输出结果（与原程序行为一致：每个查询最终的 t1 一行一个）
    for ans in results:
        print(ans)


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)