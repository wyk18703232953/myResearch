from openai import OpenAI
import os
import uuid
import json
from typing import List, Dict, Tuple

# ============================================================
# Conversation Manager – 存储整个工作流的上下文
# ============================================================
class ConversationManager:
    def __init__(self):
        self.sessions = {}

    def init_session(self, name, system_prompt):
        if name not in self.sessions:
            self.sessions[name] = [
                {"role": "system", "content": system_prompt}
            ]

    def add_user(self, name, content):
        self.sessions[name].append({"role": "user", "content": content})

    def add_assistant(self, name, content):
        self.sessions[name].append({"role": "assistant", "content": content})

    def get_messages(self, name):
        return self.sessions[name]

    def __getitem__(self, item):
        return self.sessions[item]


# ============================================================
# Model Client – 所有的模型调用都统一在这里
# ============================================================
class ModelClient:
    def __init__(self, api_key, base_url):
        self.client = OpenAI(api_key=api_key, base_url=base_url)

    def ask(self, messages, model="gpt-5-nano-2025-08-07", temperature=0.0):
        response = self.client.chat.completions.create(
            model=model,
            temperature=temperature,
            messages=messages
        )
        return response.choices[0].message.content


# ============================================================
# Pipeline – 根据你的描述构造完整流程
# ============================================================
class Pipeline:
    def __init__(self, conv, model):
        self.conv = conv
        self.model = model

    # Step 1 & 2: 基于 Prompt1 生成 SCOT 并生成 commented code
    def generate_scot_and_commented_code(self, session_name, prompt1):
        self.conv.add_user(session_name, f"Generate SCOT:\n{prompt1}")
        commented_code=self.model.ask(self.conv.get_messages(session_name))
        self.conv.add_assistant(session_name, commented_code)
        return commented_code
        
        


    # # Step 3: 将多个 commented code 聚类为 N 类
    # def cluster_codes(self, session_name, codes, N):
    #     self.conv.add_user(session_name, 
    #                        f"Cluster the following commented codes into {N} groups:\n{codes}")
    #     clustering = self.model.ask(self.conv.get_messages(session_name))
    #     self.conv.add_assistant(session_name, clustering)
    #     return clustering
    
    # --- 聚类：返回一个 dict: cluster_id -> [codes...] ---
    # 注意：这里我们让 model 返回一个 JSON 格式的聚类结果，便于解析。
    def cluster_codes(self, session: str, codes: [str], n_clusters: int) -> Dict[int, List[str]]:
        # 将所有代码附带索引传给模型，让模型按 cluster 分组并以 JSON 返回
        payload = {
            "instruction": f"Cluster the following {len(codes)} commented codes into "
                           f"{n_clusters} groups. Return JSON like {{\"0\": [0,2], \"1\": [1,3], ...}} "
                           "where numbers reference the index in the provided list. Do not output extra text.",
            "codes": codes
        }
        self.conv.add_user(session, json.dumps(payload, ensure_ascii=False, indent=2))
        clustering_raw = self.model.ask(self.conv.get_messages(session))
        self.conv.add_assistant(session, clustering_raw)

        # 解析模型返回（容错：模型可能返回包在文本里的 JSON）
        clustering_json = None
        try:
            # 尝试提取第一个 JSON 对象
            start = clustering_raw.find("{")
            end = clustering_raw.rfind("}") + 1
            possible = clustering_raw[start:end]
            clustering_json = json.loads(possible)
        except Exception:
            # 失败则让模型返回更严格的 JSON（fallback）
            self.conv.add_user(session, "The previous output wasn't valid JSON. Please output only the JSON.")
            clustering_raw = self.model.ask(self.conv.get_messages(session))
            self.conv.add_assistant(session, clustering_raw)
            clustering_json = json.loads(clustering_raw)

        # build dict cluster_id -> list of code strings
        clusters: Dict[int, List[str]] = {}
        for k, idx_list in clustering_json.items():
            cid = int(k)
            # 添加索引边界检查，确保i在codes列表范围内
            valid_codes = []
            for i in idx_list:
                if 0 <= i < len(codes):
                    valid_codes.append(codes[i])
                else:
                    print(f"Warning: Index {i} out of range for codes list of length {len(codes)}")
            clusters[cid] = valid_codes

        return clusters


    # Step 4: 对每一类做 N 次 mutation
    # def mutate_code(self, session_name, code, rounds=10):
        # mutated_versions = []
        # for i in range(rounds):
        #     self.conv.add_user(session_name, 
        #                        f"Mutate version {i+1} of this commented code:\n{code}")
        #     mutated = self.model.ask(self.conv.get_messages(session_name), temperature=0.8)
        #     self.conv.add_assistant(session_name, mutated)
        #     mutated_versions.append(mutated)
        # return mutated_versions
    def mutate_code_for_clusters(self, session: str, clusters: Dict[int, List[str]],
                                 rounds_per_cluster: int = 3,
                                 temperature: float = 0.7,
                                 rep_selector: str = "first") -> Dict[int, List[str]]:
        """
        返回: dict cluster_id -> list of mutated versions for that cluster (length = rounds_per_cluster)
        说明: 只有每一类的代表会被变异，其它同类样本被舍弃。
        """
        mutated_per_cluster: Dict[int, List[str]] = {}

        for cid, members in clusters.items():
            if not members:
                mutated_per_cluster[cid] = []
                continue

            # 选代表：当前实现取 members[0]；以后可以扩展为挑选最优或最短等
            if rep_selector == "first":
                representative = members[0]
            elif rep_selector == "longest":
                representative = max(members, key=len)
            else:
                representative = members[0]

            # 向会话加入上下文，明确说明只对 representative 变异
            self.conv.add_user(session,
                               f"Cluster {cid}: Representative code (only the first will be mutated):\n"
                               f"{representative}\n"
                               f"Other cluster members (discarded):\n{json.dumps(members[1:], ensure_ascii=False)}")

            mutated_versions = []
            for r in range(rounds_per_cluster):
                self.conv.add_user(session,
                                   f"Mutate representative (round {r+1}/{rounds_per_cluster}). "
                                   "Produce a full commented code variant. Keep semantics, but vary "
                                   "implementation details, variable names, comments and minor optimizations.")
                mutated = self.model.ask(self.conv.get_messages(session), temperature=temperature)
                # 将模型回复记录到对话历史并收集结果
                self.conv.add_assistant(session, mutated)
                mutated_versions.append(mutated)

            mutated_per_cluster[cid] = mutated_versions

        return mutated_per_cluster

    # Step 5: 对多版本(commented code) 进行一致性评分
    def score_consistency(self, session_name, versions):
        self.conv.add_user(session_name, 
                           f"Evaluate consistency of these versions:\n{versions}\n"
                           f"Return a JSON list of scores 0-100.")
        scores = self.model.ask(self.conv.get_messages(session_name))
        self.conv.add_assistant(session_name, scores)
        return scores

    # Step 6: 从 10 个 mutated code 中选出 valid@10
    def select_valid_at_10(self, versions, scores):
        import json
        score_list = json.loads(scores)
        best_idx = max(range(len(score_list)), key=lambda i: score_list[i])
        return versions[best_idx], score_list[best_idx]


