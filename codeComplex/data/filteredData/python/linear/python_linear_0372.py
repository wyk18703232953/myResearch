from math import ceil, floor, gcd, log, log2, factorial
from collections import *
import random
import string

def main(n: int):
    # 1. 根据规模 n 生成测试数据字符串 s
    #   假设原题是处理由 '0' 和 '1' 组成的字符串，这里生成长度为 n 的随机 01 串
    s = ''.join(random.choice('01') for _ in range(n))

    # 2. 原始逻辑改写
    ans = s.replace('1', '') + '2'
    t = ans.find('2')
    result = ans[:t] + '1' * s.count('1') + ans[t:len(ans) - 1]

    # 3. 输出结果
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可根据需要修改 n
    main(10)