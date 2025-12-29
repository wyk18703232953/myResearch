import random

def main(n: int) -> int:
    # 生成规模为 n 的测试数据，这里生成 1 到 100 之间的随机整数
    a = [random.randint(1, 100) for _ in range(n)]
    
    b = sorted(a, reverse=True)
    total = sum(a)
    gain = 0
    num = 0

    for x in range(len(b)):
        gain += b[x]
        num += 1
        if gain > total / 2:
            break

    # 按原始程序行为，仅输出结果
    print(num)
    return num

if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可根据需要修改 n
    main(10)