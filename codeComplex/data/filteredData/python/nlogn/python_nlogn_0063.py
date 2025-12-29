import random

def main(n: int):
    # 1. 根据 n 生成测试数据
    # 生成 n 个随机整数，范围可根据需要调整
    a = [random.randint(1, 1000) for _ in range(n)]

    # 2. 原逻辑开始
    a.sort()
    total_money = sum(a)
    i_have = 0
    cnt = 0

    for i in range(n - 1, -1, -1):
        remaining = total_money - i_have
        if i_have > remaining:
            break
        i_have += a[i]
        cnt += 1

    print(cnt)


if __name__ == "__main__":
    # 示例：调用 main，规模为 10
    main(10)