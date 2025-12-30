import random

def main(n: int):
    # 生成测试数据：n 个 1~n 范围内的随机正整数
    a = [random.randint(1, n) for _ in range(n)]

    a.sort()
    count = 0
    for i in range(n):
        cur_c = a[i]
        if not cur_c:
            continue
        count += 1
        for j in range(i + 1, n):
            if a[j] % cur_c == 0:
                a[j] = 0
    print(count)


if __name__ == "__main__":
    # 示例：可根据需要修改 n 的大小
    main(10)