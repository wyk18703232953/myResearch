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
    tmp = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                n //= i
                cnt += 1
            tmp.append((i, cnt))
        i += 1
    if n > 1:
        tmp.append((n, 1))
    return tmp

def isPrime(n):
    if n <= 1:
        return False
    if n <= 2:
        return True
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def s(b):
    ans = []
    while b > 0:
        tmp = b % 10
        ans.append(tmp)
        b //= 10
    return ans

def main(n):
    # print(n, 0, 0)
    pass
if __name__ == "__main__":
    main(10)