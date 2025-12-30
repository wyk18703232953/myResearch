import random

def main(n: int) -> None:
    # 生成规模为 n 的测试数据，这里生成 1~10*n 范围内的随机整数
    A = [random.randint(1, 10 * n) for _ in range(n)]

    A.sort()
    B = [0] * n
    ans = 0
    for i in range(n):
        if B[i] == 0:
            ans += 1
            B[i] = 1
            for j in range(n):
                if A[j] % A[i] == 0:
                    B[j] = 1
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)