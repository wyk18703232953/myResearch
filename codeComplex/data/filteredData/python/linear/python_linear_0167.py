import sys

def core_algorithm(n):
    outputs = []
    if n < 6:
        outputs.append("-1")

    else:
        l = []
        o = []
        x = (3 + n) // 2
        for i in range(3, x + 1):
            l.append((1, i))
        for i in range(x + 1, n + 1):
            o.append((2, i))
        outputs.append("1 2")
        for a, b in l:
            outputs.append(f"{a} {b}")
        for a, b in o:
            outputs.append(f"{a} {b}")
    outputs.append("1 2")
    p = 2
    for i in range(3, n + 1):
        outputs.append(f"{p} {i}")
        p = i
    return outputs

def main(n):
    outputs = core_algorithm(n)
    sys.stdout.write("\n".join(outputs) + ("\n" if outputs else ""))

if __name__ == "__main__":
    main(10)