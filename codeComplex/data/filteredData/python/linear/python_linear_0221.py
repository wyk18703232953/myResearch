import random

def main(n: int):
    # 生成长度为 n 的随机二进制字符串
    s = ''.join(random.choice('01') for _ in range(n))
    
    x = s.count('0')
    if s == '0':
        print('0')
    else:
        print('1' + '0' * x)

if __name__ == "__main__":
    # 示例：可修改为任意规模 n
    main(10)