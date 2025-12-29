import sys
import math
from collections import OrderedDict

# decimal to binary
def binary(n):
    return bin(n).replace("0b", "")

# binary to decimal
def decimal(s):
    return int(s, 2)

# power of a number base 2
def pow2(n):
    p = 0
    while n > 1:
        n //= 2
        p += 1
    return p

# if number is prime in √n time
def isPrime(n):
    if n == 1:
        return False
    root = int(n ** 0.5) + 1
    for i in range(2, root):
        if n % i == 0:
            return False
    return True

# list to string, no spaces
def lts(l):
    return ''.join(map(str, l))

# string to list of characters
def stl(s):
    return list(s)

# Returns list of numbers with a particular sum
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

mod = int(1e9) + 7

def main(n):
    """
    n: 测试规模，表示已经拥有的宝石数量（0 <= n <= 6）

    测试数据生成策略：
    - 总共有 6 种颜色的宝石：
      {"purple","green","blue","orange","red","yellow"}
    - 随机性不要求，所以这里按固定顺序取前 n 个作为“已拥有”的宝石。
    """
    all_gems = ["purple", "green", "blue", "orange", "red", "yellow"]
    owned = set(all_gems[:max(0, min(6, n))])  # 生成测试数据：前 n 个颜色

    s = set(all_gems)
    for gem in owned:
        if gem in s:
            s.remove(gem)

    # 输出与原程序行为一致
    print(6 - len(owned))
    for color in s:
        if color == "purple":
            print("Power")
        elif color == "green":
            print("Time")
        elif color == "blue":
            print("Space")
        elif color == "orange":
            print("Soul")
        elif color == "red":
            print("Reality")
        else:
            print("Mind")


if __name__ == "__main__":
    # 示例：可根据需要修改测试规模
    main(3)