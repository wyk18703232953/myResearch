import random

def main(n: int):
    # 1. 生成测试数据
    # 生成 n（不同数字种类数）的随机列表 lst
    # 为了保证有重复，先生成 n 个不同值，然后随机重复若干次
    # 同时生成一个 m（目标总数量），模拟原程序中的第二个输入
    distinct_values = list(range(1, n + 1))
    # 每个值重复 1~3 次，整体长度大约在 [n, 3n]
    lst = []
    for v in distinct_values:
        cnt = random.randint(1, 3)
        lst.extend([v] * cnt)
    random.shuffle(lst)
    # m 至少为 0，至多为 len(lst)*2，覆盖多种情况
    m = random.randint(0, len(lst) * 2)

    # 2. 原逻辑开始（去掉 input()，使用生成的 n, m, lst）

    # 注意：原代码中 n, m 的角色是独立的，其中：
    #   - n：需要的“份数”
    #   - m：原本来自输入的某个值，代码中首先与 n 比较
    # 目前生成数据时，我们用参数 n 作为“需要的份数”，
    # m 为随机生成的总量目标值。

    # 重新统计 lst 的频次
    res = list(dict.fromkeys(lst))
    c = []
    for x in res:
        c.append(lst.count(x))

    if m < n:
        print(0)
    elif m == n:
        print(1)
    else:
        m1 = 1
        j = 2
        while True:
            c1 = 0
            for cnt in c:
                c1 += cnt // j
            if c1 >= n:
                m1 = j
                j += 1
            else:
                print(m1)
                break


if __name__ == "__main__":
    # 示例：调用 main，n 为规模参数
    main(10)