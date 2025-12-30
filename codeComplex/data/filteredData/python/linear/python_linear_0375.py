from sys import stdout
import random
import string

def main(n):
    # 生成规模为 n 的测试数据字符串 s，由 '0' 和 '1' 组成
    # 为了更通用，也可以包含其他字符，这里按原逻辑关键是处理 '1'
    # 这里使用 '0' 和 '1'，更符合题目的思路
    s = ''.join(random.choice('01') for _ in range(n))

    # 原始逻辑开始
    ans = s.replace('1', '') + '2'
    t = ans.find('2')
    result = ans[:t] + '1' * s.count('1') + ans[t:-1]

    # 输出结果
    stdout.write(result + '\n')


if __name__ == "__main__":
    # 示例：运行 main(10)
    main(10)