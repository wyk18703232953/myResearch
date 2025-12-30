import random

def main(n: int):
    # 根据规模 n 生成长度为 n 的由 '-' 和 '+' 组成的字符串
    # 你可以根据需要修改数据生成策略
    s = ''.join(random.choice(['-', '+']) for _ in range(n))

    ans = 10000
    for i in range(0, 105):
        f = True
        x = i
        for c in s:
            if c == '-':
                x -= 1
            else:
                x += 1
            if x < 0:
                f = False
        if f:
            ans = min(ans, x)
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)，可按需修改 n
    main(10)