import json
import ast
import re
from collections import defaultdict

class CodeDifficultyAssessor:
    def __init__(self):
        # 难度评估规则权重
        self.weights = {
            'code_length': 0.15,
            'function_count': 0.10,
            'control_flow_complexity': 0.20,
            'algorithm_complexity': 0.25,
            'data_structures': 0.15,
            'language_features': 0.10,
            'math_complexity': 0.05
        }
        
        # 算法复杂度映射到分数 (0-5)
        self.algorithm_scores = {
            'constant': 0,
            'logarithmic': 1,
            'linear': 2,
            'linearithmic': 3,
            'quadratic': 4,
            'cubic': 5,
            'exponential': 5
        }
        
        # 复杂数据结构列表
        self.complex_data_structures = ['heapq', 'bisect', 'collections.deque', 'collections.defaultdict', 
                                       'collections.OrderedDict', 'set', 'dict', 'list', 'tuple']
        
        # 高级语言特性
        self.advanced_features = ['decorator', 'generator', 'comprehension', 'lambda', 'async', 
                                 'await', 'contextmanager', 'metaclass']
    
    def assess_difficulty(self, code):
        """评估代码难度，返回0-10的难度分数"""
        try:
            # 解析代码
            tree = ast.parse(code)
            
            # 1. 代码长度评估
            code_length_score = self._assess_code_length(code)
            
            # 2. 函数数量评估
            function_count_score = self._assess_function_count(tree)
            
            # 3. 控制流复杂度评估
            control_flow_score = self._assess_control_flow(tree)
            
            # 4. 算法复杂度评估 - 从代码结构推断
            algorithm_score = self._infer_algorithm_complexity(tree, code)
            
            # 5. 数据结构使用评估
            data_structures_score = self._assess_data_structures(code)
            
            # 6. 高级语言特性评估
            language_features_score = self._assess_language_features(tree)
            
            # 7. 数学复杂度评估
            math_score = self._assess_math_complexity(code)
            
            # 计算加权总分
            total_score = (
                code_length_score * self.weights['code_length'] +
                function_count_score * self.weights['function_count'] +
                control_flow_score * self.weights['control_flow_complexity'] +
                algorithm_score * self.weights['algorithm_complexity'] +
                data_structures_score * self.weights['data_structures'] +
                language_features_score * self.weights['language_features'] +
                math_score * self.weights['math_complexity']
            )
            
            # 转换为0-10的分数
            final_score = min(10, max(0, round(total_score * 2)))
            
            return {
                'difficulty': final_score,
                'breakdown': {
                    'code_length': code_length_score,
                    'function_count': function_count_score,
                    'control_flow': control_flow_score,
                    'algorithm': algorithm_score,
                    'data_structures': data_structures_score,
                    'language_features': language_features_score,
                    'math_complexity': math_score
                }
            }
        except SyntaxError:
            return {
                'difficulty': -1,
                'error': 'Syntax error in code'
            }
    
    def _assess_code_length(self, code):
        """评估代码长度，返回0-5的分数"""
        lines = code.split('\n')
        non_empty_lines = [line for line in lines if line.strip()]
        line_count = len(non_empty_lines)
        
        if line_count < 10:
            return 0
        elif line_count < 30:
            return 1
        elif line_count < 50:
            return 2
        elif line_count < 100:
            return 3
        elif line_count < 200:
            return 4
        else:
            return 5
    
    def _assess_function_count(self, tree):
        """评估函数数量，返回0-5的分数"""
        function_count = 0
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                function_count += 1
        
        if function_count == 0:
            return 0
        elif function_count == 1:
            return 1
        elif function_count <= 3:
            return 2
        elif function_count <= 5:
            return 3
        elif function_count <= 10:
            return 4
        else:
            return 5
    
    def _assess_control_flow(self, tree):
        """评估控制流复杂度，返回0-5的分数"""
        complexity = 0
        
        for node in ast.walk(tree):
            # 基本控制流结构
            if isinstance(node, (ast.If, ast.While, ast.For, ast.Try, ast.With, ast.Match)):
                complexity += 1
            
            # 嵌套循环或条件
            if isinstance(node, (ast.If, ast.While, ast.For)):
                # 计算嵌套深度
                depth = 0
                parent = ast.iter_child_nodes(node)
                for child in ast.walk(node):
                    if isinstance(child, (ast.If, ast.While, ast.For)):
                        depth += 1
                complexity += depth
        
        if complexity == 0:
            return 0
        elif complexity <= 2:
            return 1
        elif complexity <= 5:
            return 2
        elif complexity <= 10:
            return 3
        elif complexity <= 20:
            return 4
        else:
            return 5
    
    def _infer_algorithm_complexity(self, tree, code):
        """从代码结构推断算法复杂度，返回0-5的分数"""
        complexity = 0
        nested_loops = 0
        loop_count = 0
        
        # 遍历AST计算循环嵌套情况
        for node in ast.walk(tree):
            if isinstance(node, ast.For) or isinstance(node, ast.While):
                loop_count += 1
                # 检查嵌套深度
                depth = 0
                for child in ast.walk(node):
                    if isinstance(child, ast.For) or isinstance(child, ast.While):
                        depth += 1
                if depth > 1:
                    nested_loops += depth - 1
        
        # 根据循环情况推断复杂度
        if loop_count == 0:
            complexity = 0  # 常数复杂度
        elif loop_count == 1:
            complexity = 2  # 线性复杂度
        elif loop_count > 1 and nested_loops == 0:
            complexity = 3  # 线性复杂度（多个独立循环）
        elif nested_loops == 1:
            complexity = 4  # 平方复杂度
        else:
            complexity = 5  # 立方或更高复杂度
        
        # 检查是否包含高级数据结构操作，可能暗示对数或线性对数复杂度
        if any(ds in code for ds in ['heapq', 'bisect', 'sorted', 'sort']):
            if complexity >= 2:
                # 堆操作或二分查找通常是O(n log n)或O(log n)
                complexity = 3  # 线性对数复杂度
        
        return complexity
    
    def _assess_data_structures(self, code):
        """评估数据结构使用复杂度，返回0-5的分数"""
        score = 0
        
        # 检查导入的复杂数据结构
        for ds in self.complex_data_structures:
            if ds in code:
                score += 0.5
        
        # 检查数据结构的使用
        if '[' in code and ']' in code:  # 列表使用
            score += 0.5
        if '{' in code and '}' in code:  # 字典使用
            score += 0.5
        if '(' in code and ')' in code:  # 元组使用
            score += 0.25
        if 'set(' in code:  # 集合使用
            score += 0.5
        
        return min(5, max(0, round(score)))
    
    def _assess_language_features(self, tree):
        """评估高级语言特性的使用，返回0-5的分数"""
        score = 0
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Lambda):
                score += 1
            if isinstance(node, ast.ListComp) or isinstance(node, ast.DictComp) or isinstance(node, ast.SetComp):
                score += 1
            if isinstance(node, ast.GeneratorExp):
                score += 1
            # 检查装饰器（兼容不同Python版本）
            if hasattr(node, 'decorator_list') and node.decorator_list:
                score += 2
            if isinstance(node, ast.AsyncFunctionDef) or isinstance(node, ast.Await):
                score += 2
        
        return min(5, max(0, round(score / 2)))
    
    def _assess_math_complexity(self, code):
        """评估数学复杂度，返回0-5的分数"""
        math_patterns = ['sqrt', 'sin', 'cos', 'tan', 'log', 'exp', 'pow', 'abs', 'max', 'min']
        math_operators = ['**', '*', '/', '//', '%', '+', '-']
        
        score = 0
        
        # 检查数学函数
        for pattern in math_patterns:
            if pattern in code:
                score += 0.5
        
        # 检查复杂数学表达式
        if 'sqrt(' in code or 'pow(' in code or 'log(' in code:
            score += 1
        
        # 检查运算符密度
        operator_count = sum(code.count(op) for op in math_operators)
        if operator_count > 10:
            score += 1
        elif operator_count > 5:
            score += 0.5
        
        return min(5, max(0, round(score)))

def main():
    # 初始化评估器
    assessor = CodeDifficultyAssessor()
    
    # 读取数据集
    input_file = "d:/MyResearch/codeComplex/data/python_data.jsonl"
    output_file = "d:/MyResearch/codeComplex/data/python_data_with_difficulty.jsonl"
    
    with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
        
        line_count = 0
        for line in f_in:
            line_count += 1
            if line_count % 100 == 0:
                print(f"处理了 {line_count} 行")
            
            # 解析JSON
            try:
                data = json.loads(line.strip())
                src = data.get('src', '')
                complexity = data.get('complexity', '')
                
                # 评估难度
                difficulty_result = assessor.assess_difficulty(src)
                
                # 添加难度字段
                data['difficulty'] = difficulty_result['difficulty']
                data['difficulty_breakdown'] = difficulty_result['breakdown']
                
                # 写入输出文件
                f_out.write(json.dumps(data, ensure_ascii=False) + '\n')
            except json.JSONDecodeError as e:
                print(f"JSON解析错误 (第{line_count}行): {e}")
            except Exception as e:
                print(f"处理错误 (第{line_count}行): {e}")
    
    print(f"完成！共处理了 {line_count} 行")
    print(f"输出文件: {output_file}")

if __name__ == "__main__":
    main()