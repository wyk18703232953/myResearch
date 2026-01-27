def main(n):
    # 映射：n 作为 citys，cap 为 n // 2，保证完全确定性且可规模化
    citys = max(1, n)
    cap = max(1, n // 2)

    if citys - 1 <= cap:
        result = citys - 1

    else:
        extra = citys - cap
        result = extra * (extra + 1) // 2 + cap - 1

    # print(result)
    pass
if __name__ == "__main__":
    main(10)