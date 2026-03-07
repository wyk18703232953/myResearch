import os
import ast
import re

# Define complexity categories
COMPLEXITY_CATEGORIES = {
    'constant': ['O(1)'],
    'linear': ['O(n)'],
    'logn': ['O(log n)'],
    'nlogn': ['O(n log n)'],
    'quadratic': ['O(n^2)'],
    'cubic': ['O(n^3)'],
    'np': ['O(2^n)']
}

# Directory structure
data_dir = '/home/wuyankai/myResearch/codeComplex/data/onlyCode/python'
categories = ['constant', 'cubic', 'linear', 'logn', 'nlogn', 'np', 'quadratic']

class TimeComplexityAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.loops = []
        self.recursion = False
        self.logarithmic = False
        self.sort_operations = 0
        self.nested_loops = 0
        self.current_loop_depth = 0
        self.binary_search_pattern = False
        self.loop_variables = set()
        self.loop_increments = {}
        self.has_logarithmic_operation = False
        self.logarithmic_loops = 0
    
    def visit_For(self, node):
        self.current_loop_depth += 1
        
        # Check for loops
        if isinstance(node.iter, ast.Call):
            func = node.iter.func
            if isinstance(func, ast.Name):
                if func.id == 'range':
                    # Check if it's a logarithmic loop (e.g., range(0, n, 2))
                    is_logarithmic = False
                    if len(node.iter.args) > 2:
                        step = node.iter.args[2]
                        if isinstance(step, ast.Constant) and step.value > 1:
                            is_logarithmic = True
                            self.logarithmic = True
                            self.logarithmic_loops += 1
                    # Range-based loop
                    self.loops.append('linear')
                elif func.id in ['sorted', 'sort', 'sorted_list']:
                    # Sorting operations
                    self.sort_operations += 1
                    self.loops.append('nlogn')
                elif func.id in ['reversed', 'enumerate']:
                    # These are linear operations
                    self.loops.append('linear')
        elif isinstance(node.iter, ast.Name):
            # Iterator-based loop
            self.loops.append('linear')
        
        # Track loop variables
        if isinstance(node.target, ast.Name):
            self.loop_variables.add(node.target.id)
        
        self.generic_visit(node)
        self.current_loop_depth -= 1
    
    def visit_While(self, node):
        self.current_loop_depth += 1
        
        # Check for logarithmic patterns in while loops
        if isinstance(node.test, ast.Compare):
            # Look for patterns like i < n and i *= 2 or i /= 2
            has_compare = False
            has_mult_div = False
            loop_var = None
            
            # Extract loop variable from condition
            if isinstance(node.test, ast.Compare):
                if isinstance(node.test.left, ast.Name):
                    loop_var = node.test.left.id
                elif isinstance(node.test.comparators[0], ast.Name):
                    loop_var = node.test.comparators[0].id
            
            for child in ast.walk(node):
                if isinstance(child, ast.Compare):
                    has_compare = True
                if isinstance(child, ast.Assign):
                    for target in child.targets:
                        if isinstance(target, ast.Name):
                            if loop_var and target.id == loop_var:
                                if isinstance(child.value, ast.BinOp):
                                    if isinstance(child.value.op, (ast.Mult, ast.Div)):
                                        # Check if the multiplier/divisor is a constant
                                        if isinstance(child.value.right, ast.Constant):
                                            has_mult_div = True
                                            self.loop_increments[loop_var] = 'exponential'
            
            # If we have both comparison and multiplication/division by constant, it's likely logarithmic
            if has_compare and has_mult_div:
                self.logarithmic = True
                self.has_logarithmic_operation = True
                self.logarithmic_loops += 1
                
                # Check for binary search pattern
                test = node.test
                if isinstance(test, ast.Compare) and len(test.ops) == 1:
                    if isinstance(test.ops[0], (ast.Lt, ast.Le, ast.Gt, ast.Ge)):
                        # Check if there's a midpoint calculation (binary search pattern)
                        for child in ast.walk(node):
                            if isinstance(child, ast.Assign):
                                for target in child.targets:
                                    if isinstance(target, ast.Name) and 'mid' in target.id.lower():
                                        if isinstance(child.value, ast.BinOp):
                                            if isinstance(child.value.op, ast.Add):
                                                # Check if it's calculating mid = low + high
                                                if (isinstance(child.value.left, ast.Name) and isinstance(child.value.right, ast.Name)):
                                                    self.binary_search_pattern = True
        
        self.loops.append('linear')
        self.generic_visit(node)
        self.current_loop_depth -= 1
    
    def visit_FunctionDef(self, node):
        # Check for recursion
        for n in ast.walk(node):
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == node.name:
                self.recursion = True
        self.generic_visit(node)
    
    def visit_Call(self, node):
        # Check for function calls that might indicate complexity
        if isinstance(node.func, ast.Name):
            if node.func.id in ['sorted', 'sort']:
                self.sort_operations += 1
            elif node.func.id in ['binary_search', 'bisect', 'bisect_left', 'bisect_right', 'heappop', 'heappush']:
                # Known logarithmic functions
                self.logarithmic = True
                self.has_logarithmic_operation = True
                self.logarithmic_loops += 1
        # Check for method calls that indicate complexity
        elif isinstance(node.func, ast.Attribute):
            if node.func.attr in ['sort', 'sorted']:
                self.sort_operations += 1
            elif node.func.attr in ['bisect', 'bisect_left', 'bisect_right']:
                # Known logarithmic methods
                self.logarithmic = True
                self.has_logarithmic_operation = True
                self.logarithmic_loops += 1
        self.generic_visit(node)
    
    def determine_complexity(self):
        # Determine complexity based on loops, recursion, and operations
        if self.recursion:
            return 'O(2^n)'
        
        # Check for binary search pattern
        if self.binary_search_pattern:
            return 'O(log n)'
        
        # Check for sorting operations
        if self.sort_operations > 0:
            if len(self.loops) == 0:
                return 'O(n log n)'
            elif len(self.loops) == 1:
                return 'O(n log n)'
        
        # Check for logarithmic patterns
        if self.logarithmic or self.has_logarithmic_operation:
            if self.logarithmic_loops > 0:
                if len(self.loops) == 1:
                    return 'O(log n)'
                elif len(self.loops) == 2:
                    return 'O(n log n)'
        
        # Determine based on loop count
        loop_count = len(self.loops)
        if loop_count == 0:
            return 'O(1)'
        elif loop_count == 1:
            return 'O(n)'
        elif loop_count == 2:
            return 'O(n^2)'
        elif loop_count == 3:
            return 'O(n^3)'
        else:
            return 'O(n^3)'

