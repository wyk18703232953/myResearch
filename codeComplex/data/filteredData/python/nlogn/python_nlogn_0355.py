import random

def solve(x):
    n = len(x)
    s = set(x)
    ans = [x[0]]
    for i in range(n):
        for j in range(0, 32):
            if x[i] + 2**j in s:
                ans = [x[i], x[i] + 2**j]
                if x[i] + (2**j * 2) in s:
                    ans.append(x[i] + (2**j * 2))
                    return ans
    return ans

def main(n):
    # 生成测试数据：n 个整数，范围可根据需要调整
    # 为了提高出现等差数列的概率，先构造一部分等差序列，再打乱并补充随机数
    data = set()

    # 构造一个长度为 3 的等差数列
    base = random.randint(0, 1000)
    diff_power = random.randint(0, 10)  # 差为 2^k
    diff = 2 ** diff_power
    seq = [base, base + diff, base + 2 * diff]
    for v in seq:
        data.add(v)

    # 补充剩余的随机数据
    while len(data) < n:
        data.add(random.randint(0, 10**6))

    x = list(data)
    random.shuffle(x)

    ans = solve(x)
    print(len(ans))
    print(*ans)

if __name__ == "__main__":
    # 示范调用，规模可自行修改
    main(10)