import sys

def main(n):
    if n <= 0:
        # print(0)
        pass
        return
    # 生成确定性的字符串 s，长度为 n，在小写字母中循环
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    m = len(alphabet)
    s = "".join(alphabet[i % m] for i in range(n))

    c = set(s)
    ln = [0] * n
    INF = 10**9
    for d in c:
        last = -1
        for i, v in enumerate(s):
            if v == d:
                last = i
            if last == -1:
                ln[i] = INF

            else:
                ln[i] = max(ln[i], i - last + 1)
    # print(min(ln))
    pass
if __name__ == "__main__":
    # 示例：使用 n = 10 作为输入规模
    main(10)