import random
import string

def main(n: int):
    # 1. 生成长度为 n 的随机测试字符串（由小写字母组成）
    line = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    # 2. 原始逻辑
    temp = [0]
    for i in range(1, n):
        for j in range(n - i):
            for k in range(1, n - i - j + 1):
                if line[j:j+i] == line[j+k:j+k+i]:
                    temp.append(i)

    # 输出结果（最大重复子串长度）
    print(max(temp))

if __name__ == "__main__":
    # 示例：规模 n 可在此处调整
    main(10)