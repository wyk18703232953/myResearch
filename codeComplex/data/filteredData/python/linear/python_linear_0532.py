import random
import string

def main(n):
    # 生成参数 k，限制为不超过 26（A-Z）
    k = min(n, 26) if n > 0 else 1

    # 生成长度为 n 的随机字符串，只使用前 k 个大写字母
    alphabet = string.ascii_uppercase[:k]
    s = ''.join(random.choice(alphabet) for _ in range(n))

    # 原始逻辑
    count = [0] * k
    for c in s:
        count[ord(c) - ord("A")] += 1
    result = k * min(count)

    print(result)


if __name__ == "__main__":
    # 示例：可以修改这里的 n 测试不同规模
    main(100)