import math

def lucky(x):
    return (list(set(list(str(x)))) in [["4"], ["7"], ["4", "7"], ["7", "4"]])

def main(n):
    # 将 n 映射为待测整数 a 的规模，这里直接使用 n
    a = max(1, n)
    true = False
    for i in range(1, math.ceil(math.sqrt(a)) + 1):
        if a % i == 0:
            if lucky(i) or lucky(a // i):
                true = True
                break
    # print("YES" if true else "NO")
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 进行实验
    main(100)