#读取mbpp_plus_data.parquet文件
import pandas as pd

df = pd.read_parquet("../mbpp_plus/data/mbpp_plus_data.parquet")
print(df.columns)
print(df.head(5))

# 获取第一条数据
first_row = df.iloc[0]

# 将第一条数据的各个字段赋值给本地变量
task_id = first_row["task_id"]
code = first_row["code"]
prompt = first_row["prompt"]
source_file = first_row["source_file"]
test_imports = first_row["test_imports"]
test_list = first_row["test_list"]
test = first_row["test"]

# 输出本地变量
print("\n第一条数据的各个字段：")
print(f"task_id: {task_id}")
print(f"code: {code}")
print(f"prompt: {prompt}")
print(f"source_file: {source_file}")
print(f"test_imports: {test_imports}")
print(f"test_list: {test_list}")
print(f"test: {test}")