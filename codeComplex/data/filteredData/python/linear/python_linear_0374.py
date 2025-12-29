import random

def main(n: int):
    # 生成长度为 n 的随机仅含 '0','1','2' 的字符串
    s = ''.join(random.choice('012') for _ in range(n))

    one = s.count('1')
    zero = 0
    ind = -1
    for i in range(len(s)):
        if s[i] == '2':
            ind = i
            break
        if s[i] == '0':
            zero += 1

    d = ""
    if ind == -1:
        print("0" * zero + "1" * one)
        return

    d = d + "0" * zero + "1" * one
    for i in s[ind:]:
        if i != '1':
            d += i
    print(d)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)