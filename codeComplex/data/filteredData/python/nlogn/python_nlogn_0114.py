import random

def main(n: int):
    # 生成规模为 n 的测试数据，这里生成 1~n 的一个随机排列
    A = list(range(1, n + 1))
    random.shuffle(A)

    B = A.copy()
    B.sort()
    c = 0
    for i in range(n):
        if A[i] != B[i]:
            c += 1
    print("YES" if c <= 2 else "NO")


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)