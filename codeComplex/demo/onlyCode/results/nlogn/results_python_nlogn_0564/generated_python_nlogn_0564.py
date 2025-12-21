def main(n):
    cond = '1'
    if cond == '1':
        s = 'x' * n
        return s
    else:
        arr = list(range(1, n + 1))
        x, *a, y = sorted(arr)
        return y - x + sum(map(abs, a))


if __name__ == "__main__":
    print(main(5))