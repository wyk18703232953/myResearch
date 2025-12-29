import random
import string

def main(n: int):
    # 根据规模 n 生成长度为 n 的随机小写字母串
    a = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    l = 0
    for i in range(1, len(a)):
        for j in range(0, len(a) - i + 1):
            t = a.find(a[j:j + i])
            c = a.rfind(a[j:j + i])
            if t != c:
                if i > l:
                    l = i
    print(l)


if __name__ == "__main__":
    # 示例：可自行修改 n 测试规模
    main(10)