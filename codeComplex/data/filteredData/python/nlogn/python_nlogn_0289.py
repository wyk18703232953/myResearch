import random

def main(n: int):
    # 生成测试数据：
    # n: 第一组 (cf) 的条目数量
    # 第二组 (tc) 的条目数量 m 也与 n 相关，这里设为 n
    m = n

    # 为了让 key 有交集又有差异，构造如下：
    # cf 使用 key: 1..n
    # tc 使用 key: k..k+m-1，其中 k 取 n//2，这样前半段有重叠，后半段有独立部分
    k = max(1, n // 2)

    cf = {}
    tc = {}

    # 为了可重复测试，可以固定随机种子（如不需要可删掉下一行）
    random.seed(0)

    # 生成 cf 的 n 个 (key, value)
    for i in range(1, n + 1):
        value = random.randint(1, 1000)
        cf[i] = value

    # 生成 tc 的 m 个 (key, value)
    for i in range(k, k + m):
        value = random.randint(1, 1000)
        tc[i] = value

    # 原逻辑：对所有出现过的 key，取 cf[key], tc[key] 中存在的最大值求和
    keys_union = set(cf.keys()) | set(tc.keys())
    total = 0
    for key in keys_union:
        v_cf = cf.get(key, 0)
        v_tc = tc.get(key, 0)
        total += max(v_cf, v_tc)

    print(total)


if __name__ == "__main__":
    # 示例：规模为 10，可以根据需要修改或在外部调用 main(n)
    main(10)