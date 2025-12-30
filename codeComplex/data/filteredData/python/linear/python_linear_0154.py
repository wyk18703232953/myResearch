import random

def main(n: int):
    # 生成测试数据
    # p 取一个与 n 同级别的正整数，且至少为 1
    p = max(1, n)  
    # 生成 n 个非负整数，范围可根据需要调整
    lst = [random.randint(0, 10**6) for _ in range(n)]

    mx = 0
    curr = 0
    nxt = sum(lst)

    for i in range(n - 1):
        curr += lst[i]
        nxt -= lst[i]
        mx = max(mx, curr % p + nxt % p)

    print(mx)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)