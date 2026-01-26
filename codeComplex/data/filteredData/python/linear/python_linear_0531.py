import string


def main(n):
    # n 表示输入串长度；k 固定为 5（使用 A-E）
    k = 5
    mp = {c: 0 for c in string.ascii_uppercase[:k]}
    # 生成长度为 n 的确定性字符串：循环使用 A-E
    s = ''.join(string.ascii_uppercase[i % k] for i in range(n))
    for ch in s:
        if ch in mp:
            mp[ch] += 1
    result = min(mp.values()) * k
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(10)