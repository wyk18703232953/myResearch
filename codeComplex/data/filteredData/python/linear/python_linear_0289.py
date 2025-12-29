from collections import defaultdict
import random

def main(n):
    # 根据 n 生成测试数据：长度在 [1, 2n] 的随机括号串
    # 可根据需要调整生成策略
    s = []
    for _ in range(n):
        length = random.randint(1, 2 * n)
        s.append(''.join(random.choice('()') for _ in range(length)))

    one = defaultdict(int)
    two = defaultdict(int)

    for el in s:
        I = 0
        min_ = 0

        for char in el:
            I += 1 if char == '(' else -1
            if I < min_:
                min_ = I

        if I >= 0 and min_ == 0:
            one[I] += 1

        if I <= 0 and min_ == I:
            two[I] += 1

    ans = 0
    for key in one:
        ans += one[key] * two[-key]

    print(ans)


if __name__ == "__main__":
    # 示例：运行规模 n=10
    main(10)