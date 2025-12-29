import random

def main(n):
    # 1. 生成测试数据：长度为 n 的随机整数数组
    # 你可以根据需要调整随机数范围
    l = [random.randint(0, 100) for _ in range(n)]
    print("Generated list:", l)

    # 2. 原逻辑
    if l == sorted(l):
        print("Yes")
    else:
        cnt = 0
        g = sorted(l)
        for i in range(len(l)):
            if l[i] != g[i]:
                cnt += 1
        if cnt <= 2:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    # 示例：调用 main(10)，可自行修改 n
    main(10)