import zlib, base64

def original_program():
    exec(zlib.decompress(base64.b64decode(b'eJyFV8lu2zAQPTdfIenAUGhR9FygXxLk4MJu4SJwAscJSIEfX4nLzHtDpT0kGM6+j3w83IYfw8M0BhemL8M0+pBiWuYMBzdGtwjYgMUpWGRWtnFJq6Srkh7g4JqSjW9Jm3wKjdYohIzALkivfuX/m02nYBUJ2ZNVLjZPAM5hrFTR5BFGasLg/RbOvPniIsSU0AXAtMgMnanRShPVFx+QA+jRad5CyWhoMUbIqCBL0RII5jSZd+Fg+sLB7dpNWOItRcaFNKqVyFpKgdkR9ELB2PpzhIJGt1amli/aSDlOQ1W5ymHiJFsYYHCkD0VZsMSmDSMl1XpmYM2R9HtTwgOYgCe3KLwXmJUdMRaiID+w28WKfGVICbfyzMaHNKq36IWCC+Qp7gTLoVYRL+28GH6Pjb7JmDjJ1l6AsDu2CGFzJR5RM58wnDCZ/8it9nlXgzYrihNlNr2dFmUoamj1pv961Y93meJ9B62u0gF2rkXzB3qlJziEzfWuYFHWPJQLSrNZExXlgesBaI1S7dDm4v6AYYZkwNRD40AGaBck3vYLibQi4e7Mpzdhf7YtAgh+loaltc0HVw5zYkuEsS7ggJBtuAiJjOrDswaBanOqF9E6C7ebnO0wdKn5+BjM3k1HOl5245pj1yknlqH5iOnZ4TG5pSsPGSN7oesOHf3AbWGaglqiO/MpdM2Q3zUjZBNwYFBD7Q46XvMWlWxICAFca8Mq7x2nQwpdqS0Pa6nXHaxAQUZTtby1qnH+YLH6sFyySaV6qRYumsLpNS4dRyPdzjkSFitEDDDFtXB6irVwggtgVE55RYBFZW4rWm62iMd91wK4JjOL11vfO9LMUS85aODCdWuK7Mu3g7BkuNqOLKSfJwXMY8k/hxLiokkkR2bGIdiZtTWOCWVgH+1NYMPDXMl+q8siUffUp05hY4Q6alBt8DSSVi3jvlzTAppNKU8dpwppDSokDq2uhenx7tfzdTgP58twPVx+n/z5clv/Xt5ufp7n73efXq4b5ni4PZzeD09++vZzGj4P9/df/zyfL/7p/Hrz19P76fp6OqrcPD/Od38BvToehw==')))

def generate_input(n):
    # 原程序期望：第一行一个整数 n，第二行 n 个整数
    # 这里用确定性序列 1..n 作为第二行
    first_line = str(n)
    second_line = " ".join(str(i) for i in range(1, n + 1))
    data = first_line + "\n" + second_line + "\n"
    return data

def patched_input_factory(data_lines):
    it = iter(data_lines)
    def _input(prompt=None):
        try:
            return next(it)
        except StopIteration:
            return ""
    return _input

def main(n):
    data = generate_input(n)
    lines = data.splitlines()
    global input
    old_input = input
    input = patched_input_factory(lines)
    try:
        original_program()
    finally:
        input = old_input

if __name__ == "__main__":
    main(1000)