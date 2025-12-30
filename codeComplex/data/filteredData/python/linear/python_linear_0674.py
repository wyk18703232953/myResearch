import random

def main(n: int):
    # 生成测试数据：长度为 n 的 0/1 数组
    # 可根据需要修改生成策略
    a = [random.randint(0, 1) for _ in range(n)]

    v = [a[0]]
    for i in range(1, n):
        if v and v[-1] == a[i]:
            v.pop()
        else:
            v.append(a[i])
    print("NO" if len(v) > 1 else "YES")


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可修改为任意规模 n
    main(10)