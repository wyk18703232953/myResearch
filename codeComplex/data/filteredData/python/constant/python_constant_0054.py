import random

def luckynumber(n):
    a = []
    for i in range(4, n + 1):
        r = i
        c = 0
        while r > 0:
            x = r % 10
            if x != 4 and x != 7:
                c = 1
                break
            r //= 10
        if c == 0:
            a.append(i)
    return a

def main(n):
    # 生成测试数据，这里按照题意直接使用参数 n 作为规模
    a = luckynumber(n)
    for i in a:
        if n == i or n % i == 0:
            print("YES")
            break
    else:
        print("NO")

if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的值进行测试
    test_n = 100  # 这里生成规模为 100 的测试
    main(test_n)