def analyze_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Enhanced AST analysis
        tree = ast.parse(content)
        analyzer = TimeComplexityAnalyzer()
        analyzer.visit(tree)
        
        # Get complexity from analyzer
        return analyzer.determine_complexity()
    except Exception as e:
        return 'Error'

def main():
    results = {}
    for category in categories:
        category_dir = os.path.join(data_dir, category)
        if not os.path.exists(category_dir):
            continue
        
        results[category] = {'total': 0, 'correct': 0}
        
        # Get all Python files in the category directory
        for root, dirs, files in os.walk(category_dir):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    results[category]['total'] += 1
                    
                    # Analyze the file
                    predicted_complexity = analyze_file(file_path)
                    
                    # Check if predicted complexity matches the category
                    if any(predicted_complexity in expected for expected in COMPLEXITY_CATEGORIES[category]):
                        results[category]['correct'] += 1
    
    # Calculate total accuracy
    total_files = sum([results[cat]['total'] for cat in results])
    total_correct = sum([results[cat]['correct'] for cat in results])
    total_accuracy = (total_correct / total_files) * 100 if total_files > 0 else 0
    
    # Write results to file
    output_file = '/home/wuyankai/myResearch/codeComplex/static_anlysis_python/analysis_results.txt'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('Time Complexity Analysis Results\n')
        f.write('=' * 50 + '\n')
        
        for category in categories:
            if category in results:
                total = results[category]['total']
                correct = results[category]['correct']
                accuracy = (correct / total) * 100 if total > 0 else 0
                f.write(f'{category}:\n')
                f.write(f'  Total files: {total}\n')
                f.write(f'  Correct predictions: {correct}\n')
                f.write(f'  Accuracy: {accuracy:.2f}%\n\n')
        
        f.write('=' * 50 + '\n')
        f.write(f'Total files: {total_files}\n')
        f.write(f'Total correct predictions: {total_correct}\n')
        f.write(f'Overall accuracy: {total_accuracy:.2f}%\n')
    
    print(f'Analysis completed. Results saved to {output_file}')

if __name__ == '__main__':
    main()
