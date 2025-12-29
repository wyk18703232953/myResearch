import random

class Solver:
    def __init__(self, num_people, values):
        self.num_people = num_people
        # values 是 1-based 的数组，索引 0 不用
        self.values = [None] + values

    def solve(self):
        if self.num_people % 4 == 2:
            return -1
        return self.find_zero_pair()

    def find_zero_pair(self):
        begin = 1
        end = self.num_people // 2 + 1

        begin_value = self.func(begin)
        if begin_value == 0:
            return begin

        while begin < end:
            mid = (begin + end) // 2
            mid_value = self.func(mid)
            if mid_value == 0:
                return mid
            elif begin_value * mid_value > 0:
                begin = mid + 1
            else:
                end = mid - 1

        return begin

    def func(self, pos):
        opposite = (pos - 1 + self.num_people // 2) % self.num_people + 1
        return self.get_value(pos) - self.get_value(opposite)

    def get_value(self, pos):
        # 原逻辑为交互式询问，这里直接从预生成数据中取值
        return self.values[pos]


def generate_values(n):
    """
    生成一组测试数据 values[1..n]，保证存在某个 i（1 <= i <= n/2）
    使得 values[i] == values[opposite(i)]，从而 func(i) == 0。
    n 必须是偶数且 n % 4 != 2，才能保证原题逻辑有效。
    """
    if n % 2 != 0:
        raise ValueError("n must be even.")
    if n % 4 == 2:
        # 按原代码逻辑，这种情况直接返回 -1，因此仅构造任意数据即可
        # 但为了统一，这里也给出任意数据
        return [random.randint(-10**9, 10**9) for _ in range(n)]

    values = [0] * (n + 1)  # 1-based
    half = n // 2

    # 选定一个 i 作为保证 func(i) == 0 的位置
    i = random.randint(1, half)
    opposite_i = (i - 1 + half) % n + 1

    # 为 (i, opposite_i) 赋相同值
    v = random.randint(-10**6, 10**6)
    values[i] = v
    values[opposite_i] = v

    # 为其他位置随机赋值；与其对面的值可独立随机
    # 不强求别的位置也满足差值为 0，但不妨有多个解
    for pos in range(1, n + 1):
        if values[pos] != 0:
            continue
        # 如果这个位置的对面已经有值，可以选择同值或不同值
        opp = (pos - 1 + half) % n + 1
        if values[opp] == 0:
            # 两边都没定，则同时随机
            val_pos = random.randint(-10**6, 10**6)
            val_opp = random.randint(-10**6, 10**6)
            values[pos] = val_pos
            values[opp] = val_opp
        else:
            # 对面已有值，这里自由取值
            values[pos] = random.randint(-10**6, 10**6)

    return values[1:]  # 去掉索引 0


def main(n):
    """
    n 为问题规模（人数），需要是整数。
    将会：
      1. 生成一组长度为 n 的测试数据。
      2. 运行原算法（非交互版）。
      3. 输出找到的位置（或 -1）。
    """
    values = generate_values(n)
    solver = Solver(n, values)
    pair = solver.solve()
    print(pair)


# 示例：直接运行时可在此指定 n
if __name__ == "__main__":
    # 修改这里以测试不同的 n
    test_n = 8
    main(test_n)