import sys

def main(n):
    # 这里根据 n 构造 m；若需要可自行调整规则
    m = n

    for i in range(n // 2):
        for j in range(m):
            # sys.stdout.write('{} {}\n'.format(i + 1, j + 1))
            # sys.stdout.write('{} {}\n'.format(n - i, m - j))
            pass
    if n % 2:
        for j in range(m // 2):
            # sys.stdout.write('{} {}\n'.format(n // 2 + 1, j + 1))
            # sys.stdout.write('{} {}\n'.format(n // 2 + 1, m - j))
            pass
        if m % 2:
            # sys.stdout.write('{} {}\n'.format(n // 2 + 1, m // 2 + 1))
            pass


if __name__ == "__main__":
    # 示例：可以在此处指定规模 n 进行简单测试
    main(5)