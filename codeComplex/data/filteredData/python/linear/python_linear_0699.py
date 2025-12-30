import random

def main(n):
    # 生成测试数据：n 为规模，v 在 [1, n] 范围内随机生成
    v = random.randint(1, n)

    res = 0
    cur_tank = 0
    for c in range(1, n + 1):
        need_to_by = min(v - cur_tank, n - c - cur_tank)
        res += need_to_by * c
        cur_tank += need_to_by
        cur_tank -= 1
    print(res)


if __name__ == '__main__':
    # 示例：调用 main，n 可按需修改
    main(10)