def main(n):
    # 生成长度为 n 的二进制字符串，模式为周期 2：'1','0','1','0',...
    s = ''.join('1' if i % 2 == 0 else '0' for i in range(n))
    result = '1' * min(s.count('1'), 1) + '0' * s.count('0')
    print(result)

if __name__ == "__main__":
    main(10)