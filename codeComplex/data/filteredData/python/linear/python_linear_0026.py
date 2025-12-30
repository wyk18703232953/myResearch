import random

def main(n: int):
    # 生成测试数据：长度为 n 的整数数组
    # 为保证逻辑能正常运行（存在唯一奇数或唯一偶数），进行特殊构造
    if n < 3:
        # 对于过小的 n，简单构造一个数组并输出 1
        a = [2] * n
        print(1 if n > 0 else 0)
        return

    # 随机决定是生成“唯一偶数”还是“唯一奇数”的场景
    make_unique_even = random.choice([True, False])

    if make_unique_even:
        # 生成 n-1 个奇数和 1 个偶数
        a = [random.randrange(1, 1000, 2) for _ in range(n)]
        unique_pos = random.randrange(n)
        a[unique_pos] = random.randrange(0, 1000, 2)  # 替换为偶数
    else:
        # 生成 n-1 个偶数和 1 个奇数
        a = [random.randrange(0, 1000, 2) for _ in range(n)]
        unique_pos = random.randrange(n)
        a[unique_pos] = random.randrange(1, 1000, 2)  # 替换为奇数

    # 原逻辑开始
    chet = 0        # 偶数计数
    ne_chet = 0     # 奇数计数
    chet1 = []      # 记录偶数
    ne_chet1 = []   # 记录奇数

    for i in range(len(a)):
        if a[i] % 2 == 0:
            chet += 1
            chet1.append(a[i])
        else:
            ne_chet += 1
            ne_chet1.append(a[i])
        if chet >= 1 and ne_chet >= 1 and (chet > 1 or ne_chet > 1):
            break

    if chet == 1:
        print(a.index(chet1[0]) + 1)
    elif ne_chet == 1:
        print(a.index(ne_chet1[0]) + 1)


if __name__ == "__main__":
    # 示例：调用 main，规模为 10
    main(10)