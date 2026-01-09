def binary(n):
    return bin(n).replace("0b", "")

def decimal(s):
    return int(s, 2)

def pow2(n):
    p = 0
    while n > 1:
        n //= 2
        p += 1
    return p

def isPrime(n):
    if n == 1:
        return False
    root = int(n ** 0.5) + 1
    for i in range(2, root):
        if n % i == 0:
            return False
    return True

def lts(l):
    return ''.join(map(str, l))

def stl(s):
    return list(s)

def sq(a, target, arr=None):
    if arr is None:
        arr = []
    s = sum(arr)
    if s == target:
        return arr
    if s >= target:
        return None
    for i in range(len(a)):
        n = a[i]
        remaining = a[i + 1:]
        ans = sq(remaining, target, arr + [n])
        if ans:
            return ans
    return None

def SieveOfEratosthenes(n):
    cnt = 0
    prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n + 1):
        if prime[p]:
            cnt += 1
    return cnt

def main(n):
    if n < 2:
        n = 2
    # Interpret n as both length of string and parameter scale
    k = n if n % 2 == 0 else n - 1
    if k < 2:
        k = 2
    # Deterministically construct a parenthesis string s of length n
    # Alternate '(' and ')' to give mixed pattern
    s_chars = []
    for i in range(n):
        if i % 2 == 0:
            s_chars.append('(')

        else:
            s_chars.append(')')
    s = ''.join(s_chars)

    ans = []
    lb = k // 2
    rb = k // 2

    for c in s:
        if lb > 0:
            if c == "(":
                lb -= 1

            else:
                rb -= 1
            ans.append(c)
        elif rb > 0:
            if c == ")":
                ans.append(c)
                rb -= 1
        elif lb == 0 and rb == 0:
            break

    result = lts(ans)
    # print(result)
    pass
    return result

if __name__ == "__main__":
    # example deterministic call
    main(10)