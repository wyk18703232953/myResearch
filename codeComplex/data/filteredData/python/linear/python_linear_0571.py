from collections import Counter
import random

class Node:
    def __init__(self, val):
        self.val = val
        self.forw = set()
        self.cou = 0

    def __str__(self):
        return f'{self.val} {self.forw} {self.cou}'


def main(n: int):
    # 1. 生成测试数据：构造一个长度为 n-1 的数组，每个元素在 [1, i] 内
    #    保证与原程序的约束兼容（原程序中读取了 n-1 个整数，第 i 个在 [1..i]）。
    if n <= 0:
        return

    if n == 1:
        # 对于 n=1，原程序不会读取第二行数据，这里直接输出结果
        print(1)
        return

    arr_input = [random.randint(1, i) for i in range(1, n)]  # 长度 n-1

    # 2. 原始逻辑开始（移除 input，改用 arr_input）
    arr = [Node(i) for i in range(1, n + 1)]
    c = 2
    for x in arr_input:
        arr[x - 1].forw.add(c)
        c += 1

    dct = Counter()
    lst = [1]
    while len(lst):
        fl = 0
        # 沿着 forw 指针深度优先走一条链
        for i in arr[lst[-1] - 1].forw:
            lst.append(i)
            fl = 1
            break
        if fl:
            arr[lst[-2] - 1].forw.remove(i)
        if not fl:
            if arr[lst[-1] - 1].cou == 0:
                arr[lst[-1] - 1].cou = 1
            dct[arr[lst[-1] - 1].cou] += 1
            k = arr[lst.pop() - 1].cou
            if len(lst):
                arr[lst[-1] - 1].cou += k

    y = 1
    out = []
    for _ in range(n):
        while not dct[y]:
            y += 1
        dct[y] -= 1
        out.append(str(y))
    print(' '.join(out))


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)