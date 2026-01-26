import math

def main(n):
    # 在原程序中，输入结构为两个整数 n, k
    # 这里将第一个输入固定映射为 n
    # 第二个输入 k 由 n 确定性生成，这里取 k = n
    orig_n = n
    k = n

    ans = ((2 * orig_n + 3) - int(math.sqrt(8 * orig_n + 8 * k + 9))) // 2
    return ans

if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 的值进行规模实验
    result = main(10)
    # print(result)
    pass