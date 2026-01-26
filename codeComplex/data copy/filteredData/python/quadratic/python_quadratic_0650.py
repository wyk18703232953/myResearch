def main(n):
    if n <= 0:
        # print(0)
        pass
        return

    # 确定性生成输入数组 a，模拟原来从 input 读取的一行 n 个整数
    # 这里使用简单的算术构造，确保可重复且规模由 n 控制
    a = [i // 2 + 1 for i in range(n)]
    a = sorted(a)

    counter = 0
    test = [False] * n
    for j in range(n):
        if not test[j]:
            for i in range(n):
                if not test[i] and a[i] % a[j] == 0:
                    test[i] = True
            counter += 1
    # print(counter)
    pass
if __name__ == "__main__":
    main(10)