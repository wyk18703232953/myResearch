from collections import defaultdict
import random

def main(n: int):
    # 随机生成规模：n 行，m 列（这里简单设定 m = n 或至少为 1）
    m = max(1, n)

    # 随机生成一个 n x m 的 0/1 矩阵，模拟原来的输入数据
    # 你也可以根据需要改成固定构造或其他分布
    res = []
    cnt = defaultdict(int)

    for _ in range(n):
        # 每行生成 m 个 0/1
        A = [random.randint(0, 1) for _ in range(m)]
        res.append(A)
        for j in range(m):
            if A[j]:
                cnt[j] += 1

    # 按原逻辑判断
    valid = False
    for r in res:
        j = [i for i in range(m) if r[i]]
        if j and all(cnt[i] > 1 for i in j):
            valid = True
            break

    print("YES" if valid else "NO")


if __name__ == "__main__":
    # 示例：调用 main(5)，可以根据需要修改或在别处调用 main
    main(5)