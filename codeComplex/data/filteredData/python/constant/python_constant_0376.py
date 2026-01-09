def main(n):
    # 映射规则：
    # a, b, c 与 n 成比例，使规模随 n 线性增长并保持确定性
    a = n // 2
    b = n // 3
    c = n // 4

    # 保证至少有 1 的空间让表达式可能为正
    total_n = a + b - c + 1

    # 原始逻辑
    if total_n - a - b + c >= 1:
        if a < c or b < c:
            # print(-1)
            pass

        else:
            # print(total_n - a - b + c)
            pass

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    main(10)