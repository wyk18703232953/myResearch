S = None

def main(n):
    global S
    # 确定性生成长度为 n 的字符串，由小写字母周期构成
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if n <= 0:
        S = ""

    else:
        S = "".join(alphabet[i % len(alphabet)] for i in range(n))

    ans = 0
    met = set()

    for i in range(len(S)):
        for j in range(i, -1, -1):
            if S[j:i+1] in met:
                ans = max(ans, i - j + 1)

            else:
                met.add(S[j:i+1])

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的大小
    main(10)