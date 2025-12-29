import random

def main(n):
    # 随机生成 m（可按需要调整范围，这里设为 1 ~ n）
    m = max(1, n)  # 确保至少有 1 行
    arr = []
    for _ in range(m):
        # 每行生成 n 个随机整数（范围可调整）
        row = [random.randint(0, 100) for _ in range(n)]
        arr.append(row)

    # 原逻辑：与 arr 无关，只根据 n 输出交替 0/1 字符串
    k = 0
    ans = ""
    for _ in range(n):
        ans += str(k ^ 1)
        k = k ^ 1
    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)