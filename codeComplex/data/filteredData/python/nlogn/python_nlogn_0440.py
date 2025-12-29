import random

def gC(m, a):
    n = len(a)
    s = [0 for _ in range(2 * n + 1)]
    curr = n
    res = 0
    s[curr] = 1
    ad = 0
    for i in range(n):
        if a[i] < m:
            curr -= 1
            ad -= s[curr]
        else:
            ad += s[curr]
            curr += 1
        res += ad
        s[curr] += 1
    return res

def main(n):
    # 生成规模为 n 的测试数据
    # 数组元素范围自行设定，如 1 到 100
    a = [random.randint(1, 100) for _ in range(n)]
    # m 可以选择为中位数附近的值，这里简单取 50
    m = 50

    result = gC(m, a) - gC(m + 1, a)
    print(result)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)