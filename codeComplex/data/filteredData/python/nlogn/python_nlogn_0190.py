import random

def main(n):
    # 生成规模为 n 的测试数据，这里随机生成整数列表
    # 可根据需要修改数据范围
    l = [random.randint(1, 10) for _ in range(n)]

    freq = {}
    for v in l:
        freq[v] = 0

    total_sum = 0
    total_count = 0
    ans = 0

    for i in range(n - 1, -1, -1):
        x = total_sum
        y = total_count
        for j in range(-1, 2):
            aa = l[i] + j
            if aa in freq:
                x -= aa * freq[aa]
                y -= freq[aa]
        ans += x - l[i] * y
        total_count += 1
        total_sum += l[i]
        freq[l[i]] += 1

    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(10)，可按需修改
    main(10)