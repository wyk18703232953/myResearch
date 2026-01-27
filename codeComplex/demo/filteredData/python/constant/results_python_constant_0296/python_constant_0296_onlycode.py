# A. Paper Airplanes

k, n, s, p = map(int, input().split())

sheets = (n + s - 1) // s

print((sheets * k + p - 1) // p)

