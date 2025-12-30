from random import randint

def main(n):
    # 生成一个随机排列 pi，长度为 n
    pi = list(range(1, n + 1))
    # 打乱 pi
    for i in range(n - 1, 0, -1):
        j = randint(0, i)
        pi[i], pi[j] = pi[j], pi[i]

    if n == 1:
        print(1)
        return

    ai = [1] * (n + 1)
    ai[0] = 10 ** 9
    for i in pi:
        ai[i] = 0
    for i in range(n - 2, -1, -1):
        ai[pi[i]] += ai[i + 2]
    ai.sort()
    for i in range(n):
        print(ai[i], end=" ")
    print()


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)