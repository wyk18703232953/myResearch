def main(n):
    # 生成确定性输入规模：使用 n 本身作为原程序的整数输入
    x = n
    m = ''.join(set(list(str(x))))
    if m == '47' or m == '74' or m == '4' or m == '7':
        # print('YES')
        pass

    else:
        if x % 4 == 0 or x % 7 == 0 or x % 74 == 0 or x % 47 == 0:
            # print('YES')
            pass

        else:
            # print("NO")
            pass
if __name__ == "__main__":
    main(4747)