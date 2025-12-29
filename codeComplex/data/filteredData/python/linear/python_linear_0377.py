import random

def main(n: int):
    # 生成测试数据：长度为 n，由 '0','1','2' 组成的随机字符串
    a = ''.join(random.choice('012') for _ in range(n))

    # 原始逻辑
    c1 = a.count('1')
    parts = a.split('2')
    lex = '0' * parts[0].count('0') + '1' * c1
    m = len(parts)
    for i in range(1, m):
        lex = lex + '2' + '0' * parts[i].count('0')
    print(lex)


if __name__ == "__main__":
    # 示例：规模 n = 20，可按需修改
    main(20)