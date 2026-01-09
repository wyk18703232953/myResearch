def main(n):
    # n 表示测试用例数量
    results = []
    for k in range(1, n + 1):
        # 确定性生成 (a, b)，确保都为正整数
        a = k * 2
        b = k * 3 + 1
        c = 0
        x, y = a, b
        while x != 0 and y != 0:
            if x > y:
                c += x // y
                x = x % y
            elif y > x:
                c += y // x
                y = y % x

            else:
                c += 1
                break
        results.append(c)
    return results


if __name__ == "__main__":
    # 示例调用：使用 n=5 运行
    res = main(5)
    for val in res:
        # print(val)
        pass