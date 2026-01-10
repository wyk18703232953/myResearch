def main(n):
    from operator import itemgetter

    class CodeforcesTask528BSolution:
        def __init__(self):
            self.result = ''
            self.n = 0
            self.points = []

        def read_input(self, n):
            self.n = n
            self.points = []
            for i in range(self.n):
                # Deterministic generation of points [x, t]
                x = i
                t = (i // 2) + 1
                self.points.append([x, t])
                self.points[-1].append(self.points[-1][0] + self.points[-1][1])

        def process_task(self):
            self.points.sort(key=itemgetter(2))
            last = 0
            ans = 1 if self.n > 0 else 0
            for i in range(1, self.n):
                if self.points[i][0] - self.points[i][1] >= self.points[last][0] + self.points[last][1]:
                    last = i
                    ans += 1
            self.result = str(ans)

        def get_result(self):
            return self.result

    solution = CodeforcesTask528BSolution()
    solution.read_input(n)
    solution.process_task()
    return solution.get_result()


if __name__ == "__main__":
    # Example deterministic call for experimentation
    print(main(10))