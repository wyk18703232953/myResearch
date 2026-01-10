def main(n):
    # 将 n 的奇偶性映射为原程序中第一次 input() 的 '1' 或其他
    first_input = '1' if n % 2 == 1 else '0'

    if first_input == '1':
        # 当原程序 input()=='1' 时，第二次 input() 是任意字符串，这里构造为确定性的
        # 构造一个长度为 n 的确定性字符串
        s = ''.join(chr(97 + (i % 26)) for i in range(n))
        print(s)
    else:
        # 当原程序 input()!='1' 时，第二次 input() 是一行整数
        # 使用 n 作为列表长度规模，构造一个确定性的整数列表
        # 构造规则：a[i] = i*(-1)**i
        arr = [i if i % 2 == 0 else -i for i in range(n)]
        # 保持原程序逻辑
        x, *a, y = sorted(arr)
        result = y - x + sum(map(abs, a))
        print(result)


if __name__ == "__main__":
    main(10)