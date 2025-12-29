import random

def main(n: int):
    # 生成两行长度为 n 的随机01字符串
    row1 = [random.choice(["0", "1"]) for _ in range(n)]
    row2 = [random.choice(["0", "1"]) for _ in range(n)]
    s = [row1[:], row2[:]]  # 复制以便后续可能修改

    ans = 0
    l = len(s[0])
    i = 0
    while i < l - 1:
        a = (s[0][i], s[0][i + 1], s[1][i], s[1][i + 1])
        if a.count("0") == 4:
            ans += 1
            s[0][i + 1] = "X"
            i += 1
        elif a.count("0") == 3:
            ans += 1
            i += 2
        else:
            i += 1

    print(ans)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)