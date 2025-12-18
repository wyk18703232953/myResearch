num = int(input())
layne = input()
layne = layne.split()
layne = [int(i) for i in layne]
mx = max(layne)
dorf = mx * 2 * num
indx = 1
for i in range(num):
    dor = (layne[i] // num) * num
    if (layne[i] % num) - i > 0:
        dor = dor + num + i + 1
    else:
        dor = dor + i + 1
    if dor < dorf:
        dorf = dor
        indx = i + 1
print(indx)