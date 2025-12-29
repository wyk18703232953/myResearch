import itertools
import random

def main(n):
    # 生成测试数据
    # 约束：1 <= l <= r，x >= 0，c[i] 为正整数
    # 这里给出一种合理的生成方式，可按需要修改
    c = [random.randint(1, 100) for _ in range(n)]
    total_sum = sum(c)
    l = random.randint(0, total_sum // 2) if total_sum > 0 else 0
    r = random.randint(l, total_sum) if total_sum >= l else l
    x = random.randint(0, max(c) - min(c) if n > 1 else 0)

    counter = 0
    for val in ("".join(seq) for seq in itertools.product("01", repeat=n)):
        if val.count('1') < 2:
            continue
        dif = 0
        mx = float("-inf")
        mn = float("inf")
        for i, bit in enumerate(val):
            if bit == '1':
                dif += c[i]
                mx = max(c[i], mx)
                mn = min(c[i], mn)
        if l <= dif <= r and mx - mn >= x:
            counter += 1

    print(counter)


if __name__ == "__main__":
    # 示例：n = 10
    main(10)