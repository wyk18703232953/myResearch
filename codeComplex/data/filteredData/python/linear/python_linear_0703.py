import random

def main(n: int):
    # 1. 生成长度为 n 的测试数据：由 '-' 和 '+' 组成的字符串
    #    这里假设原程序中 input() 是一个长度任意的由 '+' / '-' 构成的字符串
    a = [random.choice(['+', '-']) for _ in range(n)]

    # 2. 对应原 go() 的逻辑
    x = 0
    for ch in a:
        if ch == '-':
            x = max(0, x - 1)
        else:
            x += 1

    # 输出结果（保持原程序有输出的行为）
    print(x)

if __name__ == "__main__":
    # 这里给一个示例规模，也可以在其他地方调用 main(n)
    main(10)