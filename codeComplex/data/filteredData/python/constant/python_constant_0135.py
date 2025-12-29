import random

def main(n: int):
    # 生成两个正整数 a, b，大小在 [1, n] 区间
    # 为保证 b 不为 0，且尽量有一定规模，做简单限制
    if n <= 1:
        a, b = 1, 1
    else:
        a = random.randint(1, n)
        b = random.randint(1, n)
    
    ans = 0
    x, y = a, b
    while x and y:
        ans += x // y
        x, y = y, x % y
    
    print(ans)

if __name__ == "__main__":
    # 示例：规模取 100
    main(100)