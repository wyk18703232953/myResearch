import random

def main(n: int):
    # 根据 n 生成测试数据：从 1 到 n 中随机选一个数作为原程序中的 n
    x = random.randint(1, n)

    li = []
    for i in range(1, x + 1):
        if x % i == 0:
            li.append(i)

    p = 0
    for t in li:
        l = [m for m in str(t)]
        if set(l) == {'4'} or set(l) == {'7'} or set(l) == {'4', '7'}:
            p += 1

    if p > 0:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    # 示例：调用 main，规模参数可自行修改
    main(1000)