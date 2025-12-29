import random

def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


def main(n):
    # 1) 按位分解数字并输出不同的 10^i * digit
    # 生成 n 个随机整数（1 到 10^9）
    for _ in range(n):
        x = random.randint(1, 10**9)
        digits = []
        new_digits = set()
        t = x
        if t in range(1, 10):
            print(1)
            print(t)
        else:
            while t > 0:
                digit = t % 10
                digits.append(digit)
                t = t // 10
            i = 0
            for d in digits:
                new_digits.add(d * 10 ** i)
                i += 1
            if 0 in new_digits:
                new_digits.remove(0)
            print(len(new_digits))
            for d in new_digits:
                print(d, end=" ")
            print("")

    # 2) 在数组中查找从 1..n 的元素索引（1-based）
    # 生成一个 1..n 的随机排列
    a = list(range(1, n + 1))
    random.shuffle(a)
    b = list(range(1, n + 1))
    results = []
    for l in b:
        results.append(a.index(l) + 1)
    for r in results:
        print(r, end=" ")
    print("")

    # 3) 统计被 k,l,m,n 中任意一个整除的 1..d 的数
    # 根据 n 生成一些参数
    k = random.randint(1, max(1, n))
    l = random.randint(1, max(1, n))
    m = random.randint(1, max(1, n))
    nn = random.randint(1, max(1, n))
    d = max(1, n * 2)
    nums = list(range(1, d + 1))
    results = set()
    for num in nums:
        if num % k == 0:
            results.add(num)
        elif num % l == 0:
            results.add(num)
        elif num % m == 0:
            results.add(num)
        elif num % nn == 0:
            results.add(num)
    print(len(results))

    # 4) function problem（简单数学函数）
    x = random.randint(-10**9, 10**9)
    if x % 2 == 0:
        result = x // 2
    else:
        result = -1 * (x // 2 + 1)
    print(result)

    # 5) General arrival 相关逻辑
    # 构造长度为 n 的随机数组
    a = [random.randint(-10**4, 10**4) for _ in range(n)]
    b = list(dict.fromkeys(a))  # 去重并保序

    # 找最大值及其在去重后数组中的索引
    max_index = 0
    i = 0
    maxi = b[0]
    while i < len(b):
        if b[i] >= maxi:
            maxi = b[i]
            max_index = i
        i += 1

    # 找最小值及其在去重后数组中的索引
    min_index = 0
    i = 0
    mini = max(b)
    while i < len(b):
        if b[i] <= mini:
            mini = b[i]
            min_index = i
        i += 1

    if len(a) == 2:
        print(len(a) - 1)
    else:
        print((max_index - 0) + ((len(b) - 1) - min_index))
    print(b)

    # 6) 最后这段：将 n 分解为两个合数 first 和 second（与原始输入 n 对应）
    # 使用参数 n 作为目标数
    temp = n // 2
    first = temp
    second = n - temp
    while is_prime(first) or is_prime(second):
        first -= 1
        second += 1
        if first + second == n and (not is_prime(first) and not is_prime(second)):
            break
    print(first, end=" ")
    print(second)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)