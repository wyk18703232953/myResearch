import random
import pymysql
import traceback
import time
from contextlib import contextmanager
from openai import OpenAI  # 导入OpenAI库

# 算法专家类：负责分析问题并生成算法思路和复杂度预估
class AlgorithmExpert:
    # 初始化函数，接收问题描述
    def __init__(self, question):
        self.question = question

    # 分析问题并生成算法思路
    def analyze_question(self):
        """
        分析问题并生成算法思路
        
        Returns:
            dict: 包含角色和算法思路的字典，失败时返回None
        """
        try:
            # 初始化OpenAI客户端并调用API生成算法思路
            print("🔍 算法专家开始分析问题...")
            client = OpenAI(api_key='sk-glL4mhF8GCov9dZiCJLIQ64OvlUpPa2qjLCpnV6zKz4byxXE', base_url="https://yunwu.ai/v1")
            response = client.chat.completions.create(
                model="gpt-5-nano-2025-08-07",
                messages=[
                    {"role": "system", "content": "你是一个经验丰富的算法专家，擅长解析复杂问题并生成高效的算法解决方案。请详细分析问题的核心需求，提供算法思路、复杂度预估，并解释选择该算法的原因。"},
                    {"role": "user", "content": self.question}
                ],
                stream=False
            )
            algorithm_idea = response.choices[0].message.content
            print("✅ 算法专家分析完成")
            # 返回角色标识和算法思路
            return {"role": "算法专家", "algorithm_idea": algorithm_idea}
        except Exception as e:
            print(f"❌ 算法专家分析失败: {str(e)}")
            traceback.print_exc()
            return None

# 实现专家类：负责将算法思路转化为具体代码实现
class ImplementationExpert:
    # 初始化函数，接收算法思路
    def __init__(self, algorithm_idea):
        self.algorithm_idea = algorithm_idea

    # 根据算法思路生成代码实现和风险提示
    def implement_algorithm(self):
        """
        根据算法思路生成代码实现和风险提示
        
        Returns:
            dict: 包含角色、代码实现和风险提示的字典，失败时返回None
        """
        try:
            # 调用API生成代码实现
            print("🔍 实现专家开始生成代码...")
            client = OpenAI(api_key='sk-glL4mhF8GCov9dZiCJLIQ64OvlUpPa2qjLCpnV6zKz4byxXE', base_url="https://yunwu.ai/v1")
            response = client.chat.completions.create(
                model="gpt-5-nano-2025-08-07",
                messages=[
                    {"role": "system", "content": "你是一个资深的实现专家，擅长将复杂算法转化为高效的代码实现。请根据算法思路生成优化的代码，详细说明代码的关键逻辑，并提供可能的实现风险及其解决方案。"},
                    {"role": "user", "content": self.algorithm_idea}
                ],
                stream=False
            )
            # 解析API响应，分离代码和风险提示
            result = response.choices[0].message.content.split("\n\n")
            code = result[0]
            risk_warning = result[1] if len(result) > 1 else "无风险提示"
            print("✅ 实现专家代码生成完成")
            # 返回角色标识、代码实现和风险提示
            return {"role": "实现专家", "code": code, "risk_warning": risk_warning}
        except Exception as e:
            print(f"❌ 实现专家代码生成失败: {str(e)}")
            traceback.print_exc()
            return None

# 测试批判专家类：负责设计测试用例并评估算法和代码质量
class TestingCriticExpert:
    # 初始化函数，接收算法思路和代码实现
    def __init__(self, algorithm_idea, code):
        self.algorithm_idea = algorithm_idea
        self.code = code

    # 设计边界测试用例并生成批判报告
    def design_tests_and_critique(self):
        """
        设计边界测试用例并生成批判报告
        
        Returns:
            dict: 包含角色、测试用例和批判报告的字典，失败时返回None
        """
        try:
            # 调用API生成测试用例和批判报告
            print("🔍 测试批判专家开始分析...")
            client = OpenAI(api_key='sk-glL4mhF8GCov9dZiCJLIQ64OvlUpPa2qjLCpnV6zKz4byxXE', base_url="https://yunwu.ai/v1")
            response = client.chat.completions.create(
                model="gpt-5-nano-2025-08-07",
                messages=[
                    {"role": "system", "content": "你是一个严谨的测试批判专家，擅长设计全面的边界测试用例并发现算法和代码中的潜在问题。请分析算法逻辑和代码漏洞，并提供改进建议。"},
                    {"role": "user", "content": f"算法思路: {self.algorithm_idea}\n代码: {self.code}"}
                ],
                stream=False
            )
            # 解析API响应，分离测试用例和批判报告
            result = response.choices[0].message.content.split("\n\n")
            test_cases = result[0].split("\n")
            critique_report = result[1] if len(result) > 1 else "无批判报告"
            print("✅ 测试批判专家分析完成")
            # 返回角色标识、测试用例和批判报告
            return {"role": "测试批判专家", "test_cases": test_cases, "critique_report": critique_report}
        except Exception as e:
            print(f"❌ 测试批判专家分析失败: {str(e)}")
            traceback.print_exc()
            return None

