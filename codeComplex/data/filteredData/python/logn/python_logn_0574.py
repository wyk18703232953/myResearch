def main(n):
    # 使用 n 作为原始程序中的 k，模拟测试数据
    k = n
    k -= 1

    c = 9
    s = 1
    while k >= c * s:
        k -= c * s
        c *= 10
        s += 1

    num = 10 ** (s - 1) + k // s
    idx = k % s
    # print(str(num)[idx])
    pass
if __name__ == "__main__":
    # 示例：可以修改这里的 n 来进行不同规模的测试
    main(1000)