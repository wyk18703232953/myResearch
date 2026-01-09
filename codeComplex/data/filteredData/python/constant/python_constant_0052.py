def main(n):
    c = 0
    lst = [4, 7, 47, 74, 447, 474, 744, 477, 747, 774]
    results = []
    # 将原来的单次输入扩展为 n 次规模化测试：测试 1..n
    for x in range(1, n + 1):
        if x in lst:
            results.append("YES")

        else:
            for i in lst:
                if x % i == 0:
                    results.append("YES")
                    c = c + 1
                    break

            else:
                results.append("NO")
    # 为避免超大量打印，这里仅返回最后一个结果和 YES 计数
    # 若需要完整输出，可改为逐行打印 results
    # print(results[-1] if results else "NO")
    pass
    # print(c)
    pass
if __name__ == "__main__":
    main(1000)