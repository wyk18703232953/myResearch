def main(n):
    # n 表示字符串长度
    # 确定性生成由 '+' 和 '-' 组成的字符串
    # 例如：前一半为 '+', 后一半为 '-'
    half = n // 2
    s = '+' * half + '-' * (n - half)

    t = 0
    mn = 0
    for ch in s:
        if ch == '-':
            t -= 1

        else:
            t += 1
        mn = min(mn, t)
    result = -mn + t
    # print(result)
    pass
    return result

if __name__ == "__main__":
    # 示例：使用 n = 10 进行一次确定性实验
    main(10)