import random

def main(n):
    # 根据 n 生成测试数据
    # 生成 m（额外参数，原代码中并未使用，因此这里仅生成占位）
    m = random.randint(1, max(1, n * 2))

    # 生成数组 a，长度为 n，元素为 1~10 之间的随机整数
    a = [random.randint(1, 10) for _ in range(n)]

    c = sum(a)
    if n == 1:
        print(0)
        return

    a.sort()
    res = 0
    pocl = a[n - 1]
    f = False
    for i in range(n - 2, -1, -1):
        if pocl > 1:
            if a[i] >= pocl:
                res += 1
                pocl -= 1
                res += (a[i] - 1)
            else:
                f = True
                pocl = a[i]
                res += 1
                res += (a[i] - 1)
                pocl -= 1
        elif pocl == 1:
            if f:
                res += 1
            res += (a[i] - 1)
            pocl -= 1
        else:
            res += (a[i] - 1)
    print(res)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可在此修改
    main(5)