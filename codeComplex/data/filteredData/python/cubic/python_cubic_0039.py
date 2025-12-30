import random
import string


def occurrences(s, sub):
    count = start = 0
    while True:
        start = s.find(sub, start) + 1
        if start > 0:
            count += 1
        else:
            return count


class CodeforcesTask23ASolution:
    def __init__(self, s=""):
        self.result = ''
        self.string = s

    def generate_input(self, n):
        # 生成长度为 n 的随机小写字母串
        letters = string.ascii_lowercase
        self.string = ''.join(random.choice(letters) for _ in range(n))

    def process_task(self):
        o_max = 0
        for x in range(len(self.string)):
            for y in range(x):
                m = occurrences(self.string, self.string[y:x])
                if m >= 2:
                    o_max = max(x - y, o_max)
        self.result = str(o_max)

    def get_result(self):
        return self.result


def main(n):
    solution = CodeforcesTask23ASolution()
    solution.generate_input(n)
    solution.process_task()
    print(solution.get_result())


if __name__ == "__main__":
    # 示例：指定规模 n
    main(10)