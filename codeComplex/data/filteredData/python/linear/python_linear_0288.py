from collections import defaultdict
import random

def main(n):
    # 生成规模为 n 的测试数据：n 个只含 '(' 和 ')' 的随机括号串
    # 这里长度随机在 [1, 2*n] 之间，可按需要调整
    s = []
    for _ in range(n):
        length = random.randint(1, 2 * n)
        s.append(''.join(random.choice('()') for _ in range(length)))

    one = defaultdict(lambda: 0)
    two = defaultdict(lambda: 0)

    for el in s:
        I = 0
        min_ = 0

        for char in el:
            I += {'(': 1, ')': -1}[char]
            min_ = min(min_, I)

        if I >= 0 and min_ == 0:
            one[I] += 1

        if I <= 0 and min_ == I:
            two[I] += 1

    ans = 0
    for el in one.keys():
        ans += one[el] * two[-el]

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)