# 1029A

def fn(string, k):
    maximum_match = 0
    for i in range(1, len(string)):
        if string[:i] == string[-i:]:
            maximum_match = i

    answer = list(string)
    extra = list(string[maximum_match:])
    for _ in range(k - 1):
        answer.extend(extra)

    return ''.join(answer)


def main(n):
    """
    n: 生成测试数据的规模参数（正整数）
    约定：
      - 构造一个长度为 n 的字符串 string，只包含小写字母
      - 构造 k = n（使输出较大，便于测试）
    """
    # 生成一个有前后缀重叠结构的字符串，便于测试 fn 的逻辑
    base = "ab"
    # 让字符串是 base 重复若干次再加一个字符，长度接近 n
    repeat_times = max(1, n // len(base))
    string = (base * repeat_times)[:max(1, n)]
    k = n if n > 0 else 1

    result = fn(string, k)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：当作为脚本直接运行时，用 n = 5 做一个简单演示
    main(5)