import requests
import json  # 添加这一行来导入json模块
from bs4 import BeautifulSoup
import time
import os
BASE_URL = "https://luogu.com.cn"   # ✅ 替换成实际网站的根网址
LIST_PAGE_URL = f"https://www.luogu.com.cn/problem/list?type=luogu&page=1&tag=302"   # ✅ 替换成含有 row-wrap 的页面
SAVE_DIR = "problems"  # 抓取的题目详情页保存路径

def fetch_problem_links_with_selenium():
    try:
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.chrome.options import Options
        # 设置Chrome选项
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # 无头模式
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=chrome_options)
        url = "https://www.luogu.com.cn/problem/list?type=luogu&page=1&tag=302"
        driver.get(url)
        
        # 等待页面加载
        time.sleep(3)
        
        # 获取页面源码
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        # 查找题目链接
        links = []
        for wrap in soup.find_all("div", class_="row-wrap"):
            rows = wrap.find_all("div", class_="row")
            for row in rows:
                title_div = row.find("div", class_="title")
                if title_div:
                    a_tag = title_div.find("a", href=True)
                    if a_tag:
                        href = a_tag["href"]
                        # 拼完整链接
                        if href.startswith("/"):
                            href = BASE_URL + href
                        links.append(href)
        driver.quit()
        return links
        
    except ImportError:
        print("Selenium未安装，跳过Selenium方法")
        return []
    except Exception as e:
        print(f"Selenium方法失败: {e}")
        return []

def save_page_content(url, save_dir):
    try:
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.chrome.options import Options
        
        # 设置Chrome选项
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # 无头模式
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        
        # 等待页面加载
        time.sleep(3)
        
        # 获取页面源码
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        
        # 提取页面内容
        problem_data = extract_problem_content(soup)
        
        if problem_data is None:
            print(f"提取页面内容失败: {url}")
            driver.quit()
            return
        
        # 生成文件名
        # 从URL中提取题目ID（如P1393）
        problem_id = url.split("/")[-1]
        if not problem_id:  # 如果URL以/结尾，取倒数第二个
            problem_id = url.split("/")[-2]
        
        file_name = f"{problem_id}.json"
        file_path = os.path.join(save_dir, file_name)
        
        # 保存为JSON格式
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(problem_data, f, ensure_ascii=False, indent=2)
        
        print(f"页面内容已保存到: {file_path}")
        driver.quit()
        
    except Exception as e:
        print(f"保存页面内容失败: {e}")
        if 'driver' in locals():
            driver.quit()

