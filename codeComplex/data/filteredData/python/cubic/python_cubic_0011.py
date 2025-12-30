import random
import string

def main(n: int):
    # 1. 生成长度为 n 的随机小写字符串作为测试数据
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    # 2. 原始逻辑：寻找最长的重复子串长度
    n = len(s)
    m = n - 1
    while m > 0:
        find = False
        for i in range(0, n - m):
            for j in range(i + 1, n - m + 1):
                match = True
                for k in range(0, m):
                    if s[i + k] != s[j + k]:
                        match = False
                        break
                if match:
                    find = True
                    break
            if find:
                break
        if find:
            break
        m -= 1

    # 输出结果
    print(m)

# 示例调用（提交到评测或集成时可去掉或按需修改）
if __name__ == "__main__":
    main(10)