#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

def main():
    # 加载JSON文件
    with open('/home/wuyankai/myResearch/codeComplex/summarized_results.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"总共找到 {len(data)} 条记录\n")
    
    for i, item in enumerate(data):
        print(f"--- 记录 {i+1}/{len(data)} ---")
        print(f"ID: {item.get('ID', 'N/A')}")
        print(f"Model Raw Output: {item.get('model_raw_output', 'N/A')}")
        print(f"Expected Complexity: {item.get('expected_complexity', 'N/A')}")
        print(f"Problem: {item.get('problem', 'N/A')}")
        print(f"Bestfit Output: {item.get('bestfit_output', 'N/A')}")
        print("\n" + "="*50)
        print("FILTERED DATA:")
        print("="*50)
        print(item.get('filteredData', 'N/A'))
        print("\n" + "="*50)
        print("ONLY CODE:")
        print("="*50)
        print(item.get('onlyCode', 'N/A'))
        print(f"--- 记录 {i+1}/{len(data)} ---")
        print(f"ID: {item.get('ID', 'N/A')}")
        print(f"Model Raw Output: {item.get('model_raw_output', 'N/A')}")
        print(f"Expected Complexity: {item.get('expected_complexity', 'N/A')}")
        print(f"Problem: {item.get('problem', 'N/A')}")
        print(f"Bestfit Output: {item.get('bestfit_output', 'N/A')}")
        # 等待用户按键继续
        input("\n按回车键继续到下一项...")
        print("\n" + "="*80 + "\n")

if __name__ == "__main__":
    main()