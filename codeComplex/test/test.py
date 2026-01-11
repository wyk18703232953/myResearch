import big_o
import random
import string

def find_longest_duplicate_substring(s):
    m = 0
    n = len(s)
    for i in range(n-1):
        for j in range(i, n+1):
            if s[i:j] in s[i+1:n] and len(s[i:j]) > m:
                m = len(s[i:j])
    return m

# 自定义字符串生成器，生成不同长度的随机字符串
def generate_string_data(n):
    # 生成长度为 n 的随机字符串
    return ''.join(random.choices(string.ascii_lowercase, k=n))

# 测试复杂度
best, others = big_o.big_o(
    find_longest_duplicate_substring,
    generate_string_data,
    n_repeats=10,
    min_n=5,
    max_n=5000  # 限制最大长度，因为 O(n³) 算法对大输入很慢
)

print(f"最佳拟合复杂度: {best}")