import random
import string

def generate_test_string(n: int) -> str:
    # 生成长度为 n 的随机小写字母串
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

def main(n: int) -> int:
    # 1. 生成测试数据
    s = generate_test_string(n)

    # 2. 原逻辑
    ans = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            cur = s[i:j]
            if cur in s[:(j - 1)] or cur in s[(i + 1):]:
                ans = max(ans, j - i)

    # 3. 返回结果（如需打印可改为 print(ans)）
    return ans

if __name__ == "__main__":
    # 示例：规模为 10
    result = main(10)
    print(result)