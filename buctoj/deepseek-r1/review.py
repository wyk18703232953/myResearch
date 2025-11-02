# https://buctoj.com/status.php?problem_id=A&cid=3950
from urllib.parse import urlparse, parse_qs
from bs4 import BeautifulSoup

# 链接：https://www.buctoj.com/problem.php?cid=3922&pid=0

def review_result(BASE_URL,session, link, REVIEW_URL,target_user):
    query = urlparse(link).query
    params = parse_qs(query)
    cid = params.get("cid", [None])[0]
    pid = params.get("pid", [None])[0]
    pid = int(pid) if pid is not None else 0  # 将pid转换为整数类型
    problem_id = chr(ord('A') + pid) if pid < 26 else ''  # pid为0对应A，1对应B，2对应C
    review_url= f"{REVIEW_URL}?problem_id={problem_id}&cid={cid}"
    # print(review_url)
    # headers = {
    #     "Referer": review_url,
    #     "Origin": f"{BASE_URL}",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/135 Safari/537.36"
    # }
    
    response = session.get(review_url)
    response.encoding = response.apparent_encoding
    # print(f"调试: 请求URL: {review_url}")
    # print(f"调试: 响应状态码: {response.status_code}")
    if response.status_code != 200:
        # print(f"无法访问页面，状态码：{response.status_code}")
        return

    # 解析 HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)
    # response=session.get(review_url, headers=headers)
    # print(response.text)  # 打印响应的 HTML 内容，用于调试
   
    table = soup.find('table', id='table')
    submissions = []
    # print(f"调试: 找到表格: {table is not None}")
    
    if not table:
        print("调试: 未找到表格")
        return None, None  # 未找到表格
    
    # 遍历表格中的每一行（除表头）
    for row in table.find_all('tr')[1:]:  # 跳过表头
        try:
            # 提取用户ID
            user_anchor = row.find('a', href=lambda x: x and 'user_id=' in x)
            user_id = user_anchor['href'].split('user_id=')[1].split('#')[0] if user_anchor else None
            # print("user_id:",user_id)
            # 提取提交时间（格式如：2025-05-15 10:26:21）
            td_tags = row.find_all('td')
            if len(td_tags) >= 10:  # 确保至少有10列（根据HTML结构，时间在第10列）
                time_td = td_tags[-1]  # 取最后一个td标签
                submission_time = time_td.find('b').text.strip() if time_td.find('b') else None
            else:
                submission_time = None
            
            # 提取结果状态
            result_anchor = row.find('a', class_=lambda x: x and 'label-' in x)
            result_status = None
            if result_anchor:
                result_class = result_anchor['class'][1]  # 类名如 label-success
                if 'success' in result_class:
                    result_status = True
                else:
                    result_status = False  # 其他状态统一视为错误，可按需细分
            
            # 过滤目标用户\
            # print(f"调试: 检查用户ID: {user_id}, ")
            # print(target_user)
            if user_id.lower() == target_user.lower() and result_status is not None and submission_time is not None:
                # print(f"调试: 找到目标用户提交 - 用户ID: {user_id}, 时间: {submission_time}, 状态: {result_status}")
                submissions.append({
                    'user_id': user_id,
                    'submission_time': submission_time,
                    'status': result_status
                })
                # print(f"调试: 找到目标用户提交 - 用户ID: {user_id}, 时间: {submission_time}, 状态: {result_status}")
        except Exception as e:
            continue
    
    # 按时间倒序排序，取最新提交（第一条）
    if submissions:
        latest_submission = sorted(submissions, key=lambda x: x['submission_time'], reverse=True)[0]
        # print(f"调试: 最新提交 - 用户ID: {latest_submission['user_id']}, 时间: {latest_submission['submission_time']}, 状态: {latest_submission['status']}")
        return latest_submission['status']
    else:
        # print("调试: 未找到该用户的提交记录")
        return None  # 未找到该用户的提交记录