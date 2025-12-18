def main():
    # import sys
    # input = sys.stdin.readline

    a = input()
    b = input()
    if len(a) < len(b):
        a = list(a)
        a.sort(reverse=True)
        print(''.join(a))
        return

    def solve(i, a: list):
        if i == len(b):
            return ''
        if a.__contains__(b[i]):
            a.remove(b[i])
            suf = solve(i+1, a)
            if suf is not None:
                return b[i] + suf
            a.append(b[i])
        best = ''
        for c in a:
            if c < b[i] and c > best:
                best = c
        if best == '':
            return None
        a.remove(best)
        a.sort(reverse=True)
        return best + ''.join(a)

    a = list(a)
    print(solve(0, a))

main()