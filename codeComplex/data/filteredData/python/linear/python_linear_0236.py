import re
import random

def main(n):
    """
    n 作为生成测试字符串的长度规模参数
    """
    # 生成长度为 n 的随机字符串，只包含 'x' 和 'y'
    s = ''.join(random.choice(['x', 'y']) for _ in range(n))

    # 原逻辑：统计所有长度至少为 3 的连续 'x' 段中多出的部分总长度
    # 即对每个匹配串 f 计算 len(f) - 2 并求和
    result = sum(len(f) - 2 for f in re.findall(r'x{3,}', s))

    print(result)


if __name__ == "__main__":
    # 示例：以 n = 100 作为规模运行
    main(100)