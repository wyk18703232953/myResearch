from copy import deepcopy
import random

mo = 10 ** 9 + 7

def main(n):
    # 1) 生成测试数据：随机生成 T 和 n 组 (t, g)
    # 你可以按需要修改数据规模或范围
    T = random.randint(1, 3 * n + 3)  # 总时间 T
    tasks = []
    for _ in range(n):
        t = random.randint(1, 5)      # 每个任务的时间
        g = random.randint(1, 3)      # g ∈ {1,2,3}
        tasks.append((t, g))

    # 2) 原代码逻辑开始（用生成的 T 和 tasks 替代输入）

    di = {(0, 0, 0, T): 1}
    for t, g in tasks:
        an = deepcopy(di)
        for k in an:
            nc = list(k)
            nc[3] -= t
            nc[g - 1] += 1
            if nc[3] >= 0:
                nc = tuple(nc)
                if nc in di:
                    di[nc] += an[k]
                else:
                    di[nc] = an[k]

    nd = {(1, 0, 0, 0): 1, (0, 1, 0, 1): 1, (0, 0, 1, 2): 1}

    def nb(tu):
        if tu not in nd:
            if tu[tu[3]] == 0:
                nd[tu] = 0
            else:
                nt = list(tu)
                nt[tu[3]] -= 1
                nt[3] = (nt[3] + 1) % 3
                nt2 = nt[:]
                nt2[3] = (nt2[3] + 1) % 3
                nd[tu] = (tu[tu[3]] * (nb(tuple(nt)) + nb(tuple(nt2)))) % mo
        return nd[tu]

    ans = sum(
        di[k] * (
            nb(k[:3] + (1,)) +
            nb(k[:3] + (0,)) +
            nb(k[:3] + (2,))
        )
        for k in di
        if k[3] == 0
    ) % mo

    # 返回结果和生成的数据，方便调试或验证
    return {
        "n": n,
        "T": T,
        "tasks": tasks,  # 列表 [(t,g), ...]
        "answer": ans
    }


# 示例：直接运行本文件时做一次调用
if __name__ == "__main__":
    result = main(5)
    print(result["answer"])