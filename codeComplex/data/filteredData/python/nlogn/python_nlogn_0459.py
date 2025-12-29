import math
import copy
import random

def dtb(n):
    return bin(n).replace("0b", "")

def btd(n):
    return int(n, 2)

def main(n):
    # 1. 生成规模为 n 的测试数据
    # 随机生成 kk (1 <= kk <= n)
    kk = random.randint(1, n)
    # 随机生成数组 a，元素范围可自己调整
    a = [random.randint(1, 1000) for _ in range(n)]

    # 2. 原逻辑开始
    c = copy.copy(a)
    a.sort(reverse=True)
    b = []
    f = []
    ans = 0

    # 选出最大的 kk 个数的和
    for i in range(kk):
        ans += a[i]
        b.append(a[i])

    count = 1
    x = 0
    y = 0

    # 在原顺序 c 中找到这 kk 个数的分割点
    for i in range(n):
        if len(f) == (kk - 1):
            y = i
            break
        if c[i] in b:
            f.append(i - x + 1)
            x = i + 1
            b.remove(c[i])

    f.append(n - y)

    # 3. 输出结果
    print(ans)
    for i in f:
        print(i, end=" ")
    print()

if __name__ == "__main__":
    # 可以在此指定 n 的规模
    main(10)