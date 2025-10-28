# 简化的数据库连接测试脚本
print("1. 开始测试...")

# 首先只测试导入
try:
    print("2. 尝试导入mysql.connector...")
    import mysql.connector
    print("3. 导入成功!")
except ImportError as e:
    print(f"❌ 导入错误: {e}")
    print("请确保已安装mysql-connector-python: pip install mysql-connector-python")
    exit(1)

# 然后测试基本连接参数
print("4. 准备数据库连接参数...")
db_config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "debate_db"
}
print(f"5. 连接参数: {db_config}")

# 最后尝试连接
try:
    print("6. 尝试建立数据库连接...")
    connection = mysql.connector.connect(**db_config)
    print("7. ✅ 数据库连接成功!")
    connection.close()
    print("8. ✅ 数据库连接已关闭")
except Exception as e:
    print(f"9. ❌ 连接错误: {type(e).__name__}: {e}")
    import traceback
    print("详细错误堆栈:")
    traceback.print_exc()

print("10. 测试完成")