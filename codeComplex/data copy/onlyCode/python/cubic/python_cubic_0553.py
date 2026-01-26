def smallest(d):
    out = ""
    for j in range(0, 10):
        out += ("%d" % j)*d[j]
    return out


def largest(d):
    out = ""
    for j in range(9, -1, -1):
        out += ("%d" % j)*d[j]
    return out


sa = input()
sb = input()
b = int(sb)

h = int(sa)
digits_a = [0]*10
while h > 0:
    digits_a[h % 10] += 1
    h //= 10

out = ""
if len(sb) > len(sa):
    print(largest(digits_a))
    exit()

out = 0
for i in range(len(sa)-1, -1, -1):
    for j in range(9, -1, -1):
        if digits_a[j] == 0:
            continue

        if j < (b % (10 ** (i+1))) // (10 ** i):
            digits_a[j] -= 1
            if out > 0:
                print("{}{}{}".format(out, j, largest(digits_a)))
                exit()
            else:
                print("{}{}".format(j, largest(digits_a)))
                exit()

        if j == (b % (10 ** (i+1))) // (10 ** i):
            if i == 0:
                out = 10*out + j
                print(out)
                exit()
            digits_a[j] -= 1
            if int(smallest(digits_a)) <= b % (10 ** i):
                out = 10*out + j
                break
            else:
                digits_a[j] += 1

print(out)
