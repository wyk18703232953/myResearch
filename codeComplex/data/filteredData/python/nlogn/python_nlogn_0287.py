import random

def main(n):
    # 生成规模为 n 的测试数据
    # 为了更有意义，这里假设第二组数据规模 m 也为 n
    m = n

    # 生成不重复的键，防止覆盖影响规模
    # 第一组键：从 1 到 2n 中随机选 n 个
    keys_a = random.sample(range(1, 2 * n + 1), n)
    # 第二组键：从 1 到 2n 中随机选 m 个
    keys_b = random.sample(range(1, 2 * n + 1), m)

    dicta = {}
    dictb = {}

    # 为每个键生成随机值
    for a in keys_a:
        x = random.randint(1, 100)
        dicta[a] = x

    for b in keys_b:
        y = random.randint(1, 100)
        dictb[b] = y

    # 以下为原逻辑
    ans = 0
    # 注意：遍历过程中删除 dictb 的键是安全的，只要不遍历 dictb 本身
    for i in list(dicta.keys()):
        if i in dictb:
            ans += max(dicta[i], dictb[i])
            del dictb[i]
        else:
            ans += dicta[i]
    for v in dictb.values():
        ans += v

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)