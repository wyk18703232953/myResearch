from collections import defaultdict
import random

def main(n):
    # 根据 n 生成 n 个由 '(' 和 ')' 构成的随机字符串
    # 字符串长度这里设为 1~2n 的随机长度，可按需求调整
    random.seed(0)
    strs = []
    for _ in range(n):
        length = random.randint(1, max(1, 2 * n))
        s = ''.join(random.choice(['(', ')']) for _ in range(length))
        strs.append(s)

    first = defaultdict(int)
    second = defaultdict(int)

    for s in strs:
        count = 0
        min_count = 0
        for c in s:
            if c == '(':
                count += 1
            else:
                count -= 1
            min_count = min(count, min_count)
        if min_count >= 0:
            first[count] += 1
        if count == min_count:
            second[count] += 1

    res = 0
    for k, v in first.items():
        res += v * second[-k]

    print(res)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)