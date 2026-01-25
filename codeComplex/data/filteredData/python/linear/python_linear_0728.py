import os

def log(*args, **kwargs):
    if os.environ.get('CODEFR'):
        print(*args, **kwargs)

def main(n):
    # 这里将原程序的 n 映射为输入中的第一个整数
    # 第二个整数 k 设为 n//2，使得规模由 n 决定且确定性
    if n < 0:
        n = 0
    input_n = n
    k = n // 2
    if input_n < k:
        k = input_n

    # 原始逻辑开始
    if input_n - k < 0:
        s = '1'
    else:
        s = '0' * ((input_n - k) // 2) + '1'

    res_chars = []
    m = len(s)
    for i in range(input_n):
        res_chars.append(s[i % m])
    output = ''.join(res_chars)
    print(output)
    return output

if __name__ == "__main__":
    main(10)