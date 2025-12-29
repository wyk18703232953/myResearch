import bisect
import random

def main(n):
    # 1. 生成规模为 n 的数组 a
    # 为了方便，可以让数组值在 [1, 10] 范围内
    a = [random.randint(1, 10) for _ in range(n)]

    # 2. 设置查询次数 q，并生成查询数组 qu
    # 这里令 q = n，查询值也在 [1, 10] 范围
    q = n
    qu = [random.randint(1, 10) for _ in range(q)]

    # 3. 以下为原逻辑（去掉 input 版本）

    pre = []
    s = 0
    for i in a:
        s += i
        pre.append(s)

    lost = 0
    val_lost = 0
    ans = []

    for i in qu:
        val = i + val_lost
        b = bisect.bisect_left(pre, val, lost, n)
        val_lost = min(val, pre[-1])
        if b == n:
            lost = 0
            val_lost = 0
            ans.append(n)
            continue
        if pre[b] == val:
            lost = b + 1
        else:
            lost = b
        if lost == n:
            lost = 0
            val_lost = 0
        ans.append(n - lost)

    # 输出结果（可根据需要改为返回 ans）
    for x in ans:
        print(x)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)