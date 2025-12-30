import random

def main(n: int):
    # 1. 生成一棵树：n 个节点，节点编号 1..n
    # 使用随机生成的树结构（父节点 < 子节点）
    d = {}
    for v in range(2, n + 1):
        u = random.randint(1, v - 1)
        d.setdefault(u, []).append(v)
        d.setdefault(v, []).append(u)

    # 2. 生成一个随机排列作为 array
    array = list(range(1, n + 1))
    random.shuffle(array)

    # 原逻辑
    flag = 0

    if array[0] == 1:
        i = 1
        j = 0
        while j < n and i < n:
            if array[i] in d.get(array[j], []):
                i += 1
            else:
                j += 1
        if j == n and i != n:
            flag = 1
    else:
        flag = 1

    if flag == 1:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)