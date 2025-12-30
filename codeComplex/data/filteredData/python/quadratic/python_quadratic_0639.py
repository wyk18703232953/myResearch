import random

def solve(n, a):
    a = sorted(a)
    col = [False for _ in range(n)]
    count = 0
    for i in range(n):
        if not col[i]:
            count += 1
            col[i] = True
            for j in range(n):
                if a[j] % a[i] == 0:
                    col[j] = True
    return count

def main(n):
    # 生成测试数据：n 个 1~1000 的随机整数
    a = [random.randint(1, 1000) for _ in range(n)]
    print(solve(n, a))

if __name__ == "__main__":
    main(10)