import random
import mysql.connector

class AlgorithmExpert:
    def __init__(self, question):
        self.question = question

    def analyze_question(self):
        # 使用API动态生成算法思路和复杂度预估
        client = OpenAI(api_key='sk-glL4mhF8GCov9dZiCJLIQ64OvlUpPa2qjLCpnV6zKz4byxXE', base_url="https://yunwu.ai/v1")
        response = client.chat.completions.create(
            model="gpt-5-nano-2025-08-07",
            messages=[
                {"role": "system", "content": "你是一个算法专家，负责解析问题并生成算法思路和复杂度预估。"},
                {"role": "user", "content": self.question}
            ],
            stream=False
        )
        algorithm_idea = response.choices[0].message.content
        return {"role": "算法专家", "algorithm_idea": algorithm_idea}

class ImplementationExpert:
    def __init__(self, algorithm_idea):
        self.algorithm_idea = algorithm_idea

    def implement_algorithm(self):
        # 使用API动态生成代码实现和风险提示
        client = OpenAI(api_key='sk-glL4mhF8GCov9dZiCJLIQ64OvlUpPa2qjLCpnV6zKz4byxXE', base_url="https://yunwu.ai/v1")
        response = client.chat.completions.create(
            model="gpt-5-nano-2025-08-07",
            messages=[
                {"role": "system", "content": "你是一个实现专家，负责将算法思路转化为代码并提供实现风险提示。"},
                {"role": "user", "content": self.algorithm_idea}
            ],
            stream=False
        )
        result = response.choices[0].message.content.split("\n\n")
        code = result[0]
        risk_warning = result[1] if len(result) > 1 else "无风险提示"
        return {"role": "实现专家", "code": code, "risk_warning": risk_warning}

class TestingCriticExpert:
    def __init__(self, algorithm_idea, code):
        self.algorithm_idea = algorithm_idea
        self.code = code

    def design_tests_and_critique(self):
        # 使用API动态生成边界测试用例和批判报告
        client = OpenAI(api_key='sk-glL4mhF8GCov9dZiCJLIQ64OvlUpPa2qjLCpnV6zKz4byxXE', base_url="https://yunwu.ai/v1")
        response = client.chat.completions.create(
            model="gpt-5-nano-2025-08-07",
            messages=[
                {"role": "system", "content": "你是一个测试批判专家，负责设计边界测试用例并批判算法逻辑和代码漏洞。"},
                {"role": "user", "content": f"算法思路: {self.algorithm_idea}\n代码: {self.code}"}
            ],
            stream=False
        )
        result = response.choices[0].message.content.split("\n\n")
        test_cases = result[0].split("\n")
        critique_report = result[1] if len(result) > 1 else "无批判报告"
        return {"role": "测试批判专家", "test_cases": test_cases, "critique_report": critique_report}

class DebateController:
    def __init__(self):
        self.database = self.connect_to_database()

    def connect_to_database(self):
        # 模拟数据库连接
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="debate_db"
        )

    def store_results(self, results):
        # 模拟存储结果到数据库
        cursor = self.database.cursor()
        for result in results:
            cursor.execute("INSERT INTO debate_results (role, output) VALUES (%s, %s)", (result["role"], str(result)))
        self.database.commit()

    def weighted_voting(self, results):
        # 模拟加权投票
        weights = {"算法专家": 0.4, "实现专家": 0.3, "测试批判专家": 0.3}
        score = sum(weights[result["role"]] for result in results)
        return score >= 0.8

    def run_debate_cycle(self, question):
        algorithm_expert = AlgorithmExpert(question)
        implementation_expert = ImplementationExpert(algorithm_expert.analyze_question()["algorithm_idea"])
        testing_critic_expert = TestingCriticExpert(algorithm_expert.analyze_question()["algorithm_idea"], implementation_expert.implement_algorithm()["code"])

        results = [
            algorithm_expert.analyze_question(),
            implementation_expert.implement_algorithm(),
            testing_critic_expert.design_tests_and_critique()
        ]

        self.store_results(results)

        consensus_reached = self.weighted_voting(results)
        if consensus_reached:
            print("共识已达成，输出最终结果：", results)
        else:
            print("共识未达成，继续辩论循环。")

if __name__ == "__main__":
    question = "给定一个数组，求最大子数组和"
    debate_controller = DebateController()
    debate_controller.run_debate_cycle(question)