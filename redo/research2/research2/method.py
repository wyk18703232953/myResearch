#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2025 - 2025 heihieyouheihei, Inc. All Rights Reserved 
#
# @Time    : 2025/1/3 下午11:41
# @Author  : 单子叶蚕豆_DzyCd
# @File    : method.py
# @IDE     : PyCharm

from openai import OpenAI
import os
import time
import json


class response:
    def __init__(self):
        self.client = OpenAI(api_key="sk-glL4mhF8GCov9dZiCJLIQ64OvlUpPa2qjLCpnV6zKz4byxXE", base_url="https://yunwu.ai/v1")
        self.name = "gpt-5-nano-2025-08-07"
        self.result = []
        self.input = []

    def read_file(self, file_name):
        self.input.clear()
        with open(file_name, "br") as f:
            msg = f.read().decode()
            # print("msg",msg)
            msg = msg.split("###_###")
            for i in msg:
                if len(i)>20:
                    self.input.append(i)
        print(f"文件已装载！total: {len(self.input)} task(s)")
        time.sleep(1)


    
    # 调用LLM进行答题，后期可以更改这部分代码实现多智能体辩论
    def work_deepseek(self, msg):
        # 添加JSON格式要求到提示词中
        # json_format_prompt = "\n\n请严格按照以下JSON格式返回题解，不要包含任何额外的说明或解释文本：\n{\n\"思路\": \"解题思路的详细描述\",\n\"c++代码\": \"完整的C++代码实现\",\n\"中文代码\": \"中文代码的详细解释\"\n}"
        json_format_prompt = "\n\n请严格按照以下JSON格式返回题解，不要包含任何额外的说明或解释文本：\n{\n\"思路\": \"解题思路的详细描述\",\n\"c++代码\": \"完整的C++代码实现\"}"
        
        full_prompt = msg + json_format_prompt
        
        R = self.client.chat.completions.create(
            model="gpt-5-nano-2025-08-07",
            messages=[{"role": "user", "content": full_prompt}],
            stream=False
        )
        
        p = R.choices[0].message.content
        print("p",p)        
        # 尝试提取JSON内容，移除可能的markdown代码块标记
        if p.startswith('```'):
            # 可能是markdown代码块，尝试提取其中的JSON
            p = p.split('```')[1]
            if p.startswith('json'):
                p = p[4:].strip()
        return p
    
    # 
    # 

    def process(self):
        # os.system('cls')
        print("Running...")
        cnt = 0
        for i in self.input:
            flag = 1
            cnt += 1
            error_cnt = 0
            error_info = ""
            while flag:
                print(f"准备运行 TASK {cnt}/{len(self.input)}>>>{cnt}\n")
                print(f'{int(cnt/len(self.input)*100)}% process>>>', end="")
                try:
                    # 调用LLM获取解答
                    res = self.work_deepseek(i)
                    # print(f"原始响应: {res}")
                    # 保存原始响应到文件
                    result_dir = 'result'
                    if not os.path.exists(result_dir):
                        os.makedirs(result_dir)
                    
                    with open(f'{result_dir}/task_{cnt}.txt', 'w', encoding='utf-8') as f:
                        f.write(res)
                    
                    # 解析JSON格式的响应
                    solution_data = json.loads(res)
                    
                    # 提取解题思路和C++代码
                    approach = solution_data.get("思路", "无法获取思路")
                    code = solution_data.get("c++代码", "无法获取C++代码")
                    
                    # 将代码中的"\n"替换为实际的换行符
                    code = code.replace("\\n", "\n")
                    
                    # 翻译思路为中文
                    # approach_translated = self.translate(approach)
                    
                    # 保存结果到result列表
                    self.result.append({"task": i, "Approach": [approach], "code": code})
                    
                    # 任务完成，退出循环
                    flag = 0
                    print(f"生成成功")
                    
                except json.JSONDecodeError as e:
                    # JSON解析错误
                    error_cnt += 1
                    error_info = f"JSON格式错误: {str(e)}"
                    print(f"{error_info}，重试中... ({error_cnt}/5)")
                    
                    # 如果超出重试次数，记录失败信息并跳过
                    if error_cnt > 5:
                        self.result.append({"task": i, "Approach": ["JSON解析失败", "JSON解析失败"], "code": "---"})
                        print(f"-超出重试范围，跳过TASK {cnt}。错误: {error_info}")
                        time.sleep(1)
                        break
                    
                except Exception as e:
                    # 其他类型的错误
                    error_cnt += 1
                    error_info = f"未知错误: {str(e)}"
                    print(f"{error_info}，重试中... ({error_cnt}/5)")
                    
                    # 如果超出重试次数，记录失败信息并跳过
                    if error_cnt > 5:
                        self.result.append({"task": i, "Approach": ["处理失败", "处理失败"], "code": "---"})
                        print(f"-超出重试范围，跳过TASK {cnt}。错误: {error_info}")
                        time.sleep(1)
                        break
                
                # 重试前短暂暂停，避免请求过于频繁
                if flag and error_cnt < 5:
                    time.sleep(1)

        print("代码生成完成,按回车键继续")

    def show(self):
        for i in self.result:
            # os.system('cls')
            print('--------------------------------------------------------------------------------------------------')
            print(f"QUESTION>>>{i['task']}")
            print(f"思路_zh>>>{i['Approach'][0]}")
            # print(f"思路_zh>>>{i['Approach'][1]}")
            print(f"CODE>>>{i['code']}") 
            print("按回车键继续>>>")
            input()

    def save(self, file_name):
        with open(file_name, "w", encoding="utf-8") as f:
            for i in self.result:
                # 将代码中的"\n"替换为实际的换行符
                code_with_newlines = i['code'].replace("\\n", "\n")
                #削除双引号，转写单引号
                f.write(f"{i['task']}|||{code_with_newlines}|||{i['Approach'][0]}###_###")
        print("文件已保存.")



if __name__ == '__main__':
    model = response()
    print("批量代码生成工具启动...")
    try:
        # 直接执行代码生成流程
        model.read_file("file.txt")
        model.process()
        model.show()
        model.save(file_name="result.txt")
        print("所有操作已完成！")
    except Exception as e:
        print(f"程序执行出错: {str(e)}")
    input("按回车键退出")
