def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count += 1

        else:
            return count


class CodeforcesTask23ASolution:
    def __init__(self):
        self.result = ''
        self.string = ''

    def read_input(self, s):
        self.string = s

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


def generate_string(n):
    if n <= 0:
        return ""
    base = "abcd"
    chars = []
    for i in range(n):
        chars.append(base[i % len(base)])
    return "".join(chars)


def main(n):
    s = generate_string(n)
    solution = CodeforcesTask23ASolution()
    solution.read_input(s)
    solution.process_task()
    # print(solution.get_result())
    pass
if __name__ == "__main__":
    main(10)