def main(n):
    class Solver:
        def __init__(self, num_people):
            self.num_people = num_people

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
            # Deterministic value generation based on position and num_people
            return (pos * 2 + self.num_people) % 101

    solver = Solver(n)
    pair = solver.solve()
    return pair


if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    result = main(10)
    # print(result)
    pass