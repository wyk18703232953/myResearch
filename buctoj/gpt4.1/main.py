import requests

from crawler import perform_login as login_oj, fetch_problem_links as get_problem_links
from LLM import get_api
from submit import submit_code
from review import review_result

import yaml

with open(r'./config.yaml', 'r') as f:
    config = yaml.safe_load(f)['gpt4.1']

BASE_URL = config['BASE_URL']
LOGIN_PAGE = BASE_URL + config['LOGIN_PAGE']
LOGIN_URL = BASE_URL + config['LOGIN_URL']
CID = config['CID']
CONTEST_URL = f"{BASE_URL}contest.php?cid={CID}"
SUBMIT_URL = BASE_URL + config['SUBMIT_URL']
REVIEW_URL = BASE_URL + config['REVIEW_URL']
USERNAME = config['USERNAME']
PASSWORD = config['PASSWORD']
Retries = config['Retries']

if __name__ == "__main__":
    session = requests.Session()
    login_oj(LOGIN_PAGE, LOGIN_URL, session, USERNAME, PASSWORD)
    problems = get_problem_links(BASE_URL, CID, session, CONTEST_URL)
    # print(problems)
    while(problems.__len__() > 0):
        for i, (link, problem) in enumerate(problems):
            print(f"正在生成第{i+1}题答案")
            cnt = 0
            flag = False
            if(i!=3):
                while cnt < Retries and not flag:
                    # code = get_api(problem, i)
                    # print(code)
                    submit_link = SUBMIT_URL
                    print("submit_link"+submit_link)
                    # submit_code(BASE_URL, session, link, submit_link, code)
                    print(f"已提交第{i+1}题第{cnt+1}次")
                    import time

                    # https: // www.buctoj.com / problem.php?id = 5844  #
                    # https: // www.buctoj.com / submit.php
                    # https://www.buctoj.com/submitpage.php?id=5844
                    # https: // www.buctcoder.com / submitpage.php?id = 5844
                    time.sleep(10+i*5)  # 等待5秒让判题系统处理
                    flag = review_result(BASE_URL, session, link, REVIEW_URL, USERNAME)
                    if flag:
                        print("已通过")
                        break
                    cnt += 1
                    if cnt >= Retries:
                        print(f"已达到最大重试次数{Retries}次，题目{i+1}未通过")
                        break
        break
    # flag = review_result(BASE_URL, session, "https://www.buctoj.com/problem.php?cid=3922&pid=0", REVIEW_URL, USERNAME)
    # if flag:
    #     print("已通过")
    # print(flag)
    # print(type(flag))
        # break
    # cnt += 1
    # if cnt >= Retries:
    #     print(f"已达到最大重试次数{Retries}次，题目{i+1}未通过")
        
