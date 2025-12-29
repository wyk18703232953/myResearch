import random

def main(n):
    # 生成测试数据：
    # x: 长度为 n 的整数列表，元素范围 1~2n
    # y: 长度为 n 的整数列表，元素范围 1~2n
    x = [random.randint(1, 2 * n) for _ in range(n)]
    y = [random.randint(1, 2 * n) for _ in range(n)]

    out = []
    first = 11
    for a in range(len(x)):
        for b in range(len(y)):
            if y[b] == x[a]:
                if first < a:
                    first = a
                    out.append(y[b])
                    b += 1
                else:
                    out.insert(0, y[b])
                    b += 1
            else:
                b += 1

    out.reverse()
    for a in out:
        print(a)


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)