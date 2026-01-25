import sys

inf = 1e10
mod = int(1e9 + 7)

def transform_string(s: str) -> str:
    c = s.count('1')
    c1, i = 0, 0
    # count '0' before first '2'
    while i < len(s) and s[i] != '2':
        if s[i] == '0':
            c1 += 1
        i += 1
    out = []
    out.append('0' * c1)
    out.append('1' * c)
    while i < len(s):
        if s[i] != '1':
            out.append(s[i])
        i += 1
    return ''.join(out)

def generate_input_string(n: int) -> str:
    # Deterministically generate a string over {'0','1','2'} of length n
    # pattern cycles every 3 characters: '0','1','2'
    chars = ['0', '1', '2']
    return ''.join(chars[i % 3] for i in range(n))

def main(n: int):
    # In original program t=1 and a single string s is read.
    # Here n controls the length of s.
    s = generate_input_string(n)
    result = transform_string(s)
    print(result, end="")

if __name__ == "__main__":
    # example: run with n = 10
    main(10)