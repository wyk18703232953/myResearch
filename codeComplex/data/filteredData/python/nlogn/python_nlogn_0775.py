import random

def main(n):
    # 生成规模为 n 的测试数据：随机整数数组 a
    # 可根据需要修改数据生成策略
    a = [random.randint(1, 10**9) for _ in range(n)]

    p = a.index(max(a))
    b = sorted(a)
    b.pop()
    ok = 1
    i, j = p - 1, p + 1
    while i >= 0 or j < n:
        if i >= 0 and a[i] == b[-1]:
            b.pop()
            i -= 1
        elif j < n and a[j] == b[-1]:
            b.pop()
            j += 1
        else:
            ok = 0
            break
    print('YES' if ok else 'NO')


if __name__ == "__main__":
    # 示例：运行 main(10)
    main(10)