import random

def main(n: int):
    # 生成 1..n 的随机排列作为测试数据
    a = [0] + random.sample(range(1, n + 1), n)  # a[1..n] 为排列

    d = {}
    for i in range(1, n + 1):
        d[a[i]] = i

    ans = 0
    for i in range(1, n + 1):
        if a[i] != i:
            ind1 = d[a[i]]
            ind2 = d[i]
            va1 = a[i]
            val2 = i
            a[ind1], a[ind2] = a[ind2], a[ind1]
            d[i] = i
            d[va1] = ind2
            ans += 1

    if (3 * n - ans) % 2 == 0:
        print("Petr")
    else:
        print("Um_nik")


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)