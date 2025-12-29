import random
from collections import Counter

def main(n: int):
    # 生成规模为 n 的测试数据：a 为长度为 n 的整数数组
    # 这里示例生成范围在 [0, 10^9] 内的随机整数
    a = [random.randint(0, 10**9) for _ in range(n)]

    freq = Counter(a)
    ans = 0
    for x in freq:
        for i in range(32):
            c = (1 << i) - x
            if c not in freq:
                continue
            if c == x and freq[x] == 1:
                continue
            break
        else:
            ans += freq[x]

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，n 可按需修改
    main(10)