from math import factorial as fact

def generate_strings(n):
    half = n // 2
    a = ''.join('+' if i % 2 == 0 else '-' for i in range(n))
    b = ''
    for i in range(n):
        if i < half:
            b += '+' if i % 3 == 0 else '-'
        else:
            b += '?'
    return a, b

def core_logic(a, b):
    aplus = a.count('+')
    aminus = len(a) - aplus

    bplus = b.count('+')
    bminus = b.count('-')
    bjolly = len(b) - bplus - bminus

    if bplus > aplus or bminus > aminus:
        return 0
    c = aplus - bplus
    res = fact(bjolly) / fact(bjolly - c) / fact(c) / 2**bjolly
    return res

def main(n):
    if n <= 0:
        return 0
    a, b = generate_strings(n)
    result = core_logic(a, b)
    print(result)
    return result

if __name__ == "__main__":
    main(10)