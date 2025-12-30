from collections import Counter
import random

def solve(a):
    count = 0
    mp = Counter(a)
    for i in range(len(a)):
        flag = 0
        for j in range(31):
            x = (1 << j) - a[i]
            if (x in mp) and (x == a[i] and mp[x] > 1):
                flag = 1
                break
            elif (x in mp) and (x != a[i] and mp[x] > 0):
                flag = 1
                break
        if flag == 0:
            count += 1
    return count

def main(n):
    # 根据规模 n 生成测试数据：生成 n 个在 [0, 10^5] 范围内的随机整数
    a = [random.randint(0, 10**5) for _ in range(n)]
    ans = solve(a)
    print(ans)

if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)