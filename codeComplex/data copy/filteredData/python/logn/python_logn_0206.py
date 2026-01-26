def main(n):
    # 根据规模 n 生成 s，这里简单设为 n 的一半（可按需要调整）
    s = n // 2

    # 按原逻辑在区间 [s, s+180) 中寻找第一个满足条件的数字
    candidates = []
    for i in range(s, s + 180):
        if i - sum(int(j) for j in str(i)) >= s:
            candidates.append(i)

    if candidates:
        first_valid = candidates[0]
        result = max(n - first_valid + 1, 0)

    else:
        result = 0

    # print(result)
    pass
if __name__ == "__main__":
    # 示例：调用 main(1000)，可根据需要修改 n 的值进行测试
    main(1000)