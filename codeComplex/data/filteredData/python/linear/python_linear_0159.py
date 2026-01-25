def val(s):
    ans = ((int(s.split('+')[0][1:]) + int(s.split('+')[1].split(')')[0])) / int(s.split('/')[1]))
    return ans

def generate_input_strings(n):
    strings = []
    for i in range(1, n + 1):
        a = i
        b = i % 5 + 1
        c = (i // 2) % 7 + 1
        s = f"({a}+{b})/{c}"
        strings.append(s)
    return strings

def main(n):
    s = []
    f = {}
    input_strings = generate_input_strings(n)
    for i in range(n):
        ss = input_strings[i]
        value = val(ss)
        s.append(value)
        if value not in f:
            f[value] = 1
        else:
            f[value] += 1
    for i in range(len(s)):
        print(f[s[i]], end=" ")
    print()

if __name__ == "__main__":
    main(10)