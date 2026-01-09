def main(n):
    # 映射输入结构：
    # 原程序：n, k 和字符串 s
    # 这里：k = min(n, 26)，s 为前 n 个小写字母循环生成的字符串
    k = n if n <= 26 else 26
    # 构造长度为 n 的字符串，只使用前 26 个字母循环
    s = ''.join(chr(ord('a') + (i % 26)) for i in range(n))

    a = [0] * 26
    for ch in s:
        a[ord(ch) - ord('a')] = 1

    ans = 0
    i = 0
    result = None
    while i < 26:
        if a[i] > 0:
            ans += i + 1
            k -= 1
            i += 1
            if k == 0:
                result = ans
                break
        i += 1

    else:
        result = -1

    return result


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的大小进行实验
    for n in [1, 5, 10, 26, 30]:
        # print(n, main(n))
        pass