from sys import stdout

def main(n):
    # 生成规模为 n 的测试数据
    # 这里假设原程序的 n 就是规模参数，直接使用传入的 n

    k = 2
    a = []
    m = n
    while True:
        t = n // k
        if t <= 1:
            k //= 2
            a.extend([k] * m)
            a[-1] = (n // k) * k
            break
        a.extend([k // 2] * (m - t))
        m = t
        k *= 2

    stdout.write(' '.join(map(str, a)))

if __name__ == "__main__":
    # 示例：调用 main(10) 进行测试
    main(10)