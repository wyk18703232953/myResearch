import random

class Solver:
    def __init__(self, num_people, values):
        self.num_people = num_people
        self.values = values  # 1-based list of values, index 0 unused

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
        return self.values[pos]


def main(n):
    # n 为规模，这里根据 n 生成测试数据
    # 为了保证一定存在解，当 n % 4 == 0 时，构造 values 使得存在 pos 使 func(pos) == 0
    # 构造方式：随机前半部分，后半部分令 opposite 位置相等
    if n < 2:
        # 极小规模，随便构造
        values = [0] * (n + 1)
        for i in range(1, n + 1):
            values[i] = random.randint(-10, 10)
    else:
        values = [0] * (n + 1)
        half = n // 2
        for i in range(1, half + 1):
            values[i] = random.randint(-10, 10)
        for i in range(1, half + 1):
            opposite = (i - 1 + half) % n + 1
            values[opposite] = values[i]

    solver = Solver(n, values)
    pair = solver.solve()
    print(pair)


if __name__ == "__main__":
    # 示例：可以在这里调用 main，或者由外部调用 main(n)
    main(8)