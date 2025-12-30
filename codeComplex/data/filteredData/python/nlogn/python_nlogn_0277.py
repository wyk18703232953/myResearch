import random

def main(n):
    d = {}

    # 生成第一组数据（规模为 n）
    # 假设键 a 范围为 [1, 2*n]，值 x 范围为 [1, 100]
    for _ in range(n):
        a = random.randint(1, 2 * n)
        x = random.randint(1, 100)
        d[a] = x

    # 生成第二组数据（规模同样用 n 控制，可根据需要调整比例）
    m = n
    for _ in range(m):
        b = random.randint(1, 2 * n)
        y = random.randint(1, 100)
        d[b] = max(y, d.get(b, 0))

    print(sum(d.values()))

if __name__ == "__main__":
    # 这里给一个默认的 n，使用时可按需修改或在其他模块中调用 main(n)
    main(10)