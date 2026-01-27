def main(n: int):
    # 根据规模 n 生成一个测试用的数字字符串 s
    # 这里简单地用从 1 到 n 的数字拼接，例如 n=5 -> "12345"
    if n <= 0:
        return
    s = ''.join(str(i) for i in range(1, n + 1))

    # 原逻辑：在 s、s 去掉最后一位、s 去掉倒数第二位的基础上求最大整数
    candidates = [s]
    if len(s) >= 2:
        candidates.append(s[:-1])
    if len(s) >= 2:
        candidates.append(s[:-2] + s[-1])

    nums = list(map(int, candidates))
    # print(max(nums))
    pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(5)