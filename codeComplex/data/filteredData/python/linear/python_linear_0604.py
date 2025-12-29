def main(n: int):
    # 根据 n 生成测试数据，这里直接使用传入的 n 作为规模
    k = n // 3
    ans = []
    for i in range(k):
        ans.append((0, 2 * i))
        ans.append((1, 2 * i + 1))
        ans.append((2, 2 * i))
    for i in range(n % 3):
        ans.append((-1000, -1000 + i))

    res = ""
    for i in ans:
        res += " ".join(map(str, i)) + "\n"
    print(res)


if __name__ == "__main__":
    # 示例：可在此处指定规模 n 进行测试
    main(10)