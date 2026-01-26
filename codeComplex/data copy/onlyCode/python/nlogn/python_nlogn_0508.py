a = input().split()
b = [int(i) for i in a]
inputs = []
diff = []
sinComprimir = 0
for i in range(b[0]):
    input1 = input().split()
    input2 = [int(i) for i in input1]
    inputs.append(input2)

comprimido = 0
for k in range(len(inputs)):
    sinComprimir = sinComprimir + inputs[k][0]
    diff.append(inputs[k][0] - inputs[k][1])
    comprimido = comprimido + inputs[k][1] 

difference = sorted(diff)
invDifference = difference[::-1]
newTotal = sinComprimir
iteraciones = 0
iterador = 0
if sinComprimir <= b[1]:
    print("0")
elif comprimido > b[1]:
    print("-1")
else:
    while newTotal > b[1]:
        iterador = iterador + 1
        newTotal = newTotal - invDifference[iterador-1] 
        iteraciones += 1
    print(iteraciones)