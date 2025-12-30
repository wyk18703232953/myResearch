import random
import string

def main(n: int):
    # 1. 生成测试数据：长度为 n 的随机小写字符串
    st = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    # 2. 原逻辑：求最长重复子串长度
    m = 0
    length = len(st)
    for i in range(length):
        for j in range(i, length + 1):
            if st[i:j] in st[i + 1:length] and len(st[i:j]) > m:
                m = len(st[i:j])
    print(m)


if __name__ == "__main__":
    # 示例：n 可根据需要调整
    main(10)