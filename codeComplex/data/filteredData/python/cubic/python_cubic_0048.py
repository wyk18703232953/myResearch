import random
import string

def main(n: int):
    # 生成长度为 n 的测试字符串：
    # 为了更有可能出现重复子串，这里使用较小的字符集
    alphabet = string.ascii_lowercase[:5]  # 字符集规模可调小以增加重复概率
    s = ''.join(random.choice(alphabet) for _ in range(n))

    # 原始逻辑
    length = len(s)

    for L in range(length - 1, 0, -1):
        substrings = {s[i:i + L] for i in range(length - L + 1)}
        if len(substrings) < length - L + 1:
            print(L)
            break
    else:
        print(0)

if __name__ == "__main__":
    # 示例：规模为 10，可按需修改或在外部调用 main(n)
    main(10)