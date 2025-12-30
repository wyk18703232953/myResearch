import sys
import random

def main(n: int):
    # 生成测试数据示例：这里只是展示，可以根据需要修改
    # 本题原逻辑只需要 n，因此不额外生成复杂数据
    # 示例：生成一个长度为 n 的随机数组（不参与后续逻辑）
    test_data = [random.randint(1, 100) for _ in range(n)]

    if n < 6:
        sys.stdout.write("-1\n")
    else:
        l = []
        o = []
        x = (3 + n) // 2
        for i in range(3, x + 1):
            l.append((1, i))

        for i in range(x + 1, n + 1):
            o.append((2, i))

        sys.stdout.write("1 2\n")
        for a, b in l:
            sys.stdout.write(f"{a} {b}\n")
        for a, b in o:
            sys.stdout.write(f"{a} {b}\n")

    sys.stdout.write("1 2\n")
    p = 2
    for i in range(3, n + 1):
        sys.stdout.write(f"{p} {i}\n")
        p = i


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可在此处修改
    main(10)