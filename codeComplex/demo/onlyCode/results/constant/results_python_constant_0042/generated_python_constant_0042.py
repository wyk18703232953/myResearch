def check(num):
    l = list(str(num))
    l = list(dict.fromkeys(l))
    if l == ['4', '7'] or l == ['7', '4'] or l == ['4'] or l == ['7']:
        return True
    else:
        return False


def main(n):
    # 生成测试数据：这里直接使用传入的 n 作为规模和被检测的数
    lucky = False
    for i in range(3, n + 1):
        if n % i == 0 and check(i):
            lucky = True
    print("YES" if lucky else "NO")


if __name__ == "__main__":
    # 示例：自行修改 n 以测试
    main(100)