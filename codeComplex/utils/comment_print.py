import os
import re

def process_file(file_path):
    """处理单个Python文件，将所有print语句加上注释并添加pass"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 使用正则表达式匹配未被注释的print语句，并且保留缩进
        # 匹配模式：以0个或多个空格/tab开头，然后是print(...)，不匹配已被注释的print
        pattern = r'^(\s*)(?!#)(print\((.*?)\))(\s*)(#.*)?$'
        
        # 首先处理所有未被注释的print语句
        lines = content.split('\n')
        new_lines = []
        
        for line in lines:
            # 检查是否包含未被注释的print语句
            match = re.match(pattern, line)
            if match:
                indent = match.group(1)
                full_print = match.group(2)
                print_content = match.group(3)
                trailing_whitespace = match.group(4)
                existing_comment = match.group(5) or ''
                
                # 构建替换后的内容：注释掉print语句并添加pass
                # 确保保留相同的缩进
                new_lines.append(f'{indent}# {full_print}{existing_comment}{trailing_whitespace}')
                new_lines.append(f'{indent}pass')
            else:
                # 没有print语句，直接添加原行
                new_lines.append(line)
        
        # 合并所有行
        new_content = '\n'.join(new_lines)
        
        # 修复可能的重复pass问题（包括连续的passpass和多行pass）
        new_content = re.sub(r'(\s*)pass(?:\s*pass)+', r'\1pass', new_content)  # 处理连续的passpass
        new_content = re.sub(r'(\s*)pass\n\s*pass', r'\1pass', new_content)  # 处理换行分隔的pass
        
        # 修复可能的格式问题：确保pass和else/elif/if之间有空格和换行
        # 匹配pass后面直接跟着else/elif/if的情况（包括同一行或不同行但没有换行）
        # 确保只匹配相同缩进级别的pass和控制流语句
        new_content = re.sub(r'(\s*)pass\s*(\1(else|elif|if))', r'\1pass\n\2', new_content)
        # 修复连续的pass问题（再次处理，确保所有情况都被覆盖）
        new_content = re.sub(r'pass(?:\s*pass)+', r'pass', new_content)  # 处理任意空格分隔的连续pass
        # 修复缩进问题，确保每个语句都有正确的缩进
        # 只在控制流语句前面添加换行，如果它前面没有空行的话
        lines = new_content.split('\n')
        new_lines = []
        
        for i, line in enumerate(lines):
            if line.strip() in ['else:', 'elif:', 'if:']:
                # 检查前一行是否已经是空行
                if i > 0 and lines[i-1].strip() != '':
                    new_lines.append('')
            new_lines.append(line)
        
        new_content = '\n'.join(new_lines)
        
        # 保存修改后的内容
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Processed: {file_path}")
        return True
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """主函数，遍历目录并处理所有Python文件"""
    target_dir = r"/home/wuyankai/myResearch/codeComplex/data/filteredData/python/cubic"
    
    if not os.path.exists(target_dir):
        print(f"Directory not found: {target_dir}")
        return
    
    processed_count = 0
    error_count = 0
    
    # 遍历目录及其子目录
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                if process_file(file_path):
                    processed_count += 1
                else:
                    error_count += 1
    
    print(f"\nProcessing complete!")
    print(f"Files processed: {processed_count}")
    print(f"Files with errors: {error_count}")

if __name__ == "__main__":
    main()
