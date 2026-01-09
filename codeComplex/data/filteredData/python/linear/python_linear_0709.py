def main(n):
    # 生成确定性的字符串 s，长度为 n
    # 使用交替的 '+' 和 '-' 模式
    s = ''.join('+' if i % 2 == 0 else '-' for i in range(n))

    t = 0
    for i in s:
        if i == '+':
            t += 1

        else:
            t = max(t - 1, 0)

    result = max(t, 0)
    return result


if __name__ == "__main__":
    # 示例调用
    # print(main(10))
    pass