import random
import string

def main(n: int) -> None:
    # 1. 生成长度为 n 的随机小写字母串作为测试数据
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    # 2. 原逻辑：求字符串中最长重复子串的长度（重复子串可重叠）
    m = 0
    for i in range(len(s)):
        for j in range(i, len(s) + 1):
            # 当前子串
            sub = s[i:j]
            # 子串长度需大于当前最大值，且在后面的子串中还能找到
            if len(sub) > m and sub in s[i + 1:]:
                m = len(sub)

    # 输出结果（可根据需要同时输出测试数据）
    print(m)

if __name__ == "__main__":
    # 示例：规模为 10
    main(10)