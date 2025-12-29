import random

def main(n: int):
    # 1. 生成测试数据：根据规模 n 生成 l, r
    # 这里选取 0 <= l <= r < 2^n 的随机整数
    if n <= 0:
        l, r = 0, 0
    else:
        upper = (1 << n) - 1
        l = random.randint(0, upper)
        r = random.randint(l, upper)

    # 2. 原逻辑开始（去掉 input 部分）
    a = bin(l)
    b = bin(r)
    a = "0" * (len(b) - len(a)) + a[2:len(a)]
    b = b[2:len(b)]
    c = [0 for _ in range(len(a))]
    flag = False
    for i in range(len(a)):
        if a[i] != b[i]:
            flag = True
        if flag:
            c[i] = 1
    ans = 0
    for j in range(len(a)):
        ans += c[len(a) - 1 - j] * (2 ** j)

    # 输出结果，可根据需要调整输出内容
    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(10)，规模 n 可自行调整
    main(10)