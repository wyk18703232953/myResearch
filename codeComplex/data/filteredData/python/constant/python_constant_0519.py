def main(n):
    # 映射 n 到输入规模：
    # x, y, z 在 [0, n] 范围内，t1, t2, t3 在 [1, max(1, n)] 范围内
    # 使用简单算术构造确保确定性
    x = n // 2
    y = (n // 3) % (n + 1)
    z = (n // 5) % (n + 1)
    limit = max(1, n)
    t1 = (n % limit) + 1
    t2 = ((n // 2) % limit) + 1
    t3 = ((n // 3) % limit) + 1

    lift = abs(z - x) * t2 + t3 + t3 + abs(x - y) * t2 + t3
    stairs = t1 * abs(x - y)
    if lift <= stairs:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    # 示例调用，可根据需要调整 n
    main(10)