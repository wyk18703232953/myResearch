def main(n):
    # 根据规模 n 生成测试数据：前 n 个正整数
    a = list(range(1, n + 1))
    n = len(a)

    cnt = 0
    for i in range(n):
        f = True
        for j in range(n):
            if i == j:
                continue
            if a[i] % a[j] == 0:
                f = False
        if f:
            cnt += 1

    # print(cnt)
    pass
if __name__ == "__main__":
    # 示例调用：可修改 n 测试
    main(10)