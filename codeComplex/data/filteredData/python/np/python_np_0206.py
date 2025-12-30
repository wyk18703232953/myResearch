import sys
import random

def main(n: int):
    # 生成测试数据
    # 约束：1 <= n <= 15（原题是 1 << n 枚举子集，n 太大会爆炸）
    if n <= 0:
        print(0)
        return

    # 随机生成参数 l, r, x 和数组 temp
    # temp 中每个难度在 [1, 100] 范围内
    temp = [random.randint(1, 100) for _ in range(n)]
    temp.sort()

    # 为了保证 l, r 合理，先根据 temp 的一些统计来生成
    total_sum = sum(temp)
    min_sum = temp[0] + temp[1] if n >= 2 else temp[0]
    max_sum = total_sum

    # 保证 l <= r，并且区间覆盖一部分可能的和
    l = random.randint(min_sum, max_sum)
    r = random.randint(l, max_sum)

    # x 为难度差要求，范围在 [0, max(temp) - min(temp)]
    difficulty_range = temp[-1] - temp[0]
    x = random.randint(0, difficulty_range) if difficulty_range > 0 else 0

    ans = 0
    for i in range(1 << n):
        score = 0
        _min = sys.maxsize
        _max = -sys.maxsize
        for j in range(n):
            if i & (1 << j):
                _min = min(_min, temp[j])
                _max = max(_max, temp[j])
                score += temp[j]
        if score >= l and score <= r and _max - _min >= x:
            ans += 1

    print(ans)


if __name__ == "__main__":
    # 示例：可在这里指定规模 n 进行运行
    main(5)