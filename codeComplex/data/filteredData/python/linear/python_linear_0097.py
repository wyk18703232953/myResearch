import random
import string

def main(n: int):
    # 1. 生成测试数据字符串 s（长度为 n，由小写字母组成）
    #   可按需要调整字符集合，例如 string.ascii_letters 或自定义字符集。
    chars = string.ascii_lowercase
    if n <= 0:
        print(0)
        return
    s = ''.join(random.choice(chars) for _ in range(n))

    # 2. 原始逻辑
    p = len(set(s))
    q = {}
    r = 10**6
    for i in range(n):
        q[s[i]] = i
        if len(q) == p:
            r = min(r, max(q.values()) - min(q.values()))
    print(r + 1)

# 示例调用
if __name__ == "__main__":
    main(20)