import sys

def main(n):
    # 生成测试数据：长度为 n 的两个只含 '0' 和 '1' 的字符串
    # 这里简单构造一个有一定差异的模式，便于测试
    s1 = ''.join('0' if i % 2 == 0 else '1' for i in range(n)) + '0'
    s2 = ''.join('1' if i % 3 == 0 else '0' for i in range(n)) + '0'

    res = 0
    i = 0
    while i < n:
        if s1[i] != s2[i]:
            if s1[i+1] == s2[i] and s2[i+1] == s1[i]:
                res += 1
                i += 2
                continue
            res += 1
        i += 1
    print(res)

if __name__ == "__main__":
    # 示例：可在此修改 n 进行本地测试
    main(10)