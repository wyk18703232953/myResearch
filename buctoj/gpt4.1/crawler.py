import hashlib
import os

import requests
from bs4 import BeautifulSoup

def encrypt_with_md5(input_text):
    return hashlib.md5(input_text.encode('utf-8')).hexdigest()

def perform_login(login_page_url, login_process_url, http_session, user_id, user_password):
    try:
        # 访问登录页，获取 CSRF token
        login_page_response = http_session.get(login_page_url)
        soup = BeautifulSoup(login_page_response.text, 'html.parser')
        csrf_input = soup.find('input', {'name': 'csrf'})
        csrf_token = csrf_input['value'] if csrf_input else ''

        # 构造登录表单
        login_form_data = {
            'user_id': user_id,
            'password': encrypt_with_md5(user_password),  # 模拟 jsMd5
            'csrf': csrf_token
        }

        # 提交表单
        response = http_session.post(login_process_url, data=login_form_data)

        # 登录成功检测（可根据实际 HTML 特征判断）
        if "UserName or Password Wrong!" not in response.text:
            print("✅ 登录成功")
            return True
        else:
            print("❌ 登录失败，页面中未发现登录成功标识")
            return False

    except Exception as e:
        print("⚠️ 登录异常：", e)
        return False

def fetch_problem_links(oj_base_url, contest_id, http_session, contest_page_url):
    # 获取页面内容
    print("contest_page_url"+contest_page_url)
    response = http_session.get(contest_page_url)
    response.encoding = response.apparent_encoding
    if response.status_code != 200:
        print(f"无法访问页面，状态码：{response.status_code}")
        return

    # 解析 HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    print("soup"+response.text)
    # 提取题目链接：在表格中查找所有 href 形如 problem.php?cid=3966&pid=0 的链接
    unique_problem_links = []
    problem_details_list = []
    for link_element in soup.select("table.ui.table a[href^='problem.php?id=']"):
        relative_link = link_element.get('href')
        full_link = oj_base_url + relative_link
        if full_link not in unique_problem_links:
            unique_problem_links.append(full_link)

    print(f"共找到 {len(unique_problem_links)} 道题目。")

    # 创建保存文件的文件夹
    output_folder = f"problems_{contest_id}"
    os.makedirs(output_folder, exist_ok=True)

    # 遍历每个题目链接（你可以在这里拓展对每个题目的操作）
    for index, link in enumerate(unique_problem_links, start=1):
        # print(f"第{index}题链接：{link}")
        try:
            problem_data = extract_problem_info(http_session, link)
            for key in problem_data:
                if problem_data[key] is None:
                    problem_data[key] = ""

            problem_description = (
                    f"链接：{link}\n\n" +
                    "题目描述：\n" + problem_data["description"] + "\n" +
                    "输入：\n" + problem_data["input_description"] + "\n" +
                    "输出：\n" + problem_data["output_description"] + "\n" +
                    "样例输入：\n" + problem_data["sample_input"] + "\n" +
                    "样例输出：\n" + problem_data["sample_output"] + "\n" +
                    "提示：\n" + problem_data["hint"]
            )

            non_empty_lines = [line for line in problem_description.splitlines() if line.strip()]
            formatted_problem = "\n".join(non_empty_lines)

            # 写入文件
            file_name = f"Problem{index}.txt"
            file_path = os.path.join(output_folder, file_name)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(formatted_problem)

            problem_details_list.append([link, formatted_problem])
        except Exception as e:
            print(f"处理第 {index} 题时出错: {e}")

    print(f"所有题目已保存到文件夹：{output_folder}")
    return problem_details_list

def extract_problem_info(http_session, problem_url):
    response = http_session.get(problem_url)
    if response.status_code != 200:
        raise Exception(f"请求失败，状态码: {response.status_code}")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 标题
    title = soup.find('h1', class_='ui header').text.strip()
    
    # 描述
    description = soup.find('div', class_='ui bottom attached segment font-content').text.strip()
    
    # 样例输入
    sample_input_element = next(
        (header for header in soup.find_all('h4') if '样例输入' in header.get_text(strip=True)),
        None
    )
    if sample_input_element:
        code_block = sample_input_element.find_next('div', class_='ui bottom attached segment font-content').find('code')
        sample_input = code_block.text.strip() if code_block else '未找到'
    else:
        sample_input = '未找到'
    
    # 样例输出
    sample_output_element = next(
        (header for header in soup.find_all('h4') if '样例输出' in header.get_text(strip=True)),
        None
    )
    if sample_output_element:
        code_block = sample_output_element.find_next('div', class_='ui bottom attached segment font-content').find('code')
        sample_output = code_block.text.strip() if code_block else '未找到'
    else:
        sample_output = '未找到'
    
    # 提示
    hint_element = soup.find('h4', class_='ui top attached block header', string='提示')
    if hint_element:
        hint_div = hint_element.find_next('div', class_='ui bottom attached segment font-content')
        hint = hint_div.get_text(strip=True) if hint_div else '未找到'
    else:
        hint = '未找到'
    
    # 输入说明
    input_header = soup.find('h4', string=lambda s: s and '输入' in s)
    if input_header:
        input_div = input_header.find_next_sibling('div', class_='ui bottom attached segment font-content')
        if input_div:
            paragraphs = input_div.find_all('p')
            input_description = '\n'.join(
                p.get_text(strip=True) for p in paragraphs) if paragraphs else input_div.get_text(strip=True)
        else:
            input_description = '未找到'
    else:
        input_description = '未找到'
    
    # 输出说明
    output_header = soup.find('h4', string=lambda s: s and '输出' in s)
    if output_header:
        output_div = output_header.find_next_sibling('div', class_='ui bottom attached segment font-content')
        if output_div:
            paragraphs = output_div.find_all('p')
            output_description = '\n'.join(
                p.get_text(strip=True) for p in paragraphs) if paragraphs else output_div.get_text(strip=True)
        else:
            output_description = '未找到'
    else:
        output_description = '未找到'
    
    return {
        'title': title,
        'description': description,
        'sample_input': sample_input,
        'sample_output': sample_output,
        'hint': hint,
        'input_description': input_description,
        'output_description': output_description,
    }
