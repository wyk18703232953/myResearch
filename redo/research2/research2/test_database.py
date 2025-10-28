# 尝试导入MySQL连接器，如果未安装则提供安装指导
try:
    import mysql.connector
    import traceback
except ImportError:
    print("❌ 错误：未找到MySQL连接器模块")
    print("\n请运行以下命令安装所需依赖：")
    print("  pip install mysql-connector-python")
    print("\n或者使用以下替代方案：")
    print("  pip install pymysql")
    print("\n安装完成后重新运行此脚本")
    exit(1)

class DatabaseTester:
    """
    数据库测试工具类，用于测试debate_agents.py中使用的数据库连接和操作
    提供连接测试、表创建、数据插入、查询和清理功能
    """
    
    def __init__(self, host='localhost', user='root', password='123456', database='debate_db'):
        """
        初始化数据库连接参数
        
        Args:
            host: 数据库主机地址
            user: 数据库用户名
            password: 数据库密码
            database: 数据库名称
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None
        
    def connect(self):
        """
        测试数据库连接
        
        Returns:
            bool: 连接成功返回True，否则返回False
        """
        print(f"测试连接到数据库: {self.host}@{self.database}")
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=3306,
                user=self.user,
                password=self.password,
                database=self.database,
                charset='utf8mb4',
                collation='utf8mb4_unicode_ci',
                use_unicode=True,
                connection_timeout=30
            )
            self.cursor = self.connection.cursor()
            print("✅ 数据库连接成功!")
            return True
        except mysql.connector.Error as err:
            print(f"❌ 数据库连接失败: {err}")
            print("错误详情:")
            traceback.print_exc()
            return False
    
    def create_test_tables(self):
        """
        创建测试所需的表结构，模拟debate_agents.py中使用的表
        """
        if not self.connection or not self.cursor:
            print("请先成功连接到数据库")
            return False
        
        try:
            # 创建debate_results表，与debate_agents.py中使用的表结构匹配
            create_table_sql = """
            CREATE TABLE IF NOT EXISTS debate_results (
                id INT AUTO_INCREMENT PRIMARY KEY,
                role VARCHAR(255) NOT NULL,
                output TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
            
            self.cursor.execute(create_table_sql)
            self.connection.commit()
            print("✅ 表结构创建/验证成功")
            return True
        except mysql.connector.Error as err:
            print(f"❌ 创建表结构失败: {err}")
            traceback.print_exc()
            return False
    
    def test_insert_data(self):
        """
        测试数据插入功能
        """
        if not self.connection or not self.cursor:
            print("请先成功连接到数据库")
            return False
        
        try:
            # 插入测试数据
            test_data = [
                ("算法专家", "这是一个测试算法思路"),
                ("实现专家", "这是一个测试代码实现"),
                ("测试批判专家", "这是一个测试批判报告")
            ]
            
            insert_sql = "INSERT INTO debate_results (role, output) VALUES (%s, %s)"
            self.cursor.executemany(insert_sql, test_data)
            self.connection.commit()
            print(f"✅ 成功插入 {self.cursor.rowcount} 条测试数据")
            return True
        except mysql.connector.Error as err:
            print(f"❌ 插入数据失败: {err}")
            traceback.print_exc()
            return False
    
    def test_query_data(self):
        """
        测试数据查询功能
        """
        if not self.connection or not self.cursor:
            print("请先成功连接到数据库")
            return False
        
        try:
            # 查询数据
            query_sql = "SELECT id, role, output, created_at FROM debate_results ORDER BY created_at DESC LIMIT 10"
            self.cursor.execute(query_sql)
            results = self.cursor.fetchall()
            
            print(f"✅ 查询到 {len(results)} 条记录:")
            for row in results:
                print(f"ID: {row[0]}, 角色: {row[1]}, 创建时间: {row[3]}")
                print(f"内容: {row[2][:100]}..." if len(row[2]) > 100 else f"内容: {row[2]}")
                print("-" * 50)
            return True
        except mysql.connector.Error as err:
            print(f"❌ 查询数据失败: {err}")
            traceback.print_exc()
            return False
    
    def test_database_interaction(self):
        """
        综合测试数据库交互功能
        """
        print("\n" + "=" * 60)
        print("开始数据库综合测试")
        print("=" * 60)
        
        success = True
        
        # 步骤1: 连接数据库
        success &= self.connect()
        if not success:
            print("数据库测试中断: 无法连接到数据库")
            return False
        
        # 步骤2: 创建表结构
        success &= self.create_test_tables()
        
        # 步骤3: 测试插入
        success &= self.test_insert_data()
        
        # 步骤4: 测试查询
        success &= self.test_query_data()
        
        # 清理资源
        self.close()
        
        print("\n" + "=" * 60)
        if success:
            print("✅ 数据库测试全部通过!")
        else:
            print("❌ 数据库测试存在失败项，请检查以上错误信息")
        print("=" * 60)
        
        return success
    
    def close(self):
        """
        关闭数据库连接和游标
        """
        if self.cursor:
            try:
                self.cursor.close()
                print("游标已关闭")
            except Exception as e:
                print(f"关闭游标时出错: {e}")
        
        if self.connection:
            try:
                self.connection.close()
                print("数据库连接已关闭")
            except Exception as e:
                print(f"关闭数据库连接时出错: {e}")
    
    def get_connection_info(self):
        """
        获取并打印数据库连接信息，用于调试
        """
        print("\n数据库连接配置:")
        print(f"主机: {self.host}")
        print(f"用户名: {self.user}")
        print(f"密码: {'*' * len(self.password)}")  # 密码掩码
        print(f"数据库: {self.database}")
        print()

# 测试用例
if __name__ == "__main__":
    # 创建测试实例，使用与debate_agents.py相同的连接参数
    tester = DatabaseTester(
        host='localhost',
        user='root',
        password='123456',
        database='debate_db'
    )
    
    # 显示连接信息
    tester.get_connection_info()
    
    # 运行综合测试
    tester.test_database_interaction()
    
    print("\n测试完成。如果连接失败，请检查:")
    print("1. MySQL服务是否正在运行")
    print("2. 主机地址、用户名、密码是否正确")
    print("3. 数据库debate_db是否已创建")
    print("4. 用户是否有足够的权限")