import random
import string

def main(n: int):
    # 1. 根据 n 生成测试数据：长度为 n 的随机小写字母串
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    mc = -1

    # 2. 原逻辑：枚举所有起点对 (i, j)，暴力比较最长公共前缀
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            for cu in range(len(s) - max(i, j)):
                if s[i + cu] == s[j + cu]:
                    mc = max(mc, cu)
                else:
                    break

    # 3. 输出结果
    print(mc + 1)


if __name__ == "__main__":
    # 示例：规模 n = 100
    main(100)