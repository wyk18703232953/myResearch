import requests

from crawler import login_oj, get_problem_links
from model import get_api
from submit import submit_code

BASE_URL = 'https://www.buctoj.com/'  # 改为你自己的 OJ 域名
LOGIN_PAGE = BASE_URL + 'loginpage.php'  # 登录页地址
LOGIN_URL = BASE_URL + 'login.php'       # 表单提交地址
CID = '3964'
CONTEST_URL = BASE_URL + 'contest.php' + '?cid=' + CID
SUBMIT_URL = BASE_URL + 'submit.php'

USERNAME = 'HappyJoe_bot_1'
PASSWORD = 'HappyJoe520'

if __name__ == "__main__":
    session = requests.Session()
    login_oj(LOGIN_PAGE, LOGIN_URL, session, USERNAME, PASSWORD)
    problems = get_problem_links(BASE_URL, CID, session, CONTEST_URL)

    while(problems.__len__() > 0):
        for i, (link, problem) in enumerate(problems):
            print(f"正在思考。。。正在生成第{i+1}题答案。。。")

            submit_link = SUBMIT_URL

            code = get_api(problem)
            submit_code(BASE_URL, session, link, submit_link, code)

            print(f"已提交第{i+1}题")

        break

