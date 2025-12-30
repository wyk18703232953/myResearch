import random

def main(n: int):
    # 生成规模为 n 的测试数据列表 k，元素在 1..4 之间
    k = [random.randint(1, 4) for _ in range(n)]

    ans = 'NO'
    if min(k) == 1 or k.count(2) >= 2 or k.count(3) >= 3 or (k.count(4) == 2 and k.count(2) == 1):
        ans = 'YES'

    print(ans)


if __name__ == "__main__":
    # 示例：可自行修改 n 测试
    main(4)