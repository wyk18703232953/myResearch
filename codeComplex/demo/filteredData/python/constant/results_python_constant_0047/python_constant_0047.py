import math

def islucky(x):
    digits = set(list(str(x)))
    return (len(digits) == 2 and ("4" in digits and "7" in digits)) or (len(digits) == 1 and ("4" in digits or "7" in digits))

def check_number(a):
    lucky = islucky(a)
    for i in range(2, math.ceil(math.sqrt(a)) + 1):
        if a % i == 0:
            if islucky(i) or islucky(a // i):
                lucky = True
                break
    return "YES" if lucky else "NO"

def main(n):
    if n < 1:
        n = 1
    # 确定性构造输入规模：原程序只有一个整数输入
    # 这里将输入整数映射为 n 的简单函数，保证可扩展
    a = n * 123457 + 4  # 始终为正且随 n 线性增长
    result = check_number(a)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要调整 n 以改变“输入规模”
    main(10)