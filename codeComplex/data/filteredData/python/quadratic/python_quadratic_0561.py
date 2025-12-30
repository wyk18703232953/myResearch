import sys
import random

def main(n: int):
    # 根据规模 n 生成 N 和 M，这里简单设定 N = n, M = n
    N = n
    M = n

    Ans = [(0, 0) for _ in range(N * M)]
    for i in range(1, N * M + 1):
        if i % 2:
            a, b = divmod(i // 2, M)
        else:
            a, b = divmod(N * M - i // 2, M)
        Ans[i - 1] = ' '.join((str(a + 1), str(b + 1)))

    for a in Ans:
        sys.stdout.write(f'{a}\n')


if __name__ == "__main__":
    # 示例：可以在这里调用 main 进行简单测试
    # 随机给一个规模 n（例如 1~10），实际使用时请在外部调用 main(n)
    n = random.randint(1, 10)
    main(n)