# 数据库连接类
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

# 辩论控制器类：协调各个专家之间的交互并管理辩论流程
class DebateController:
    # 初始化函数，连接数据库
    def __init__(self):
        self.db = DatabaseConnection()
        self.test_connection()

    # 测试数据库连接
    def test_connection(self):
        print("🔍 尝试连接到数据库...")
        try:
            with self.db.get_cursor() as cursor:
                cursor.execute("SELECT 1")
                print("✅ 数据库连接成功!")
                return True
        except Exception as err:
            print(f"❌ 数据库连接失败: {err}")
            print("错误详情:")
            traceback.print_exc()
            return False

    # 存储辩论结果到数据库
    def store_results(self, question, results):
        try:
            with self.db.get_cursor() as cursor:
                for result in results:
                    # 检查表结构是否存在
                    cursor.execute("SHOW COLUMNS FROM debate_results LIKE 'question'")
                    has_question_column = cursor.fetchone() is not None
                    
                    if has_question_column:
                        sql = "INSERT INTO debate_results (question, role, output) VALUES (%s, %s, %s)"
                        cursor.execute(sql, (question, result["role"], str(result)))
                    else:
                        sql = "INSERT INTO debate_results (role, output) VALUES (%s, %s)"
                        cursor.execute(sql, (result["role"], str(result)))
                print(f"✅ 成功存储 {cursor.rowcount} 条辩论结果到数据库")
                return True
        except Exception as err:
            print(f"❌ 存储结果失败: {err}")
            traceback.print_exc()
            return False

    # 执行加权投票，判断是否达成共识
    def weighted_voting(self, results):
        # 为不同角色分配不同权重：算法专家(40%)、实现专家(30%)、测试批判专家(30%)
        weights = {"算法专家": 0.4, "实现专家": 0.3, "测试批判专家": 0.3}
        # 计算加权分数，判断是否达到0.8阈值
        score = sum(weights[result["role"]] for result in results)
        return score >= 0.8

    # 运行辩论循环，协调整个流程
    def run_debate_cycle(self, question):
        print(f"\n🔄 开始辩论循环，问题: {question}")
        print("=" * 80)
        
        # 初始化各个专家角色
        algorithm_expert = AlgorithmExpert(question)
        
        # 优化API调用，避免重复调用
        print("\n第1步: 算法专家分析问题")
        algo_result = algorithm_expert.analyze_question()
        if not algo_result:
            print("❌ 算法分析失败，终止辩论")
            return
        
        print("\n第2步: 实现专家生成代码")
        time.sleep(1)  # 添加短暂延迟避免API限流
        implementation_expert = ImplementationExpert(algo_result["algorithm_idea"])
        impl_result = implementation_expert.implement_algorithm()
        if not impl_result:
            print("❌ 代码实现失败，终止辩论")
            return
        
        print("\n第3步: 测试批判专家分析")
        time.sleep(1)  # 添加短暂延迟避免API限流
        testing_critic_expert = TestingCriticExpert(
            algo_result["algorithm_idea"], 
            impl_result["code"]
        )
        test_result = testing_critic_expert.design_tests_and_critique()
        if not test_result:
            print("❌ 测试分析失败，终止辩论")
            return
        
        # 收集所有专家的输出结果
        results = [algo_result, impl_result, test_result]
        print("\n当前辩论结果:")
        for result in results:
            print(f"角色: {result['role']}")
            if "algorithm_idea" in result:
                print(f"算法思路: {result['algorithm_idea'][:100]}...") 

        print("\n第4步: 存储结果到数据库")
        # 存储结果到数据库
        self.store_results(question, results)
        
        print("\n第5步: 执行加权投票")
        # 执行加权投票，判断是否达成共识
        consensus_reached = self.weighted_voting(results)
        print("=" * 80)
        if consensus_reached:
            print("✅ 共识已达成！")
            # 输出关键结果信息而非完整对象
            print(f"\n📊 算法思路摘要: {algo_result['algorithm_idea'][:100]}...")
            print(f"📝 代码实现行数: {impl_result['code'].count('\n') + 1}行")
            print(f"⚠️  风险提示: {impl_result['risk_warning'][:100]}...")
            print(f"🧪 测试用例数: {len(test_result['test_cases'])}个")
        else:
            print("❌ 共识未达成，需要继续辩论。")
        print("=" * 80)

# 程序入口
if __name__ == "__main__":
    # 示例问题：求最大子数组和
    question = "给定一个数组，求最大子数组和"
    print(f"问题: {question}")
    # 初始化辩论控制器并开始辩论循环
    debate_controller = DebateController()
    
    # 检查数据库连接是否成功
    if debate_controller.test_connection():
        print("✅ 数据库连接成功，开始辩论循环")
        debate_controller.run_debate_cycle(question)
        print("✅ 程序执行完毕")
    else:
        print("❌ 无法初始化数据库连接，程序终止")