input_1 = input()
input_2 = input()

line_1 = [i for i in str(input_1)]
line_2 = [i for i in str(input_2)]

no = 0
for i in range(len(line_1) - 1):
    if line_1[i] != 'X' and line_2[i] != 'X':
        if line_1[i + 1] != 'X':
            no += 1
            line_1[i] = 'X'
            line_2[i] = 'X'
            line_1[i + 1] = 'X'

        elif line_2[i + 1] != 'X':
            no += 1
            line_1[i] = 'X'
            line_2[i] = 'X'
            line_2[i + 1] = 'X'

    elif line_1[i] != 'X' and line_1[i + 1] != 'X' and line_2[i + 1] != 'X':
        no += 1
        line_1[i] = 'X'
        line_1[i + 1] = 'X'
        line_2[i + 1] = 'X'

    elif line_2[i] != 'X' and line_1[i + 1] != 'X' and line_2[i + 1] != 'X':
        no += 1
        line_2[i] = 'X'
        line_1[i + 1] = 'X'
        line_2[i + 1] = 'X'

print(no)

            

            
        