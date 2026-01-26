def decimal_to_26(num):
    num = int(num)
    res = ''
    while num:
        mod = num % 26
        if mod == 0:
            res = 'Z' + res
            num = num // 26 - 1

        else:
            num //= 26
            res = chr(mod + 64) + res
    return res

def RXCY_to_Excel(c, r):
    new_row = decimal_to_26(r)
    return new_row + str(c)

def excel_to_RXCY(s):
    # s is like "AB12"
    # find first digit position
    num_start = 0
    for k in range(len(s)):
        if s[k].isdigit():
            num_start = k
            break
    col_letters = s[:num_start]
    row_part = s[num_start:]
    # convert column letters to number
    row_num = 0
    length = len(col_letters)
    for m in range(length):
        row_num += (26 ** (length - 1 - m)) * (ord(col_letters[m]) - 64)
    return "R" + row_part + "C" + str(row_num)

def detect_format(s):
    di_index = []
    al_index = []
    temp = s
    i = s
    for j in range(len(i)):
        if i[j].isalpha():
            al_index.append(j)
            i = i.replace(i[j], ' ')
        elif i[j].isdigit():
            di_index.append(j)
            i = i.replace(i[j], ' ')
    if not di_index or not al_index:
        return None
    if min(di_index) < max(al_index):
        return "RXCY"

    else:
        return "EXCEL"

def convert_line(i):
    di_index = []
    al_index = []
    temp = i
    for j in range(len(i)):
        if i[j].isalpha():
            al_index.append(j)
            i = i.replace(i[j], ' ')
        elif i[j].isdigit():
            di_index.append(j)
            i = i.replace(i[j], ' ')
    i = temp
    if not di_index or not al_index:
        return ""
    if min(di_index) < max(al_index):  # RxxCxx
        row = int(i[1:i.index('C')])
        col = int(i[i.index('C') + 1:])
        return RXCY_to_Excel(row, col)
    else:  # COL + ROW
        row_num = 0
        for k in range(len(i)):
            if i[k].isdigit():
                num_start = k
                break
        length = len(i[0:k])
        for m in range(num_start):
            row_num += 26 ** (length - 1) * (ord(i[m]) - 64) or (ord(i[m]) - 64)
            length -= 1
        return 'R' + i[num_start:] + 'C' + str(row_num)

def generate_inputs(n):
    # Deterministically generate a mix of RXCY and Excel-like inputs.
    inputs = []
    for idx in range(1, n + 1):
        if idx % 2 == 0:
            # RXCY form: RrowCcol
            row = idx
            col = idx * 2
            inputs.append(f"R{row}C{col}")

        else:
            # Excel form: letters + digits
            # Use idx to derive row and column deterministically
            row = idx + 10
            col = idx
            excel_col = decimal_to_26(col)
            inputs.append(f"{excel_col}{row}")
    return inputs

def main(n):
    lines = generate_inputs(n)
    outputs = []
    for line in lines:
        res = convert_line(line)
        outputs.append(res)
    # For experimental setting, print all outputs to keep behavior similar
    for out in outputs:
        # print(out)
        pass
if __name__ == "__main__":
    main(10)