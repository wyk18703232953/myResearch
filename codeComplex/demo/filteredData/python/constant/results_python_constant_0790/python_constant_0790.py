def is_square(x):
    sq = int(x**0.5)
    return sq * sq == x


def main(n):
    # 生成 n 组测试数据：第 i 组数据为 i+1
    test_cases = [i + 1 for i in range(n)]

    results = []
    for val in test_cases:
        if ((val % 2 == 0 and is_square(val // 2))
                or (val % 4 == 0 and is_square(val // 4))):
            results.append("YES")

        else:
            results.append("NO")

    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(10)