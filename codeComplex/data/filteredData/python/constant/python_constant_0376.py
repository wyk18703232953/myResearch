import random

def main(n: int):
    # 随机生成一组 (a, b, c) 用于规模为 n 的测试
    # 保证 0 <= a, b, c <= n
    a = random.randint(0, n)
    b = random.randint(0, n)
    c = random.randint(0, n)

    # 原逻辑
    if n - a - b + c >= 1:
        if a < c or b < c:
            print(-1)
        else:
            print(n - a - b + c)
    else:
        print(-1)

if __name__ == "__main__":
    # 示例：调用 main，规模 n 可按需修改
    main(10)