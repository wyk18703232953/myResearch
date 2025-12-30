import random

def main(n: int):
    # 生成长度为 n 的测试数据：从 1 到 n 的整数，每个恰好出现两次，然后打乱顺序
    arr = list(range(1, n + 1)) * 2
    random.shuffle(arr)

    # 原逻辑
    ans = 0
    while len(arr) != 0:
        e = arr.pop(0)
        ans += arr.index(e)
        arr.remove(e)

    print(ans)


if __name__ == "__main__":
    # 示例：可根据需要修改或删除
    main(5)