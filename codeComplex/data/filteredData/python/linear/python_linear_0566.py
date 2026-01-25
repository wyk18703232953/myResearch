def main(n):
    if n <= 0:
        return
    # 确定性生成 permutation pi，长度为 n-1，范围 1..n-1
    if n == 1:
        print(1)
        return
    pi = [(i % (n - 1)) + 1 for i in range(n - 1)]

    ai = [1] * (n + 1)
    ai[0] = 10**9
    for i in pi:
        ai[i] = 0
    for i in range(n - 2, -1, -1):
        ai[pi[i]] += ai[i + 2]
    ai.sort()
    for i in range(n):
        print(ai[i], end=" ")
    print()


if __name__ == "__main__":
    main(10)