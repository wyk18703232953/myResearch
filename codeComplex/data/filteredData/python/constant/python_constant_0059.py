def main(n: int):
    # 预生成斐波那契数列，足够覆盖一般 n 范围
    f0, f1 = 0, 1
    li = [0, 1]
    for _ in range(45):
        f0, f1 = f1, f0 + f1
        li.append(f1)

    x = []
    cur = n
    for _ in range(3):
        for i in range(len(li) - 1, -1, -1):
            if li[i] <= cur:
                cur -= li[i]
                x.append(li[i])
                break

    if cur == 0:
        print(*x, sep=" ")
    else:
        print("I'm too stupid to solve this problem")


if __name__ == "__main__":
    # 根据 n 生成测试数据，这里直接调用 main(n)
    # 可按需要修改测试规模
    test_n = 100
    main(test_n)