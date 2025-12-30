from math import factorial as fact
import random

def main(n: int):
    """
    n 为规模参数，用于生成测试字符串 s 和 t：
    - s: 由 '+' 和 '-' 随机组成，长度为 n
    - t: 由 '+', '-', '?' 随机组成，长度为 n
    """
    # 生成测试数据
    s = ''.join(random.choice(['+', '-']) for _ in range(n))
    t = ''.join(random.choice(['+', '-', '?']) for _ in range(n))

    pos = s.count('+') - t.count('+')
    neg = s.count('-') - t.count('-')
    que = t.count('?')

    if pos < 0 or neg < 0:
        print(0)
    else:
        # 保持与原始代码相同的浮点计算方式
        result = (fact(que) / (fact(pos) * fact(neg))) / (2 ** que)
        print(result)

if __name__ == "__main__":
    # 示例：使用 n = 10 运行
    main(10)