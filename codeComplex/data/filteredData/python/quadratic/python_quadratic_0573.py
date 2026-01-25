import sys

def main(n):
    # 映射：n -> (rows, cols) = (n, n)
    r = n
    c = n
    out_lines = []
    for i in range(r // 2 + r % 2):
        x1 = i + 1
        x2 = r - i
        if x1 == x2:
            for j in range(c // 2 + c % 2):
                if j + 1 == c - j:
                    out_lines.append(f"{x1} {j+1}")
                else:
                    out_lines.append(f"{x1} {j+1}")
                    out_lines.append(f"{x2} {c-j}")
        else:
            if i % 2 == 0:
                for j in range(c):
                    out_lines.append(f"{x1} {j+1}")
                    out_lines.append(f"{x2} {c-j}")
            else:
                for j in range(c):
                    out_lines.append(f"{x1} {c-j}")
                    out_lines.append(f"{x2} {j+1}")
    sys.stdout.write("\n".join(out_lines) + ("\n" if out_lines else ""))

if __name__ == "__main__":
    main(5)