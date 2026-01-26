#!/usr/bin/python3
def main(n):
    # 生成一个确定性的字符串，长度为 n
    # 使用小写字母循环生成
    if n <= 0:
        s = ""

    else:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        s = "".join(alphabet[i % 26] for i in range(n))

    for i in range(len(s), 0, -1):
        if s[:i] != s[i-1::-1]:
            # print(i)
            pass
            break

    else:
        # print(0)
        pass
if __name__ == "__main__":
    main(10)