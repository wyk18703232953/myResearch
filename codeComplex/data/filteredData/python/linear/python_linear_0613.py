import random

def main(n):
    # 1. 生成测试数据
    # A 为 1..n 的一个随机排列
    A = list(range(1, n + 1))
    random.shuffle(A)
    # B 为 1..n 的另一个随机排列
    B = list(range(1, n + 1))
    random.shuffle(B)

    # 2. 原逻辑
    REVA = [None] * (n + 1)
    for i in range(n):
        REVA[A[i]] = i + 1

    top = 0
    ANSLIST = []

    for b in B:
        if REVA[b] > top:
            ANSLIST.append(REVA[b] - top)
            top = REVA[b]
        else:
            ANSLIST.append(0)

    # 3. 输出结果
    for ans in ANSLIST:
        print(ans, end=" ")

if __name__ == "__main__":
    # 示例：调用 main(5) 或按需修改规模
    main(5)