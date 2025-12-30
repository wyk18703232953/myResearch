import random
import string

def main(n: int):
    # 1. 生成规模为 n 的测试字符串 s
    #   这里生成由小写字母组成的随机字符串，长度为 n
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))
    # 如果不希望有换行符，可以去掉下面一行的注释以观察生成的字符串
    # print("Generated s:", repr(s))

    # 2. 保持原逻辑：寻找最长重复子串的长度（子串可重叠）
    # 注意：原代码读入的一行包含末尾换行符，这里不添加换行符，更符合字符串问题的直觉
    # 如果想完全模拟原行为，可以改成：s = s + '\n'

    for ln in range(len(s), 0, -1):        # 子串长度从大到小
        for L in range(len(s) - ln + 1):   # 起始位置
            if s[L:L + ln] in s[L + 1:]:
                print(ln)
                return
    print(0)


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可在其他模块中调用 main(n)
    main(10)