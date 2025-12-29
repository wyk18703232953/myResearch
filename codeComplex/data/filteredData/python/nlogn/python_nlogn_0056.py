import random

def main(n: int):
    # 生成测试数据：n 个 1~100 之间的随机整数
    l = [random.randint(1, 100) for _ in range(n)]
    l.sort(reverse=True)

    coin = 0
    total_sum = sum(l)
    current_sum = 0

    for i in range(len(l)):
        coin += 1
        current_sum += l[i]
        remaining_sum = total_sum - current_sum
        if current_sum > remaining_sum:
            break

    print(coin)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)