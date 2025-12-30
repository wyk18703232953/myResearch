import random

def main(n):
    # 生成规模为 n 的测试数据：随机整数列表
    l = [random.randint(1, 1000) for _ in range(n)]

    # 原逻辑开始（去掉了 input()）
    l.sort(reverse=True)
    s = sum(l)
    x = 0
    c = 0
    for i in l:
        if x <= s:
            c += 1
            x += i
            s -= i
        else:
            break
    print(c)

if __name__ == "__main__":
    # 示例：调用 main(10)，可根据需要修改 n
    main(10)