def extract_problem_content(soup):
    """
    从洛谷题目页面的soup中提取题目各个部分的内容
    """
    problem_data = {}
    
    try:
        # 1. 获取题目标题
        title_element = soup.find('h1', class_='lfe-h1')
        if title_element:
            problem_data["title"] = title_element.get_text(strip=True)
        else:
            # 尝试其他可能的标题选择器
            title_element = soup.find('h1')
            if title_element:
                problem_data["title"] = title_element.get_text(strip=True)
            else:
                problem_data['title'] = "未找到标题"
        
        print(f"题目标题: {problem_data['title']}")
        
        # 2. 获取题目背景
        background_section = soup.find('h2', string=lambda text: text and "题目背景" in text)
        if background_section:
            background_content = background_section.find_next('div', class_='lfe-marked-wrap')
            if background_content:
                problem_data['background'] = background_content.get_text(strip=True)
                print("题目背景:")
                print(problem_data['background'][:200] + "..." if len(problem_data['background']) > 200 else problem_data['background'])
            else:
                problem_data['background'] = "未找到题目背景内容"
        else:
            problem_data['background'] = ""  # 如果没有背景，设置为空字符串
            print("未找到题目背景")
        
        # 3. 获取题目描述
        description_section = soup.find('h2', string=lambda text: text and "题目描述" in text)
        if description_section:
            description_content = description_section.find_next('div', class_='lfe-marked-wrap')
            if description_content:
                problem_data['description'] = description_content.get_text(strip=True)
                print("\n题目描述:")
                print(problem_data['description'][:200] + "..." if len(problem_data['description']) > 200 else problem_data['description'])
            else:
                problem_data['description'] = "未找到题目描述内容"
        else:
            problem_data['description'] = "未找到题目描述标题"
        
        # 4. 获取输入格式
        input_format_section = soup.find('h2', string=lambda text: text and '输入格式' in text)
        if input_format_section:
            input_content = input_format_section.find_next('div', class_='lfe-marked-wrap')
            if input_content:
                problem_data['input_format'] = input_content.get_text(strip=True)
                print("\n输入格式:")
                print(problem_data['input_format'][:200] + "..." if len(problem_data['input_format']) > 200 else problem_data['input_format'])
            else:
                problem_data['input_format'] = "未找到输入格式内容"
        else:
            problem_data['input_format'] = "未找到输入格式标题"
        
        # 5. 获取输出格式
        output_format_section = soup.find('h2', string=lambda text: text and '输出格式' in text)
        if output_format_section:
            output_content = output_format_section.find_next('div', class_='lfe-marked-wrap')
            if output_content:
                problem_data['output_format'] = output_content.get_text(strip=True)
                print("\n输出格式:")
                print(problem_data['output_format'][:200] + "..." if len(problem_data['output_format']) > 200 else problem_data['output_format'])
            else:
                problem_data['output_format'] = "未找到输出格式内容"
        else:
            problem_data['output_format'] = "未找到输出格式标题"
        
        # 6. 获取输入输出样例（修改后的部分）
        sample_section = soup.find('h2', string=lambda text: text and '输入输出样例' in text)
        if sample_section:
            sample_block = sample_section.find_next('div', class_='io-sample')
            if sample_block:
                # 获取所有样例块
                sample_blocks = sample_block.find_all('div', class_='io-sample-block')
                samples = []
                
                current_sample = {}
                
                for i, block in enumerate(sample_blocks):
                    caption = block.find('p', class_='lfe-caption')
                    code_block = block.find('pre', class_='lfe-code')
                    
                    if caption and code_block:
                        caption_text = caption.get_text(strip=True)
                        code_text = code_block.get_text(strip=True)
                        
                        if '输入' in caption_text:
                            # 如果当前已有样例且包含output，先保存
                            if current_sample and 'output' in current_sample:
                                samples.append(current_sample)
                                current_sample = {}
                            
                            # 开始新的输入样例
                            current_sample['input'] = code_text
                            
                        elif '输出' in caption_text:
                            # 添加输出到当前样例
                            current_sample['output'] = code_text
                
                # 添加最后一个样例（如果存在）
                if current_sample:
                    samples.append(current_sample)
                
                problem_data['samples'] = samples
                print("\n输入输出样例:")
                for i, sample in enumerate(samples):
                    print(f"样例 {i+1} - 输入:")
                    print(sample['input'])
                    if 'output' in sample:
                        print(f"样例 {i+1} - 输出:")
                        print(sample['output'])
            else:
                problem_data['samples'] = []
        else:
            problem_data['samples'] = []
            print("\n未找到输入输出样例")
        
        # 7. 获取说明/提示
        hint_section = soup.find('h2', string=lambda text: text and '说明/提示' in text)
        if hint_section:
            hint_content = hint_section.find_next('div', class_='lfe-marked-wrap')
            if hint_content:
                problem_data['hint'] = hint_content.get_text(strip=True)
                print("\n说明/提示:")
                print(problem_data['hint'][:200] + "..." if len(problem_data['hint']) > 200 else problem_data['hint'])
            else:
                problem_data['hint'] = "未找到说明/提示内容"
        else:
            problem_data['hint'] = "未找到说明/提示标题"
        
        return problem_data
        
    except Exception as e:
        print(f"提取题目内容时出错: {e}")
        import traceback
        traceback.print_exc()  # 打印详细错误信息
        return None

if __name__ == '__main__':
    # 方法1：使用requests
    url = "https://www.luogu.com.cn/problem/list?type=luogu&page=1&tag=302"
    links = fetch_problem_links_with_selenium()
    print(f"\n总共获取到 {len(links)} 个链接")
    
    # 保存每个链接的页面内容
    os.makedirs(SAVE_DIR, exist_ok=True)
    for link in links:
        save_page_content(link, SAVE_DIR)

