def main(n: int):
    # 生成规模为 n 的测试数据，这里简单使用 n 自身作为逻辑输入
    # 如需批量测试，可在外层循环多次调用 main 并传入不同 n

    a = [0, 1]
    i = 2
    r = 0
    while r < n:
        r = a[i - 1] + a[i - 2]
        a.append(r)
        i += 1

    l = len(a) - 1
    if n > 3:
        # print(a[l - 4], a[l - 3], a[l - 1])
        pass
    elif n == 3:
        # print(1, 1, 1)
        pass
    elif n == 2:
        # print(0, 1, 1)
        pass
    elif n == 1:
        # print(0, 0, 1)
        pass
    elif n == 0:
        # print(0, 0, 0)
        pass
if __name__ == "__main__":
    # 示例：用若干不同规模 n 进行测试
    for test_n in [0, 1, 2, 3, 5, 10]:
        # print(f"n = {test_n} -> ", end="")
        pass
        main(test_n)