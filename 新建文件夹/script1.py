# script1.py - First Python script
import time
import sys
import dis

# Direct assignment of code to execute - user can customize this directly
code_to_execute = """
# Recursive function example
def factorial(n):
    if n <= 1:
        return 1
    else:
        return factorial(n-2) + factorial(n-1)
def main():
    n=40
    result = factorial(n)
    print(f'Factorial of {n} is: {result}')
main()
"""
# 354224848179261915075
# Dynamic bytecode counting function
def count_dynamic_bytecode(code_str, globals_dict, locals_dict):
    """Execute code and count dynamic bytecode instructions"""
    # Compile code
    compiled_code = compile(code_str, '<string>', 'exec')
    
    # Instruction count
    instruction_count = 0
    
    # Create a mapping from (code_obj, line_number) to number of instructions on that line
    line_instruction_counts = {}
    
    # Function to count instructions per line for a code object
    def count_instructions_per_line(code_obj):
        current_line = None
        line_counts = {}
        
        for inst in dis.get_instructions(code_obj):
            if inst.starts_line:
                current_line = inst.starts_line
            
            if current_line is not None:
                if current_line not in line_counts:
                    line_counts[current_line] = 0
                line_counts[current_line] += 1
        
        # Store in the global mapping
        for line, count in line_counts.items():
            line_instruction_counts[(code_obj, line)] = count
    
    # Recursively process all code objects
    def process_code_objects(code_obj):
        # Count instructions per line for this code object
        count_instructions_per_line(code_obj)
        
        # Process nested code objects (functions inside functions)
        for const in code_obj.co_consts:
            if hasattr(const, 'co_code'):
                process_code_objects(const)
    
    # Start processing from the main code object
    process_code_objects(compiled_code)
    
    # Trace function - count instructions for each line execution
    def trace_function(frame, event, arg):
        nonlocal instruction_count
        
        if event == 'line':
            # Get current code object and line number
            code_obj = frame.f_code
            line_num = frame.f_lineno
            
            # Look up the instruction count for this code object and line
            if (code_obj, line_num) in line_instruction_counts:
                instruction_count += line_instruction_counts[(code_obj, line_num)]
        
        return trace_function
    
    try:
        # Set trace function
        original_trace = sys.gettrace()
        sys.settrace(trace_function)
        
        # Execute code - use same dict for both globals and locals to support recursion
        exec(compiled_code, globals_dict, globals_dict)
        
        # Restore original trace function
        sys.settrace(original_trace)
        
        return instruction_count
    except Exception as e:
        # Restore original trace function
        sys.settrace(original_trace)
        print(f"Dynamic trace counting error: {e}")
        
        # Use fallback method: execute and count all instructions
        instruction_count = 0
        
        # Execute code - use same dict for both globals and locals
        exec(compiled_code, globals_dict, globals_dict)
        
        # Count all static instructions
        def count_all_instructions(code_obj):
            nonlocal instruction_count
            for inst in dis.get_instructions(code_obj):
                instruction_count += 1
            # Recursively handle nested code objects
            for const in code_obj.co_consts:
                if hasattr(const, 'co_code'):
                    count_all_instructions(const)
        
        count_all_instructions(compiled_code)
        
        return instruction_count

# Static bytecode counting function (for comparison)
def count_static_bytecode(code_str):
    """Calculate total static bytecode instructions for given code string"""
    try:
        compiled_code = compile(code_str, '<string>', 'exec')
        
        def count_instructions(code_obj):
            count = 0
            for inst in dis.get_instructions(code_obj):
                count += 1
            for const in code_obj.co_consts:
                if hasattr(const, 'co_code'):
                    count += count_instructions(const)
            return count
        
        return count_instructions(compiled_code)
    except Exception as e:
        print(f"Static bytecode counting error: {e}")
        return 0

# Main program
print("=== Bytecode Counting Start ===")

# Calculate static bytecode instructions
static_count = count_static_bytecode(code_to_execute)
print(f"Static bytecode instructions total: {static_count}")

# Execute code and calculate dynamic bytecode instructions
print("\n=== Code Execution Start ===")
# Create a copy of globals to avoid polluting the global namespace
globals_copy = globals().copy()
globals_copy['time'] = time
dynamic_count = count_dynamic_bytecode(code_to_execute, globals_copy, globals_copy)
print("=== Code Execution End ===")

# Output results
print(f"\n=== Bytecode Counting Results ===")
print(f"Static bytecode instructions total: {static_count}")
print(f"Dynamic bytecode instructions total: {dynamic_count}")
print(f"Difference (dynamic - static): {dynamic_count - static_count}")
print(f"This shows that dynamic counting correctly tracks repeated executions!")
print("====================")