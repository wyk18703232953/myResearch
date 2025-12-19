import math


def field(n, x, y, t):
    t = t + 1
    upper_dist = x - 1
    left_dist = y - 1
    down_dist = n - x
    right_dist = n - y
    out_up = max(0, t - upper_dist - 1)
    out_down = max(0, t - down_dist - 1)
    out_left = max(0, t - left_dist - 1)
    out_right = max(0, t - right_dist - 1)
    field_val = base_field(t) - right_field(out_right) - right_field(out_left) - up_field(out_up, n, y) - up_field(out_down, n, y)
    return field_val


def right_field(out_r):
    return out_r ** 2


def up_field(out_up, n, y):
    rect = max(0, out_up - n + 1)
    h = out_up - rect
    wyst = max(y - 1 + h - n, 0, h - y)
    result = n * rect + h ** 2 - int((1 + wyst) / 2 * wyst)
    if result < 0:
        result = 0
    return result


def base_field(t):
    return 2 * (t ** 2) - 2 * t + 1


class CodeforcesTask256BSolution:
    def __init__(self, n, x, y, c):
        self.result = ''
        self.n_x_y_c = [n, x, y, c]

    def process_task(self):
        search = 0
        mid = 1
        found = False
        last_sm = 0
        while not found:
            ff = field(self.n_x_y_c[0], self.n_x_y_c[1], self.n_x_y_c[2], search)
            if ff == self.n_x_y_c[3]:
                found = True
            elif ff > self.n_x_y_c[3]:
                if search - last_sm == 1:
                    found = True
                else:
                    search = last_sm + (search - last_sm) // 2
            else:
                last_sm = search
                search += mid
                mid = search - last_sm
        self.result = str(search)

    def get_result(self):
        return self.result


def main(n):
    x = (n + 1) // 2
    y = (n + 1) // 2
    t = n
    c = field(n, x, y, t)
    solution = CodeforcesTask256BSolution(n, x, y, c)
    solution.process_task()
    return solution.get_result()


if __name__ == "__main__":
    print(main(5))