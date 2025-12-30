import random

def main(n):
    # 3. 生成规模为 n 的测试数据，这里用随机非负整数
    # 你可以根据需要自行调整数据生成范围和规则
    a = [random.randint(0, 10**9) for _ in range(n)]

    d = set()
    t = {}
    rep = set()

    if a.count(0) >= 2:
        print("cslnb")
        return

    for i in a:
        if i in d:
            if t[i] + 1 == 3:
                print("cslnb")
                return
            else:
                t[i] += 1
                rep.add(i)
                if len(rep) >= 2:
                    print("cslnb")
                    return
        else:
            t[i] = 1
            d.add(i)

    if rep:
        for c in rep:
            if c - 1 in d:
                print("cslnb")
                return

    s = 0
    a.sort()
    for i in range(n):
        s += a[i] - i

    if s % 2 == 1:
        print("sjfnb")
    else:
        print("cslnb")


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)