import requests
from bs4 import BeautifulSoup
import json
import time
import random
from typing import Dict, List
import os

class CodeforceScraper:
    def __init__(self):
        self.base_url = "https://codeforces.com"
        self.session = requests.Session()
        
        # 添加多个 User-Agent
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0'
        ]
        
        # 添加随机延迟
        self.min_delay = 2
        self.max_delay = 5
    
    def _update_headers(self):
        """更新请求头"""
        self.session.headers.update({
            'User-Agent': random.choice(self.user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'Referer': 'https://codeforces.com/problemset',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1'
        })
        
    def get_problemset_list(self, page: int = 1) -> List[Dict]:
        """获取题目列表（使用 Codeforces API）"""
        # 在请求之前添加随机延迟
        time.sleep(random.uniform(self.min_delay, self.max_delay))
        
        # 更新请求头，使用更简单的请求头
        self.session.headers.update({
            'User-Agent': random.choice(self.user_agents),
            'Accept': 'application/json',
            'Accept-Language': 'en-US,en;q=0.9'
        })
        
        url = "https://codeforces.com/api/problemset.problems"
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            try:
                data = response.json()
            except json.JSONDecodeError as e:
                print(f"解析 API 响应失败: {e}\n响应内容: {response.text[:200]}...")
                return []
            
            if data.get('status') != 'OK':
                print(f"API 请求失败: {data.get('status')}\n错误信息: {data.get('comment', '未知错误')}")
                return []
            
            if 'result' not in data or 'problems' not in data['result']:
                print(f"API 响应格式不正确: {data}")
                return []
            
            problems = []
            for problem in data['result']['problems']:
                if 'contestId' in problem and 'index' in problem:
                    problems.append({
                        'id': f"{problem['contestId']}{problem['index']}",
                        'name': problem.get('name', 'Unknown'),
                        'url': f"{self.base_url}/problemset/problem/{problem['contestId']}/{problem['index']}",
                        'tags': problem.get('tags', []),
                        'difficulty': str(problem.get('rating', 'Unknown'))
                    })
            
            return problems
        except Exception as e:
            print(f"获取题目列表失败 (页面 {page}): {e}")
            return []
    
    def scrape_problem_detail(self, problem_url: str) -> Dict:
        """爬取单个题目的详细信息"""
        try:
            response = self.session.get(problem_url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            problem_statement = soup.find('div', class_='problem-statement')
            if not problem_statement:
                return None
            
            # 提取基本信息
            header = problem_statement.find('div', class_='header')
            title = header.find('div', class_='title').text.strip()
            
            time_limit = header.find('div', class_='time-limit').text.strip()
            memory_limit = header.find('div', class_='memory-limit').text.strip()
            input_file = header.find('div', class_='input-file').text.strip()
            output_file = header.find('div', class_='output-file').text.strip()
            
            # 提取题目描述部分
            sections = problem_statement.find_all('div', recursive=False)
            
            problem_description = ""
            input_spec = ""
            output_spec = ""
            note = ""
            
            for section in sections:
                if 'class' not in section.attrs:
                    # 题目描述（没有class的第一个div）
                    paragraphs = section.find_all(['p', 'pre'])
                    problem_description = '\n'.join([p.get_text(strip=True) for p in paragraphs])
                elif 'input-specification' in section.get('class', []):
                    input_spec = section.get_text(strip=True).replace('Input', '', 1).strip()
                elif 'output-specification' in section.get('class', []):
                    output_spec = section.get_text(strip=True).replace('Output', '', 1).strip()
                elif 'note' in section.get('class', []):
                    note = section.get_text(strip=True).replace('Note', '', 1).strip()
            
            # 提取样例测试
            sample_tests = []
            sample_test_div = problem_statement.find('div', class_='sample-tests')
            if sample_test_div:
                inputs = sample_test_div.find_all('div', class_='input')
                outputs = sample_test_div.find_all('div', class_='output')
                
                for inp, out in zip(inputs, outputs):
                    input_pre = inp.find('pre')
                    output_pre = out.find('pre')
                    if input_pre and output_pre:
                        sample_tests.append({
                            'input': input_pre.get_text(strip=False),
                            'output': output_pre.get_text(strip=False)
                        })
            
            return {
                'url': problem_url,
                'title': title,
                'time_limit': time_limit,
                'memory_limit': memory_limit,
                'input_file': input_file,
                'output_file': output_file,
                'description': problem_description,
                'input_specification': input_spec,
                'output_specification': output_spec,
                'sample_tests': sample_tests,
                'note': note
            }
            
        except Exception as e:
            print(f"爬取题目详情失败 {problem_url}: {e}")
            return None
    
    def scrape_problems(self, target_count: int = 2000, output_file: str = 'codeforces_problems.json'):
        """爬取指定数量的题目"""
        all_problems = []
        page = 1
        
        # 如果已存在文件，先加载已有数据
        if os.path.exists(output_file):
            with open(output_file, 'r', encoding='utf-8') as f:
                all_problems = json.load(f)
            print(f"已加载 {len(all_problems)} 道题目")
        
        while len(all_problems) < target_count:
            print(f"\n正在爬取第 {page} 页...")
            problem_list = self.get_problemset_list(page)
            
            if not problem_list:
                print("没有更多题目了")
                break
            
            for problem in problem_list:
                if len(all_problems) >= target_count:
                    break
                
                print(f"正在爬取: {problem['id']} - {problem['name']}")
                detail = self.scrape_problem_detail(problem['url'])
                
                if detail:
                    detail['problem_id'] = problem['id']
                    all_problems.append(detail)
                    print(f"成功! 已爬取 {len(all_problems)}/{target_count}")
                    
                    # 每爬取10道题保存一次
                    if len(all_problems) % 10 == 0:
                        with open(output_file, 'w', encoding='utf-8') as f:
                            json.dump(all_problems, f, ensure_ascii=False, indent=2)
                        print(f"已保存到 {output_file}")
                
                # 随机延迟，避免请求过快
                time.sleep(random.uniform(1, 3))
            
            page += 1
        
        # 最终保存
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(all_problems, f, ensure_ascii=False, indent=2)
        
        print(f"\n爬取完成! 共 {len(all_problems)} 道题目")
        print(f"数据已保存到: {output_file}")
        
        return all_problems


def main():
    scraper = CodeforceScraper()
    
    # 爬取2000道题目
    problems = scraper.scrape_problems(target_count=2000, output_file='codeforces_problems.json')
    
    # 打印统计信息
    print(f"\n统计信息:")
    print(f"总题目数: {len(problems)}")
    if problems:
        print(f"\n第一道题示例:")
        print(json.dumps(problems[0], ensure_ascii=False, indent=2)[:500] + "...")


if __name__ == "__main__":
    main()