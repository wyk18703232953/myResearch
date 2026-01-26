def main(n):
    # 根据规模 n 生成测试数据：这里构造一个与 n 同数量级的 s
    # 可根据需要调整生成策略
    s = n

    x, y = divmod(s, 9)
    if not s:
        x = 0
    elif y:
        x += 1
    low = x * 9
    for i in range(low, low + 10000):
        if i - sum(int(c) for c in str(i)) >= s:
            low = i
            break
    result = max(n - low + 1, 0)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：调用 main，规模可在此处修改
    main(10**6)