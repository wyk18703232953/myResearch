def main(n):
    x = 2 * n - 1
    ans = x
    x -= 2
    curr = 0
    while x > 0:
        curr += x
        x -= 2
    # print(ans + 2 * curr)
    pass
if __name__ == "__main__":
    # 示例：在这里指定规模 n，进行一次可重复的实验
    main(10)