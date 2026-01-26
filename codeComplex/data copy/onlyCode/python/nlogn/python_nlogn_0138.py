n_extnson, n_dvics, n_sokts = list(map(int, input().split()))
extensions = list(map(int, input().split()))
extensions.sort(reverse=True)
devices_left = n_dvics - n_sokts
extnson_used = 0
i = 0
while devices_left > 0 and n_extnson > 0:
    devices_left += 1
    extnson_siez = extensions[i]
    devices_left -= extnson_siez
    extnson_used += 1
    n_extnson -= 1
    i += 1

if devices_left > 0:
    print(-1)
else:
    print(extnson_used)


