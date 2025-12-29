import random

def main(n):
    # 生成测试数据
    p = random.randint(1, 10**9)  # 随机选择模数
    list1 = [random.randint(0, 10**9) for _ in range(n)]

    mx = 0
    curr = 0
    nxt = sum(list1)
    for i in range(n - 1):
        curr += list1[i]
        nxt -= list1[i]
        mx = max(mx, curr % p + nxt % p)
    print(mx)

if __name__ == "__main__":
    # 示例：调用 main(10)，可按需修改 n
    main(10)