def main(n):
    # 这里将 n 视为测试用例数量
    # 生成确定性的 (a, b, c) 三元组
    results = []
    for i in range(n):
        a = i
        b = (2 * i + 1)
        c = (3 * i + 2)
        if a > c or b > c:
            results.append(-1)

        else:
            if (a % 2 + b % 2 == 1):
                results.append(c - 1)
            elif (a % 2 == b % 2 == c % 2):
                results.append(c)

            else:
                results.append(c - 2)
    # 为了防止 IO 成为瓶颈，统一输出
    for res in results:
        # print(res)
        pass
if __name__ == "__main__":
    main(10)