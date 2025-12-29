import random

def main(n: int):
    # 随机生成 m（列数），至少为 1
    m = max(1, n // 2)
    # 生成 n 个长度为 m 的 01 串
    l = []
    d = {x: 0 for x in range(m)}  # 每一列为 '1' 的个数统计

    for _ in range(n):
        # 随机生成一行 01 串
        s = ''.join(random.choice('01') for _ in range(m))
        l.append(s)
        for x in range(m):
            if s[x] == '1':
                d[x] += 1

    # 原逻辑：判断是否存在一行，其所有 '1' 在列上都不是唯一的
    for x in l:
        t = 0
        for y in range(m):
            if x[y] == '1' and d[y] == 1:
                t = 1
                break
        if t == 0:
            print('YES')
            return
    print('NO')


if __name__ == "__main__":
    # 示例调用，可按需修改 n 的大小进行测试
    main(5)