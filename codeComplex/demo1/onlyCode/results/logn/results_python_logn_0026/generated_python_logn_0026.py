import random

def main(n: int):
    # 生成测试数据：随机生成 l, r，保证 0 <= l <= r <= 2^n - 1
    if n <= 0:
        l, r = 0, 0
    else:
        max_val = (1 << n) - 1
        l = random.randint(0, max_val)
        r = random.randint(l, max_val)

    # 原逻辑
    ans = l ^ r
    j = 0
    while (1 << j) <= ans:
        ans |= (1 << j)
        j += 1

    print(ans)

if __name__ == "__main__":
    # 示例：可根据需要修改 n
    main(5)