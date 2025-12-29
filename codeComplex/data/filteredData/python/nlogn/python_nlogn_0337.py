import random
import string

def main(n: int):
    # 1. 生成测试数据：构造一个长度递增且两两包含的字符串序列
    # 为了能输出 YES，我们生成 s[i] 是 s[i+1] 的子串的序列
    base = ''.join(random.choice(string.ascii_lowercase) for _ in range(max(1, n)))
    strings = []
    cur = ""
    for i in range(n):
        # 每次在当前串基础上附加一点，保证前者是后者的子串
        cur += base[i % len(base)]
        strings.append(cur)

    # 2. 将原逻辑封装到 main 中（包括插入排序与检查）
    s = ['']
    for inp in strings:
        s.append(inp)
        pos = len(s) - 1
        # 使用插入排序按长度非降序排列
        while len(s[pos]) < len(s[pos - 1]):
            s[pos], s[pos - 1] = s[pos - 1], s[pos]
            pos -= 1

    out = 'YES'
    for i in range(n):
        if s[i] not in s[i + 1]:
            out = 'NO'
            s = []
            break

    print(out + '\n'.join(s))


if __name__ == "__main__":
    # 示例：运行规模为 5
    main(5)