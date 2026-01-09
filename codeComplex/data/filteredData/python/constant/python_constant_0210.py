def main(n):
    # 将 n 映射为 (k1, k2, k3)，保证确定性且避免除零
    # 使得当 n 增大时参数随之变化，但规律固定
    k1 = (n % 5) + 1
    k2 = (n % 7) + 1
    k3 = (n % 9) + 1

    fl = 0
    for i1 in range(5):
        for i2 in range(5):
            for i3 in range(5):
                flak = 1
                for i in range(8):
                    if (i - i1) % k1 == 0 or (i - i2) % k2 == 0 or (i - i3) % k3 == 0:
                        continue

                    else:
                        flak = 0
                if flak == 1:
                    fl = 1
    if fl == 1:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)