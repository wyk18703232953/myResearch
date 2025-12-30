def main(n):
    # 这里将原来的 N 视为规模 n
    N = n

    terms = 1
    digit = 9
    total = 0

    # 寻找第 N 位所在的数字范围
    while N > terms * digit:
        N -= terms * digit
        total += digit
        terms += 1
        digit *= 10

    # 找到具体数字并取出对应位
    target_number = total + (N + terms - 1) // terms
    target_index = (N - 1) % terms
    answer_digit = str(target_number)[target_index]

    print(answer_digit)


if __name__ == "__main__":
    # 示例：使用规模 n = 100
    main(100)