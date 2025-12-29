import random

def main(n: int):
    # 随机生成 m（列数），这里简单设为 1~n 范围内
    m = random.randint(1, max(1, n))

    # 生成 n 行长度为 m 的 0/1 字符串
    ps = []
    tc = [0] * m  # 每一列的总计数
    for _ in range(n):
        row_bits = [random.choice('01') for _ in range(m)]
        temp = ''.join(row_bits)

        psa = [0] * m
        for i in range(m):
            if temp[i] == '1':
                psa[i] += 1
                tc[i] += 1
        ps.append(psa)

    ans = 'NO'
    for i in ps:
        c = 0
        for j in range(m):
            if tc[j] - i[j] > 0:
                c += 1
        if c == m:
            ans = 'YES'
            break

    print(ans)


if __name__ == "__main__":
    # 示例：规模为 5
    main(5)