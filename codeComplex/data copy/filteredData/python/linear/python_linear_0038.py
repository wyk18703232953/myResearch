def main(n):
    # 映射规则：
    # - 数组长度为 n
    # - k 为不同元素目标数量，设为 n//2（至少为 1）
    if n <= 0:
        return

    k = max(1, n // 2)
    # 构造一个确定性的数组：a[i] = (i * 2) // 3
    a = [(i * 2) // 3 for i in range(n)]

    count = 0
    b = {}
    i = -1  # 保证在 count!=k 时也有定义
    for idx in range(n):
        val = a[idx]
        if val in b:
            b[val] += 1

        else:
            b[val] = 1
        if b[val] == 1:
            count += 1
        if count == k:
            i = idx
            break

    # 第二段逻辑
    j = -1  # 保证在后续判断中总是有值
    for idx in range(n):
        val = a[idx]
        if val in b:
            b[val] -= 1
        if b[val] == 0:
            j = idx
            break

    if count != k:
        # print("-1 -1")
        pass

    else:
        if n == 1:
            # print(1, 1)
            pass
        elif n == 2 and count == 2:
            # print(1, 2)
            pass

        else:
            # print(j + 1, i + 1)
            pass
if __name__ == "__main__":
    # 示例：使用 n=10 运行一次
    main(10)