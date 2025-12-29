import random
import string

def main(n: int):
    # 1. 根据规模 n 生成测试数据：长度为 n 的随机小写字符串
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    o = len(s)
    k = 0
    for i in range(o):
        r = {0}
        for j in range(o - i + 1):
            if s[j:j + i] in r:
                k = max(i, k)
            else:
                r.add(s[j:j + i])
    print(k)


if __name__ == "__main__":
    # 示例：调用 main(10)，可根据需要修改 n
    main(10)