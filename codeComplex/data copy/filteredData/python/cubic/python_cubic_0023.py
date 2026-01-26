def main(n):
    # 根据 n 生成确定性的字符串 s
    # 使用循环周期为 26 的小写字母序列
    if n <= 0:
        s = ""

    else:
        s = "".join(chr(ord('a') + (i % 26)) for i in range(n))

    length = len(s)
    answer = []
    for i in range(0, length):
        for j in range(i + 1, length + 1):
            k = s[i:j]
            co = 0
            for u in range(0, length):
                if s[u:].startswith(k):
                    co += 1
            if co >= 2:
                answer.append(len(k))
    if len(set(s)) == length:
        # print('0')
        pass

    else:
        # print(max(answer))
        pass
if __name__ == "__main__":
    main(100)