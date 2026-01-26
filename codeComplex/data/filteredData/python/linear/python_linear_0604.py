def main(n):
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
    # print(res)
    pass
if __name__ == "__main__":
    # 示例：使用 n = 10 作为输入规模
    main(10)