import random

def main(n):
    # 1. 生成测试数据
    # 座位行数为 n，对应 seat_rows 长度为 n
    # aliens 长度也设为 n，保证操作合法：出现 eldian 时入栈，marleyan 时出栈
    # 生成一个合法的 0/1 序列：先随机打乱，再保证整个过程栈不为空
    # 为简化，使用固定的构造方式：前半部分全是 "0"，后半部分全是 "1"
    # 这样过程一定合法：先把所有位置入栈，再依次出栈
    seat_rows = [random.randint(1, 100) for _ in range(n)]
    half = n // 2
    aliens = "0" * half + "1" * (n - half)

    eldian = "0"
    marleyan = "1"

    # 2. 原逻辑
    empty = sorted(enumerate(seat_rows), key=lambda x: x[1], reverse=True)
    non_empty = []

    result = []
    for alien in aliens:
        if alien == eldian:
            row = empty.pop()
            non_empty.append(row)
        else:
            row = non_empty.pop()

        result.append(row[0] + 1)

    print(' '.join(map(str, result)))


if __name__ == "__main__":
    # 示例调用：规模 n = 10
    main(10)