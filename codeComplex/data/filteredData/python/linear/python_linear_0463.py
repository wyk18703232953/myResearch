import random
import string

def main(n: int):
    # 1. 生成测试数据：长度为 n 的随机字符串，字符从小写字母中选取
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))
    
    # 2. 原逻辑
    s = s * 3
    length = len(s)
    m, curr = 1, 1
    for i in range(length - 1):
        if s[i] != s[i + 1]:
            curr += 1
            m = max(curr, m)
        else:
            curr = 1
    result = min(m, length // 3)
    
    # 3. 输出结果
    print(result)

# 示例调用
if __name__ == "__main__":
    main(10)