import random

def main(n):
    # 生成规模为 n 的测试数据，这里随机生成整数数组 A
    # 可根据需要调整数据范围
    A = [random.randint(-10**9, 10**9) for _ in range(n)]

    # 原逻辑开始
    if n == 1:
        if A[0] >= 0:
            print(A[0])
        else:
            print(-A[0] - 1)
        return

    for i in range(n):
        if A[i] < 0:
            pass
        else:
            A[i] = -A[i] - 1

    if n % 2 == 0:
        print(*A)
        return

    mim = 0
    indmim = 0
    for i in range(n):
        if A[i] < mim:
            mim = A[i]
            indmim = i
    A[indmim] = -A[indmim] - 1
    print(*A)


if __name__ == "__main__":
    # 示例：调用 main(5)，可自行修改 n
    main(5)