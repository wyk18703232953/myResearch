import random

def main(n: int):
    # 生成测试数据：两行长度为 n 的仅含 '0' 和 '1' 的字符串
    # 可按需修改数据生成策略
    s = [
        [random.choice(['0', '1']) for _ in range(n)],
        [random.choice(['0', '1']) for _ in range(n)]
    ]

    cnt = 0
    for i in range(n - 1):
        if s[0][i] == s[1][i] == s[0][i + 1] == "0":
            cnt += 1
            s[0][i] = s[1][i] = s[0][i + 1] = "X"
        elif s[0][i] == s[1][i] == s[1][i + 1] == "0":
            cnt += 1
            s[0][i] = s[1][i] = s[1][i + 1] = "X"
        elif s[0][i] == s[1][i + 1] == s[0][i + 1] == "0":
            cnt += 1
            s[0][i] = s[1][i + 1] = s[0][i + 1] = "X"
        elif s[0][i + 1] == s[1][i] == s[1][i + 1] == "0":
            cnt += 1
            s[0][i + 1] = s[1][i] = s[1][i + 1] = "X"

    print(cnt)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)