def fun(a, b):
    return (2 * (a + b)) ** 2 / (a * b)

def main(n):
    # 生成测试数据：构造一个长度为 n 的数组，其中有足够的重复元素
    # 这里简单生成从 1 开始的整数，每个数字重复两次，长度至少为 n
    arr = []
    x = 1
    while len(arr) < n:
        arr.extend([x, x])
        x += 1
    a = arr[:n]

    a.sort()
    b = []
    i = 0
    while i < n - 1:
        if a[i] == a[i + 1]:
            b.append(a[i])
            i += 2
        else:
            i += 1

    # 如果没有形成至少一对矩形，直接返回或打印提示
    if len(b) < 2:
        print("Not enough pairs to form a rectangle")
        return

    m = 10 ** 14
    mi = -1
    for i in range(len(b) - 1):
        curr = fun(b[i], b[i + 1])
        if curr < m:
            m = curr
            mi = i

    print(b[mi], b[mi], b[mi + 1], b[mi + 1])


if __name__ == "__main__":
    # 示例调用：规模 n 可自行调整
    main(10)