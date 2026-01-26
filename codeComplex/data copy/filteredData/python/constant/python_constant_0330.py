def main(n):
    if n == 0:
        return 0
    if (n + 1) % 2 == 0:
        return (n + 1) // 2

    else:
        return n + 1

if __name__ == "__main__":
    # 示例：使用若干不同规模 n 调用 main 并打印结果，便于做时间复杂度实验
    for n in range(0, 11):
        # print(f"n={n}, result={main(n)}")
        pass