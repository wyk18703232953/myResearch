import random

def main(n):
    # 生成测试数据
    # 随机生成 x，保证是非负整数，位数控制在 30 位以内
    x = random.randint(0, (1 << 30) - 1)
    # 随机生成长度为 n 的数组 a，元素值控制在 0 ~ (1<<30)-1
    a = [random.randint(0, (1 << 30) - 1) for _ in range(n)]

    s = set(a)
    if len(s) < n:
        print(0)
        return

    for i in a:
        if (i & x) != i and (i & x) in s:
            print(1)
            return
    k = [i & x for i in a]
    if len(set(k)) < n:
        print(2)
    else:
        print(-1)


if __name__ == "__main__":
    # 示例调用，可按需修改 n 的规模
    main(10)