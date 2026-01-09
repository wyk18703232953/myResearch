import sys

def findmin(h, n):
    n.sort()
    h = int(h)
    ans = '-1'
    for i in n:
        if int(i) > h:
            break
        ans = i
    return ans

def original_algorithm(n_str, n1_str):
    n = list(n_str)
    n1 = list(n1_str)
    if len(n) < len(n1):
        n.sort(reverse=True)
        return "".join(n)
    n.sort()
    ans = ""
    f = 0
    for i in range(len(n)):
        t = i - 1
        c = 0
        r = findmin(n1[i], n)
        if r == '-1':
            while r == '-1':
                n.append(ans[-c-1])
                r = findmin(int(n1[t]) - 1, n)
                t -= 1
                c += 1
            ans = ans[:len(ans)-c]
            ans += r
            n.remove(r)
            f = 1
            break
        n.remove(r)
        if r == n1[i]:
            ans += r
            continue

        else:
            ans += r
            f = 1
            break
    if f == 1:
        n.sort(reverse=True)
        for i in n:
            ans += i
    return ans

def main(n):
    if n < 1:
        n = 1
    n_str = "".join(str((i % 10)) for i in range(1, n + 1))
    n1_len = max(1, n // 2)
    n1_str = "".join(str(((i * 3) % 10)) for i in range(1, n1_len + 1))
    result = original_algorithm(n_str, n1_str)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)