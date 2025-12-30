import random

def main(n):
    # 生成规模为 n 的测试数据：随机整数数组 a
    # 这里假设原题只关心元素的奇偶性，因此生成任意整数即可
    a = [random.randint(0, 1000) for _ in range(n)]

    b = []
    for i in range(n):
        a[i] %= 2
        if b:
            if b[-1] == a[i]:
                b.pop()
            else:
                b.append(a[i])
        else:
            b.append(a[i])

    if len(b) > 1:
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    # 示例：运行 main，使用某个规模 n
    main(10)