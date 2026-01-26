import math

def main(n):
    # 生成确定性的测试数据 a，长度为 n
    # 这里选择一个简单的确定性构造方式
    a = [(i * i + 3 * i + 7) for i in range(n)]

    x = 10**9 + 2
    y = 0
    for i in range(n):
        val = math.ceil((a[i] - i) / n) * n + i + 1
        if x > val:
            x = val
            y = i + 1
    # print(y)
    pass
if __name__ == "__main__":
    main(10)