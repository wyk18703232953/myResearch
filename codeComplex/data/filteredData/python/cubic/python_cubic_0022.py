import random
import string as strlib

def main(n: int):
    # 1. 生成规模为 n 的测试数据：由小写字母随机组成的字符串
    s = ''.join(random.choice(strlib.ascii_lowercase) for _ in range(n))

    # 2. 原逻辑：寻找最长重复子串长度
    n = len(s)
    check = True
    for sub_len in range(n - 1, 0, -1):
        for starting_index in range(n - sub_len + 1):
            if s[starting_index:starting_index + sub_len] in s[starting_index + 1:]:
                print(sub_len)
                check = False
                break
        if not check:
            break
    if check:
        print(0)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)