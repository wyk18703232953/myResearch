import sys

def main(n):
    # 将 n 映射为原程序中的 n, m
    # 这里选择 n 为原 n，m 为 n（同规模的方阵情形）
    orig_n = n
    orig_m = n

    out_lines = []
    for i in range(orig_n // 2 + orig_n % 2):
        x1 = i + 1
        x2 = orig_n - i
        if x1 == x2:
            for j in range(orig_m // 2 + orig_m % 2):
                if j + 1 == orig_m - j:
                    out_lines.append(f"{x1} {j+1}")

                else:
                    out_lines.append(f"{x1} {j+1}")
                    out_lines.append(f"{x2} {orig_m-j}")

        else:
            if i % 2 == 0:
                for j in range(orig_m):
                    out_lines.append(f"{x1} {j+1}")
                    out_lines.append(f"{x2} {orig_m-j}")

            else:
                for j in range(orig_m):
                    out_lines.append(f"{x1} {orig_m-j}")
                    out_lines.append(f"{x2} {j+1}")
    # sys.stdout.write("\n".join(out_lines) + ("\n" if out_lines else ""))

if __name__ == "__main__":
    main(5)