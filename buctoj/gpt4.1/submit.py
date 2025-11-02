from urllib.parse import urlparse, parse_qs


def submit_code(BASE_URL, session, link, submit_link, code):
    query = urlparse(link).query
    params = parse_qs(query)
    cid = params.get("cid", [None])[0]
    pid = params.get("pid", [None])[0]

    data = {
        "cid": str(cid),
        "pid": str(pid),
        "language": str(1),
        "source": code,
        "submit": "submit"
    }

    headers = {
        "Referer": f"{submit_link}?cid={cid}&pid={pid}&langmask=0",
        "Origin": f"{BASE_URL}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/135 Safari/537.36"
    }

    session.post(submit_link, data=data, headers=headers)
