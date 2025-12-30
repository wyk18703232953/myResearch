from sys import setrecursionlimit
from random import choice, randint
import time

setrecursionlimit(10 ** 9)
mod = 10 ** 9 + 7
mod2 = 998244353


def main(n):
    """
    n: 规模，用于生成测试数据的字符串长度
    程序逻辑：与原程序相同，尝试通过相邻交换把 s 变为 t，
    若能则输出操作次数和所有操作位置（1-based），否则输出 -1。
    """

    # 1. 根据 n 生成测试数据
    # 字符集可根据需要调整，这里用小写字母
    alphabet = "abc"
    # 保证 n >= 1
    if n <= 0:
        n = 1

    # 生成随机 s
    s = [choice(alphabet) for _ in range(n)]

    # 生成 t：在 s 的基础上做若干随机相邻交换，以保证大概率可达
    t = s[:]
    swap_times = randint(0, n)  # 做一些随机相邻交换
    for _ in range(swap_times):
        if n > 1:
            i = randint(0, n - 2)
            t[i], t[i + 1] = t[i + 1], t[i]

    # 2. 原有逻辑封装
    s_cur = s[:]  # 工作副本
    ans = []
    for i in range(n):
        for j in range(i, n):
            if s_cur[j] == t[i]:
                # 把 s_cur[j] 这个字符通过相邻交换拉到位置 i
                for k in range(j, i, -1):
                    s_cur[k], s_cur[k - 1] = s_cur[k - 1], s_cur[k]
                    ans.append(k)  # 1-based 下标
                break

    # 3. 输出
    if s_cur == t:
        print(len(ans))
        if ans:
            print(" ".join(map(str, ans)))
        else:
            print()
    else:
        print(-1)


if __name__ == "__main__":
    # 示例：运行 main(5)，可自行修改 n 做本地测试
    main(5)