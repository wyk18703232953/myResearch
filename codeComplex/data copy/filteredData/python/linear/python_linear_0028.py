n = None

def main(n):
    s = ('H' * n + 'T' * n) * 2
    h = s.count('H') // 2
    result = h - max(s[i:i + h].count('H') for i in range(n))
    # print(result)
    pass
if __name__ == "__main__":
    main(10)