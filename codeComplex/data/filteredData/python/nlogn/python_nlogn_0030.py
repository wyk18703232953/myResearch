import random

def main(n: int):
    # 生成测试数据：n 个 1~10^9 范围内的随机整数
    arr = [random.randint(1, 10**9) for _ in range(n)]
    s = " ".join(map(str, arr))

    # 原逻辑开始
    L = s.split(" ")
    L = list(set(L))
    for i in range(len(L)):
        L[i] = int(L[i])
    L = sorted(L)
    if len(L) == 1:
        print("NO")
    else:
        print(L[1])

if __name__ == "__main__":
    # 示例：调用 main(n)，这里可以修改 n 的大小
    main(5)