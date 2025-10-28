import pymysql
from contextlib import contextmanager

class DatabaseConnection:
    def __init__(self, host='localhost', port=3306, user='root', password='123456', database='debate_db'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
    
    def get_connection(self):
        return pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor  # 返回字典格式的结果
        )
    
    @contextmanager
    def get_cursor(self):
        connection = None
        cursor = None
        try:
            connection = self.get_connection()
            cursor = connection.cursor()
            yield cursor
            connection.commit()
        except Exception as e:
            if connection:
                connection.rollback()
            raise e
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

# 使用示例
db = DatabaseConnection()

# 查询数据
def get_users():
    with db.get_cursor() as cursor:
        cursor.execute("SELECT * FROM debate_results LIMIT 10")
        results = cursor.fetchall()
        return results

# 插入数据
def insert_user(role, output):
    with db.get_cursor() as cursor:
        sql = "INSERT INTO debate_results (role, output) VALUES (%s, %s)"
        cursor.execute(sql, (role, output))
        return cursor.lastrowid  # 返回插入的记录ID

# 测试查询
print("查询用户:")
# users = get_users()
# print(users)

# 测试插入
new_user_id = insert_user("n1r", "1111")
users = get_users()
print(users)