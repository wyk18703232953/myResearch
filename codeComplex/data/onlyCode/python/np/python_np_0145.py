import sys


def read_input(input_path=None):
    if input_path is None:
        f = sys.stdin
    else:
        f = open(input_path, 'r')

    n, m = map(int, f.readline().split())

    return n, m


def sol(n, m):
    v = [0 for _ in range(n+1)]
    left, right = 1, n
    for i in range(1, n + 1):
        if n - i - 1 <= 0:
            pw = 1
        else:
            pw = 1 << (n - i - 1)

        if m <= pw:
            v[left] = i
            left += 1
        else:
            v[right] = i
            right -= 1
            m -= pw
    return [' '.join(map(str, v[1:]))]


def solve(input_path=None):
    return sol(*read_input(input_path))


def main():
    for line in sol(*read_input()):
        print(f"{line}")


if __name__ == '__main__':
    main()
