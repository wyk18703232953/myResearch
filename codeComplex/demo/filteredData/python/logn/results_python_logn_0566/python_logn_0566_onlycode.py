k = int(input())

nc = [0 for i in range(14)]

for i in range(1, 14):
    nc[i] += nc[i - 1] + 9 * (10 ** (i - 1)) * i

for i in range(13):
    if nc[i] < k <= nc[i + 1]:
        cif = i + 1

if cif == 1:
    print(k)
    quit()

c = k - nc[cif - 1]

if c % cif == 0:
    nnr = c // cif
    ncif = cif
else:
    nnr = 1 + c // cif
    ncif = c % cif

number = nnr + 10 ** (cif - 1) - 1

while cif != ncif:
    number //= 10
    cif -= 1

print(number % 10)