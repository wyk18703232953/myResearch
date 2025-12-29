import math
import random

def main(n):
    # 根据规模 n 生成 s，保证 1 <= s <= n
    if n <= 0:
        return 0
    s = random.randint(1, n)

    c = 0
    # 原代码中的 i 起始为 n，但随即在 for 中被覆盖，这里直接从 s 开始
    last_i = s
    upper = min(s + 1000, n + 1)
    for i in range(s, upper):
        if i - sum(map(int, str(i))) >= s:
            c += 1
        last_i = i

    # 原代码在 for 后使用 c += max(0, n - i)
    c += max(0, n - last_i)
    print(c)
    return c

if __name__ == "__main__":
    # 示例：可自行设置 n 的测试规模
    main(10**6)