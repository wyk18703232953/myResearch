from itertools import accumulate
import random

def main(n: int):
    # 1. 生成测试数据
    # 随机生成 M，并生成 n 个严格递增且小于 M 的整数
    # 保证 A 中元素在 [1, M-1] 且递增
    if n <= 0:
        # 退化情况，直接输出 0
        print(0)
        return

    M = max(2 * n + 1, 10)  # 简单设置一个与 n 相关的上界
    # 从 [1, M-1] 中选 n 个不重复的数并排序
    A = sorted(random.sample(range(1, M), n))

    # 2. 按照原逻辑处理
    A = [0] + A + [M]
    D = []
    for i in range(n + 1):
        D.append(A[i + 1] - A[i])

    E = []
    O = []
    for i, d in enumerate(D):
        if i % 2 == 0:
            E.append(d)
            O.append(0)
        else:
            O.append(d)
            E.append(0)

    CE = [0] + E
    CE = list(accumulate(CE))
    CO = [0] + O
    CO = list(accumulate(CO))

    ans = CE[-1]
    for i in range(n + 1):
        if D[i] == 1:
            continue
        temp = CE[i] + (D[i] - 1) + CO[-1] - CO[i + 1]
        ans = max(ans, temp)

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)