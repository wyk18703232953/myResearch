from math import *

def main(n):
    # 生成确定性的 n 和 k
    # 这里将原来的 n 替换为 n，k 生成为 n 的一半（向下取整）
    orig_n = n
    k = n // 2

    s = 1
    dob = 2
    for i in range(1, orig_n):
        s += dob
        dob += 1
        if s - (orig_n - i - 1) == k:
            print(orig_n - i - 1)
            return
    print(0)

if __name__ == "__main__":
    # 示例调用，可按需修改 n 的值进行规模实验
    main(10)