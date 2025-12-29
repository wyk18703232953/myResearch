import random
import string

def generate_test_string(n: int) -> str:
    # 生成长度为 n 的随机小写字母串
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

def longest_repeated_substring_length(s: str) -> int:
    m = 0
    n = len(s)
    for i in range(n - 1):
        for j in range(i, n + 1):
            if s[i:j] in s[i + 1:n] and len(s[i:j]) > m:
                m = len(s[i:j])
    return m

def main(n: int):
    s = generate_test_string(n)
    result = longest_repeated_substring_length(s)
    print(result)

# 示例：需要时可调用 main(n)
# main(10)