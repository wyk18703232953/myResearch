import random

def main(n):
    # 生成测试数据：
    # 选取一个适当的 x（例如不太大的随机数）
    x = random.randint(1, 2 * n + 5)
    # 生成长度为 n 的数组 b，元素范围适度
    b = [random.randint(1, 2 * n + 5) for _ in range(n)]

    # 原始逻辑开始
    d = {}
    flag = 0
    for i in b:
        if d.get(i):
            flag = 1
            break
        else:
            d[i] = 1

    if flag:
        print(0)
    else:
        flag = 0
        c = set()
        for i in b:
            a = i & x
            c.add(a)
            if d.get(a) and a != i:
                flag = 1
                break
        if flag:
            print(1)
        elif len(c) < n and flag == 0:
            print(2)
        else:
            print(-1)

if __name__ == "__main__":
    # 示例：调用 main，规模自行设定
    main(5)