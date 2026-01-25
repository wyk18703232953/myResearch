def main(n):
    if n <= 5:
        print(-1)
        for i in range(2, n + 1):
            print(1, i)
        return

    print(1, 2)
    print(2, 3)
    print(2, 4)
    for i in range(5, n + 1):
        print(3, i)

    for i in range(2, n + 1):
        print(1, i)


if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 进行实验
    main(10)