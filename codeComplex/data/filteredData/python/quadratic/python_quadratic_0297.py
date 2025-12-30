import random

def main(n: int) -> None:
    # 生成测试数据：长度为 n 的数组，元素在 1~(n//2+1) 之间，保证有重复以触发逻辑
    if n <= 0:
        print(0)
        return
    max_val = max(2, n // 2 + 1)
    a = [random.randint(1, max_val) for _ in range(n)]

    p = 0
    # 跳过前面成对相等的元素
    while p + 1 < len(a) and a[p] == a[p + 1]:
        p += 2

    c = 0
    # 主逻辑：按原程序模拟
    while p < len(a):
        if p + 1 < len(a):
            i = a.index(a[p], p + 1)
            c += i - p - 1
            tmp = a.pop(i)
            a.insert(p, tmp)
        # 再次跳过成对相等的元素
        while p + 1 < len(a) and a[p] == a[p + 1]:
            p += 2
    print(c)


if __name__ == "__main__":
    # 示例：可根据需要修改 n 的规模
    main(10)