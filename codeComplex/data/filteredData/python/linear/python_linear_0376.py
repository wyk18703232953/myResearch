import math
import random
import string

def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if (n % 2 == 0) or (n % 3 == 0):
        return False
    i = 5
    while i * i <= n:
        if (n % i == 0) or (n % (i + 2) == 0):
            return False
        i += 6
    return True


def SieveOfEratosthenes(n):
    prime = []
    primes = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if primes[p]:
            prime.append(p)
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return prime


def factors(n):
    fac = []
    while n % 2 == 0:
        fac.append(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 2):
        while n % i == 0:
            fac.append(i)
            n //= i
    if n > 1:
        fac.append(n)
    return fac


def generate_test_string(n: int) -> str:
    # 生成长度为 n 的只包含字符 '0','1','2' 的字符串
    choices = ['0', '1', '2']
    return ''.join(random.choice(choices) for _ in range(n))


def process(a: str) -> str:
    b = a.count('1')
    a = a.replace('1', '')
    c = a.find('2')
    if c == -1:
        a = a + '1' * b
    else:
        a = a[:c] + '1' * b + a[c:]
    return a


def main(n: int):
    # 1. 根据规模 n 生成测试数据
    a = generate_test_string(n)

    # 2. 执行原始逻辑
    result = process(a)

    # 3. 输出结果
    print(result)


if __name__ == "__main__":
    # 示例：可在此处修改 n 进行简单本地测试
    main(10)