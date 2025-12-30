import random

def main(n: int):
    # 根据 n 生成测试数据
    # 这里生成参数 l, r, x 以及数组 c
    # 可根据需要调整生成规则
    c = [random.randint(1, 10**6) for _ in range(n)]
    total_sum = sum(c)
    l = random.randint(0, total_sum // 2 if total_sum > 1 else 0)
    r = random.randint(l, total_sum)  # 保证 l <= r
    x = random.randint(0, max(c) - min(c) if n > 1 else 0)

    ans = 0
    for bitmask in range(1 << n):
        if bin(bitmask).count('1') > 1:
            res = 0
            _min = float('+inf')
            _max = float('-inf')
            for i in range(n):
                if (bitmask >> i) & 1:
                    c_i = c[i]
                    res += c_i
                    if c_i < _min:
                        _min = c_i
                    if c_i > _max:
                        _max = c_i
            if l <= res <= r and (_max - _min) >= x:
                ans += 1

    print(ans)


if __name__ == '__main__':
    # 示例：调用 main，规模可自行调整
    main(5)