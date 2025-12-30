from random import randint

def main(n):
    # 生成规模为 n 的测试数据
    # 第一组 m1 个键值对，第二组 m2 个键值对
    # 键的取值范围 [1, 2n]，值的范围 [0, 10^9]
    m1 = n
    m2 = n

    lst1 = {}
    lst2 = {}
    keys_used = set()

    # 生成第一组数据
    for _ in range(m1):
        x = randint(1, 2 * n)
        y = randint(0, 10**9)
        lst1[x] = y
        keys_used.add(x)

    # 生成第二组数据
    for _ in range(m2):
        x = randint(1, 2 * n)
        y = randint(0, 10**9)
        lst2[x] = y
        keys_used.add(x)

    # 按原逻辑计算答案：对每个出现过的键，取两组中该键值的最大值求和
    ans = 0
    for k in keys_used:
        x = lst1.get(k, 0)
        y = lst2.get(k, 0)
        ans += max(x, y)

    print(ans)


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)