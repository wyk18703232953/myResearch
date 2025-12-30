import random

def main(n):
    # 生成测试数据
    # 生成一个长度为 n 的排列 a
    a = list(range(1, n + 1))
    random.shuffle(a)
    # 生成一个长度为 n 的排列 b
    b = a[:]  # 保证 b 中的元素一定都在 a 中，避免死循环
    random.shuffle(b)

    now = 0
    ans = []
    h = set()
    for i in range(n):
        count = 0
        while b[i] not in h:
            h.add(a[now])
            now += 1
            count += 1
        ans.append(str(count))
    print("n =", n)
    print("a:", " ".join(map(str, a)))
    print("b:", " ".join(map(str, b)))
    print("answer:", " ".join(ans))


if __name__ == '__main__':
    # 示例：规模为 10
    main(10)