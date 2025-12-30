import random

def main(n: int):
    # 生成测试数据：长度为 n 的整数数组 a
    # 这里生成 0 ~ n 范围内的随机整数，可根据需要修改
    a = [random.randint(0, n) for _ in range(n)]

    mx = -1
    ans = -1
    for i in range(n):
        if a[i] > mx + 1:
            ans = i + 1
            break
        else:
            mx = max(mx, a[i])
    print(ans)


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)