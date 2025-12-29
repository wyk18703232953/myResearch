import random

def main(n: int):
    # 1. 生成测试数据 a：长度为 n 的字符串列表，每个为 "x0".."x{n-1}"
    a = [f"x{i}" for i in range(n)]

    # 2. 生成查询序列 s_list：长度也为 n，可随机从 a 中抽取，允许重复与不存在的元素
    #   这里构造方式：
    #   - 一半必定是来自 a 的元素
    #   - 一半可能是不存在于 a 中的元素
    in_a = [random.choice(a) for _ in range(n // 2)]
    not_in_a = [f"y{i}" for i in range(n - n // 2)]
    s_list = in_a + not_in_a
    random.shuffle(s_list)

    # 原始逻辑开始
    d = {}
    k = 0
    for i in range(len(a)):
        d[a[i]] = i

    out = []
    for s in s_list:
        if d.get(s, -1) != -1:
            c = d[s]
            out.append(str(c - k + 1))
            for i in range(k, c + 1):
                d[a[i]] = -1
            k = c + 1
        else:
            out.append("0")

    print(" ".join(out))


if __name__ == "__main__":
    # 示例：n = 10
    main(10)