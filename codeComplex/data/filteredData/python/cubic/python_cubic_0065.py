import random
import string as _string

def main(n: int):
    # 生成长度为 n 的随机小写字母串作为测试数据
    s = ''.join(random.choice(_string.ascii_lowercase) for _ in range(n))
    size = len(s)

    ans_got = 0
    for length in range(1, size)[::-1]:
        seen = {}
        for i in range(0, size - length + 1):
            sub = s[i:i + length]
            if sub in seen:
                print(length)
                ans_got = 1
                break
            else:
                seen[sub] = 1
        if ans_got == 1:
            break
    if ans_got == 0:
        print(0)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)