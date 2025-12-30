import random
import string

def main(n: int):
    # 生成长度为 n 的测试数据，只包含字符 '0','1','2'
    # 可根据需要调整生成逻辑
    chars = ['0', '1', '2']
    s = ''.join(random.choice(chars) for _ in range(n))

    inf = 1e10
    mod = int(1e9 + 7)

    c = s.count('1')
    c1, i = 0, 0
    while i < len(s) and s[i] != '2':
        if s[i] == '0':
            c1 += 1
        i += 1

    # 为保持原逻辑的“连续输出”效果，统一在末尾打印
    output = []
    output.append('0' * c1)
    output.append('1' * c)
    while i < len(s):
        if s[i] != '1':
            output.append(s[i])
        i += 1
    print(''.join(output))


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)