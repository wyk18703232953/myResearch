import random

def main(n: int):
    # 根据 n 生成测试数据：生成 n 个非负整数
    # 可按需要修改数据规模或范围
    a = [random.randint(0, 10**9) for _ in range(n)]

    amin = min(a)
    for i in range(n):
        a[i] -= amin
    ans = amin % n
    cnt = 0
    while True:
        if a[ans] <= cnt:
            break
        ans = (ans + 1) % n
        cnt += 1
    print(ans + 1)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)