# ============================================================
# Example usage
# ============================================================

API_KEY = "sk-glL4mhF8GCov9dZiCJLIQ64OvlUpPa2qjLCpnV6zKz4byxXE"
BASE_URL = "https://yunwu.ai/v1"

conv = ConversationManager()
model1 = ModelClient(API_KEY, BASE_URL)

pipeline = Pipeline(conv, model1)

# 初始化会话 (你可以为每个任务一个session)
session_name = str(uuid.uuid4())

conv.init_session(session_name, 
"""
You are Model1, responsible for SCOT generation,
commented code generation, mutation, clustering,
and consistency scoring. Keep full memory of all steps.
""")

# ========== Run the whole workflow ==========
file_path="D:/myResearch/SCoT/template.txt"
with open(file_path, 'r', encoding='utf-8') as f:
    prompt = f.read()
prompt1 = """
{prompt}
"""
# Step 1 & 2: Generate SCOT and commented code
# commented_code = pipeline.generate_scot_and_commented_code(session_name, prompt1)
# print("commented_code=", commented_code)

#读取commented_code中的内容到变量commented_code中。

file_path="D:/myResearch/SCoT/commented_code.txt"
with open(file_path, 'r', encoding='utf-8') as f:
    commented_code = f.read()
    
# 将commented_code按照==============划分为若干字符串list
commented_code_list = commented_code.split('========================================================')
# 去除空字符串和前后空白
# commented_code_list = [item.strip() for item in commented_code_list if item.strip()]
# print("commented_code_list长度:", len(commented_code_list))
# print("commented_code_list前两个元素:", commented_code_list[:2] if len(commented_code_list)>=2 else commented_code_list)

# print("commented_code=", commented_code)
# Step 3 聚类（示例：把 10 个版本的 code 聚成 3 类）
clustering = pipeline.cluster_codes(session_name, commented_code_list, 3)
# print("clustering=", clustering)
# file_path="D:/myResearch/SCoT/clustering.txt"
# with open(file_path, 'r', encoding='utf-8') as f:
#     clustering = f.read()
# print("clustering=", clustering)
# # Step 4 mutate (10次)
mutations = pipeline.mutate_code_for_clusters(session_name, clustering)
print("mutations=", mutations)
# Step 5 consistency scoring
# scores = pipeline.score_consistency(session_name, mutations)

# Step 6 pick valid@10
# valid_code, best_score = pipeline.select_valid_at_10(mutations, scores)

# print("Valid@10 Score =", best_score)
# print(valid_code)
