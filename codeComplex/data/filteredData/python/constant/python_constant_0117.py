def main(n):
    if n >= 0:
        # print(n)
        pass

    else:
        a = int(n / 10)
        b = int(n / 100) * 10 - abs(n) % 10
        # print(max(a, b))
        pass
if __name__ == "__main__":
    # 示例：使用不同规模调用 main(n)
    main(0)
    main(5)
    main(-13)
    main(-1003)