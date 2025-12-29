import random

def main(n):
    # 生成测试数据：a, b, c, n
    # 这里的 n 作为总和规模，同时生成 a,b,c 不超过 n
    a = random.randint(0, n)
    b = random.randint(0, n)
    c = random.randint(0, min(a, b))  # 为了常见情况可行，约束 c <= a,b
    total = n                         # 用 n 作为原代码中的 n（总数）

    # 原始逻辑
    p = total - (a + b - c)
    if c > a or c > b or p <= 0:
        print(-1)
        return
    if p < 1:
        print(-1)
    else:
        print(p)

if __name__ == "__main__":
    # 示例：规模设为 100
    main(100)