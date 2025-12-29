import random

mod = 10**9 + 7
mod1 = 998244353

def hnbhai(n, s):
    low = s
    high = n + 1
    ans = n + 1
    while low <= high:
        mid = (low + high) // 2
        ss = sum(int(ch) for ch in str(mid))
        if mid - ss < s:
            low = mid + 1
        else:
            ans = mid
            high = mid - 1
    return n - ans + 1

def main(n):
    # 根据规模 n 生成测试数据
    # 约束：1 <= s <= n
    if n < 1:
        n = 1
    s = random.randint(1, n)
    
    # 调用原逻辑函数
    result = hnbhai(n, s)
    
    # 输出结果
    print(result)

if __name__ == "__main__":
    # 示例：可修改这里的 n 来调整规模
    main(10**6)