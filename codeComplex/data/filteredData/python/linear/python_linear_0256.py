#!/usr/bin/env python3
import random
import string

def main(n: int):
    """
    n: 要生成的字符串长度
    功能：根据原题逻辑，在随机生成的长度为 n 的字符串上计算答案并打印。
    """

    # 3. 根据 n 生成测试数据：生成一个长度为 n 的随机小写字母串
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    # 原始逻辑
    for i in range(len(s), 0, -1):
        if s[:i] != s[i-1::-1]:
            print(i)
            break
    else:
        print(0)


if __name__ == "__main__":
    # 示例：可在此处修改 n 的默认值进行测试
    main(10)