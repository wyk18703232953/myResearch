import random
import string

def main(n: int):
    # 1. 生成长度为 n 的测试字符串，字符集为小写字母
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    # 2. 原始逻辑：求最长重复子串长度（至少出现两次，且不重叠位置不限）
    m = 0
    for i in range(n - 1):
        for j in range(1, n - i):
            if s[i:i + j] in s[i + 1:]:
                if j > m:
                    m = j

    # 输出结果（可视需要输出 s 用于调试）
    print(m)

if __name__ == "__main__":
    # 示例：规模为 10，可按需修改
    main(10)