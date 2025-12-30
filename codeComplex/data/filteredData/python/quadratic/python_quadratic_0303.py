import random

def main(n: int) -> None:
    # 生成测试数据：长度为 2n 的数组，每个数字出现两次，顺序打乱
    c = []
    for i in range(n):
        c.extend([i, i])
    random.shuffle(c)

    ans = 0
    # 模拟原逻辑：每次取出第一个元素，在剩余列表中找到与之相同的元素并移除
    for _ in range(n):
        f = c.pop(0)
        g = c.index(f)
        c.pop(g)
        ans += g

    print(ans)


if __name__ == "__main__":
    # 可以在此修改 n 的大小进行本地测试
    main(5)