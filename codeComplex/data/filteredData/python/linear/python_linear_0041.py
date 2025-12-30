from collections import Counter
import random

def main(n):
    # 生成测试数据
    # 随机生成 k，1 <= k <= min(n, 10)
    k = random.randint(1, max(1, min(n, 10)))
    # 生成数组 a，长度为 n，元素在 1..(k+2) 之间
    a = [random.randint(1, k + 2) for _ in range(n)]

    # 原程序逻辑开始
    d = {}
    r = l = -2

    # 找到第一个使得不同元素个数达到 k 的位置 r
    for i in range(n):
        d[a[i]] = d.get(a[i], 0) + 1
        if len(d) == k:
            r = i
            break

    # 若无法达到 k 个不同元素，则输出 -1 -1
    if r == -2:
        print(-1, -1)
        return

    # 从左边收缩到第一个可以删除到只出现一次的元素位置 l
    for i in range(r + 1):
        if d[a[i]] == 1:
            l = i
            break
        d[a[i]] -= 1

    print(l + 1, r + 1)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可根据需要调整
    main(10)