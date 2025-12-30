import math
import random

def main(n: int):
    # 生成测试数据 s 和 s1
    # 保证规模与 n 相关，这里令 s 的长度为 n
    # s 和 s1 的字符从 {'+', '-'} 和 {'+', '-', '?'} 中随机生成
    chars_s = ['+', '-']
    chars_s1 = ['+', '-', '?']

    # 生成 s
    s = ''.join(random.choice(chars_s) for _ in range(n))
    # 生成 s1
    s1 = ''.join(random.choice(chars_s1) for _ in range(n))

    plus = s.count('+') - s1.count('+')
    minus = s.count('-') - s1.count('-')
    v = s1.count('?')

    if plus < 0 or minus < 0 or plus + minus != v:
        # 原始逻辑中只检查 plus<0 或 minus<0；
        # 若不满足组合条件，概率应为 0
        print(0.0)
        return

    # 组合数 C(v, plus) * (0.5 ** v)
    # 使用整数阶乘计算后再乘以概率
    ways = math.factorial(v) // (math.factorial(plus) * math.factorial(v - plus))
    result = ways * (0.5 ** v)
    print(result)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)