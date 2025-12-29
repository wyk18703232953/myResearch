import random

def main(n: int):
    # 生成规模为 n 的测试数据（整数数组）
    # 这里生成区间 [0, 1000] 内的随机整数
    a = [random.randint(0, 1000) for _ in range(n)]

    # 以下为原逻辑
    i = a.index(max(a))
    v = True
    for j in range(0, i):
        if a[j] > a[j + 1]:
            v = False
    for j in range(i, n - 1):
        if a[j] < a[j + 1]:
            v = False
    if v is True:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：可自行调整 n
    main(10)