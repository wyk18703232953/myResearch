def main():
    from sys import stdin, stdout

    def read():
        return stdin.readline().rstrip('\n')

    def read_array(sep=None, maxsplit=-1):
        return read().split(sep, maxsplit)

    def read_int():
        return int(read())

    def read_int_array(sep=None, maxsplit=-1):
        return [int(a) for a in read_array(sep, maxsplit)]

    def write(*args, **kwargs):
        sep = kwargs.get('sep', ' ')
        end = kwargs.get('end', '\n')
        stdout.write(sep.join(str(a) for a in args) + end)

    def write_array(array, **kwargs):
        sep = kwargs.get('sep', ' ')
        end = kwargs.get('end', '\n')
        stdout.write(sep.join(str(a) for a in array) + end)

    n, m = read_int_array()
    bmin = read_int_array()
    gmax = read_int_array()

    bmin.sort()
    gmax.sort()

    max_boy = bmin[-1]
    min_girl = gmax[0]
    if max_boy > min_girl:
        write(-1)
    elif max_boy == min_girl:
        bmin.pop()
        out = sum(gmax) + sum(x * m for x in bmin)
        write(out)
    else:
        bmin.pop()
        out = sum(gmax) - min_girl + max_boy
        out += min_girl + bmin[-1] * (m-1)
        bmin.pop()
        out += sum(x * m for x in bmin)
        write(out)


main()
