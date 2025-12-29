import random

def ncr(n, r, p):
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den, p - 2, p)) % p

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def valid(row, col, rows, cols, rcross, lcross):
    return rows[row] == 0 and cols[col] == 0 and rcross[col + row] == 0 and lcross[col - row] == 0

def div(n):
    if n == 1:
        return 1
    cnt = 2
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if i != n // i:
                cnt += 2
            else:
                cnt += 1
    return cnt

def isPrime(n):
    if n <= 1:
        return False
    elif n <= 2:
        return True
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

def s(b):
    ans = []
    while b > 0:
        tmp = b % 10
        ans.append(tmp)
        b = b // 10
    return ans

def main(n):
    # 生成测试数据：
    # 规模 n 为点的数量；k 在 [1, n] 内随机生成
    k = random.randint(1, n)
    arr = []
    for _ in range(n):
        # 随机生成 (x, y)，范围可根据需要调整
        x = random.randint(0, 10**6)
        y = random.randint(0, 10**6)
        arr.append((x, y))

    # 原逻辑开始
    arr = sorted(arr, key=lambda x: x[0], reverse=True)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i][0] == arr[j][0] and arr[i][1] > arr[j][1]:
                arr[i], arr[j] = arr[j], arr[i]

    cnt = arr.count(arr[k - 1])
    print(cnt)

if __name__ == '__main__':
    # 示例：调用 main，规模自定
    main(10)