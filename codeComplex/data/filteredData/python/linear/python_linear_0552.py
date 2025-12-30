import random

def main(n):
    # 生成测试数据：长度为 n 的非负整数数组
    # 这里生成单调不减的数组，更符合原逻辑的典型使用场景
    a = []
    cur = 0
    for _ in range(n):
        # 每次在当前值基础上加 0 或 1，保证平缓增长
        cur += random.randint(0, 1)
        a.append(cur)

    max_el = -1
    er = -1
    for i in range(len(a)):
        if a[i] - max_el > 1:
            er = i + 1
            break
        if a[i] > max_el:
            max_el = a[i]

    print(er)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)