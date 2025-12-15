import json
import os
import timeit
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import pearsonr
from openai import OpenAI
import tempfile

class CodeComplexityAnalyzer:
    def __init__(self):
        self.llm_client = self._setup_llm_client()
        self.results_dir = "D:/MyResearch/codeComplex/auto2/results/"
        os.makedirs(self.results_dir, exist_ok=True)
        
    def _setup_llm_client(self):
        """Set up the LLM client using existing API configuration"""
        return OpenAI(
            api_key="sk-glL4mhF8GCov9dZiCJLIQ64OvlUpPa2qjLCpnV6zKz4byxXE",
            base_url="https://yunwu.ai/v1"
        )
    
    def read_jsonl(self, file_path, limit=5):
        """Read first 'limit' records from JSONL file"""
        records = []
        with open(file_path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                if i >= limit:
                    break
                try:
                    record = json.loads(line.strip())
                    records.append(record)
                except json.JSONDecodeError:
                    continue
        return records
    
    def modify_code_with_llm(self, original_code):
        """Send code to LLM to modify input() calls and generate generate_input(n) function"""
        prompt = f"""
        Identify all input() function calls in the following code. Replace each input() call with generate_input(n).
        Generate a complete implementation of generate_input(n) that:
        i. Accepts a single parameter n representing test data scale/size
        ii. Returns test data of the same type as original input() calls
        iii. Generates appropriate test data based on the value of n
        Return only the modified source code with the implemented generate_input(n) function included.
        Ensure no additional explanations, comments, or content outside the modified source code is included in the response.
        
        Original code:
        {original_code}
        """
        
        response = self.llm_client.chat.completions.create(
            model="gpt-5-nano-2025-08-07",
            temperature=0.0,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert Python developer specializing in code transformation and test data generation."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            stream=False
        )
        
        modified_code = response.choices[0].message.content.strip()
        
        # Clean up any code blocks if present
        if modified_code.startswith('```python'):
            modified_code = modified_code[9:]
        if modified_code.endswith('```'):
            modified_code = modified_code[:-3]
        modified_code = modified_code.strip()
        
        return modified_code
    
    def execute_code(self, code, n_values, runs=5):
        """Execute code with different n values and measure execution time"""
        results = {}
        
        for n in n_values:
            total_time = 0.0
            
            for _ in range(runs):
                # Create a local namespace for execution
                local_namespace = {'n': n}
                
                # Start timing
                start_time = timeit.default_timer()
                
                try:
                    # Execute the code in the local namespace
                    exec(code, globals(), local_namespace)
                except Exception as e:
                    print(f"  Error executing code with n={n}: {e}")
                    print(f"  Code: {code[:1000]}...")
                    continue
                
                # Stop timing
                end_time = timeit.default_timer()
                total_time += (end_time - start_time)
            
            if total_time > 0:
                avg_time = total_time / runs
                results[n] = avg_time
        
        return results
    
    # Define common time complexity functions for curve fitting
    def _constant_func(self, n, a):
        return np.full_like(n, a)
    
    def _log_func(self, n, a, b):
        return a * np.log(n) + b
    
    def _linear_func(self, n, a, b):
        return a * n + b
    
    def _linearithmic_func(self, n, a, b):
        return a * n * np.log(n) + b
    
    def _quadratic_func(self, n, a, b, c):
        return a * n**2 + b * n + c
    
    def _cubic_func(self, n, a, b, c, d):
        return a * n**3 + b * n**2 + c * n + d
    
    def _exponential_func(self, n, a, b):
        return a * np.exp(b * n)
    
    def calculate_r_squared(self, y_true, y_pred):
        """Calculate R-squared value"""
        ss_res = np.sum((y_true - y_pred) ** 2)
        ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
        r_squared = 1 - (ss_res / ss_tot)
        return r_squared
    
    def analyze_time_complexity(self, execution_results):
        """Analyze execution times to determine time complexity"""
        n_values = np.array(sorted(execution_results.keys()))
        times = np.array([execution_results[n] for n in n_values])
        
        # Define complexity functions to test
        complexity_functions = {
            'O(1)': self._constant_func,
            'O(log n)': self._log_func,
            'O(n)': self._linear_func,
            'O(n log n)': self._linearithmic_func,
            'O(n²)': self._quadratic_func,
            'O(n³)': self._cubic_func,
            'O(2^n)': self._exponential_func
        }
        
        best_fit = None
        best_r_squared = -float('inf')
        all_fits = {}
        
        for complexity_name, func in complexity_functions.items():
            try:
                # Fit the function to the data
                popt, _ = curve_fit(func, n_values, times, maxfev=10000)
                
                # Predict times using the fitted function
                predicted_times = func(n_values, *popt)
                
                # Calculate R-squared value
                r_squared = self.calculate_r_squared(times, predicted_times)
                
                all_fits[complexity_name] = {
                    'params': popt.tolist(),
                    'r_squared': r_squared,
                    'predicted_times': predicted_times.tolist()
                }
                
                # Update best fit if current fit is better
                if r_squared > best_r_squared:
                    best_r_squared = r_squared
                    best_fit = complexity_name
            except Exception as e:
                # Skip if curve fitting fails
                all_fits[complexity_name] = {
                    'error': str(e),
                    'r_squared': -float('inf')
                }
        
        return {
            'n_values': n_values.tolist(),
            'actual_times': times.tolist(),
            'all_fits': all_fits,
            'best_fit': best_fit,
            'best_r_squared': best_r_squared
        }
    
    def generate_report(self, record_index, original_code, modified_code, execution_results, complexity_analysis):
        """Generate a comprehensive report for a single record"""
        report = {
            'record_index': record_index,
            'original_code': original_code,
            'modified_code': modified_code,
            'execution_results': execution_results,
            'complexity_analysis': complexity_analysis
        }
        
        # Save report to JSON file
        report_path = os.path.join(self.results_dir, f'record_{record_index + 1}.json')
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        return report
    
    def run_analysis(self, jsonl_file_path, n_values=[10, 100, 1000, 10000, 100000], limit=1):
        """Run the complete analysis workflow"""
        # Step 1: Read JSONL file
        records = self.read_jsonl(jsonl_file_path, limit)
        
        all_reports = []
        
        for i, record in enumerate(records):
            print(f"Processing record {i + 1} of {len(records)}...")
            
            # Step 2: Extract original code from "src" field
            original_code = record['src']
            
            # Step 3: Modify code using LLM
            print(f"  Modifying code using LLM...")
            modified_code = self.modify_code_with_llm(original_code)
            
            # Debug: Print first 500 chars of modified code
            print(f"  Modified code preview: {modified_code[:500]}...")
            
            # Step 4: Execute code with different n values
            print(f"  Executing code with different n values...")
            execution_results = self.execute_code(modified_code, n_values)
            
            # Step 5: Analyze time complexity
            print(f"  Analyzing time complexity...")
            complexity_analysis = self.analyze_time_complexity(execution_results)
            
            # Step 6: Generate and save report
            print(f"  Generating report...")
            report = self.generate_report(i, original_code, modified_code, execution_results, complexity_analysis)
            all_reports.append(report)
        
        # Generate summary report
        self._generate_summary_report(all_reports)
        
        print(f"Analysis completed. Results saved to {self.results_dir}")
    
    def _generate_summary_report(self, all_reports):
        """Generate a summary report of all analyzed records"""
        summary = {
            'total_records': len(all_reports),
            'records': [
                {
                    'record_index': report['record_index'] + 1,
                    'best_fit': report['complexity_analysis']['best_fit'],
                    'best_r_squared': report['complexity_analysis']['best_r_squared'],
                    'execution_times': report['execution_results']
                }
                for report in all_reports
            ]
        }
        
        summary_path = os.path.join(self.results_dir, 'summary_report.json')
        with open(summary_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    analyzer = CodeComplexityAnalyzer()
    jsonl_file = "D:\MyResearch\codeComplex\data\python_data.jsonl"
    
    # Define n values to test (test data sizes)
    n_values = [10, 100, 1000, 10000, 100000]
    
    # Run the analysis
    analyzer.run_analysis(jsonl_file, n_values=n_values, limit=1)
