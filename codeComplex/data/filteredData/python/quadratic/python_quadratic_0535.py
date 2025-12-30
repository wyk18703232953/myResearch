import random

def main(n):
    # 生成测试数据：
    # n: 类型为 0 的事件数量
    # m: 类型为 1 的事件数量，这里设为 n，规模相同
    m = n
    total = n + m

    # 生成 t：前 n 个为 0，后 m 个为 1，然后打乱顺序
    t = [0] * n + [1] * m
    random.shuffle(t)

    # 生成 x：为每个事件生成一个位置值，这里用 0~(10*n) 的随机整数
    x = [random.randint(0, 10 * n if n > 0 else 10) for _ in range(total)]

    # 原始逻辑开始
    arr = []
    pep = {}

    for i in range(n + m):
        if t[i] == 0:
            arr.append(i)
            pep[x[i]] = 0
        else:
            for j in arr:
                pep[x[j]] = i
            arr = []

    for i in range(n + m - 1, -1, -1):
        if t[i] == 0:
            arr.append(i)
        else:
            for j in arr:
                if abs(x[j] - x[i]) <= abs(x[pep[x[j]]] - x[j]):
                    pep[x[j]] = i
            arr = []

    ans = []
    for i in range(n + m):
        if t[i]:
            ans.append(1)
        else:
            ans.append(0)

    for key in pep:
        ans[pep[key]] += 1

    # 按原程序格式输出：对于非零项输出 i-1，并用空格分隔
    for v in ans:
        if v:
            print(v - 1, end=' ')

if __name__ == "__main__":
    # 示例：调用 main(5)，可根据需要修改规模
    main(5)