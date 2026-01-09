def solve(k):
    k.sort()
    if min(k) == 1:
        return "YES"
    elif k.count(2) >= 2:
        return "YES"
    elif k.count(3) == 3:
        return "YES"
    elif k == [2, 4, 4]:
        return "YES"
    return "NO"


def main(n):
    # 生成长度为3的列表，因为原题隐含输入为3个数
    # 使用与 n 相关的确定性构造
    a = (n % 5) + 1
    b = ((n // 2) % 5) + 1
    c = ((n // 3) % 5) + 1
    k = [a, b, c]
    res = solve(k)
    # print(res)
    pass
if __name__ == "__main__":
    main(10)