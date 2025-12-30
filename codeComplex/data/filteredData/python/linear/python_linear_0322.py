import random
import string

def main(n: int):
    # 生成测试数据：两个长度为 n 的字符串序列
    # 字符串由小写字母组成，长度在 1~5 之间随机
    seq1 = [
        ''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 5)))
        for _ in range(n)
    ]
    seq2 = [
        ''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 5)))
        for _ in range(n)
    ]

    a_dicts = [{}, {}]
    # 模拟原来 j=0、j=1 两次读入
    for j, seq in enumerate([seq1, seq2]):
        for x in seq:
            if x in a_dicts[j]:
                a_dicts[j][x] += 1
            else:
                a_dicts[j][x] = 1
            if x not in a_dicts[1 - j]:
                a_dicts[1 - j][x] = 0

    c = 0
    for k in a_dicts[0]:
        c += abs(a_dicts[0][k] - a_dicts[1][k])
    return c // 2

if __name__ == "__main__":
    # 示例：规模为 10
    result = main(10)
    print(result)