import requests
import json
import time
from tqdm import tqdm

# -----------------------------
# 配置
# -----------------------------
BASE_URL = "https://leetcode.com/graphql"
HEADERS = {
    "Content-Type": "application/json",
    "Referer": "https://leetcode.com",
    "User-Agent": "Mozilla/5.0"
}

# -----------------------------
# GraphQL 查询模板
# -----------------------------
query_problemset = """
query problemsetQuestionList($limit: Int, $skip: Int) {
  problemsetQuestionList: questionList(
    categorySlug: ""
    limit: $limit
    skip: $skip
  ) {
    total: totalNum
    questions: data {
      questionId
      questionFrontendId
      title
      titleSlug
      difficulty
      isPaidOnly
      topicTags { name slug }
    }
  }
}
"""

query_detail = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    title
    content
    difficulty
    isPaidOnly
    topicTags { name slug }
    exampleTestcases
    likes
    dislikes
  }
}
"""

# -----------------------------
# 获取所有题目列表
# -----------------------------
def get_all_problems():
    problems = []
    skip = 0
    limit = 100
    print("Fetching LeetCode problem list...")
    while True:
        variables = {"limit": limit, "skip": skip}
        resp = requests.post(BASE_URL, headers=HEADERS, json={"query": query_problemset, "variables": variables})
        data = resp.json().get("data", {}).get("problemsetQuestionList", {})
        if not data or "questions" not in data or "total" not in data:
            print("❌ Error: Unexpected response format.")
            break
        problems.extend(data["questions"])
        skip += limit
        if skip >= data["total"]:
            break
        time.sleep(0.5)
    print(f"✅ Got {len(problems)} problems.")
    return problems

# -----------------------------
# 获取单个题目详情
# -----------------------------
def get_problem_detail(slug):
    variables = {"titleSlug": slug}
    resp = requests.post(BASE_URL, headers=HEADERS, json={"query": query_detail, "variables": variables})
    data = resp.json()["data"]["question"]
    return data

# -----------------------------
# 主程序
# -----------------------------
def main():
    all_problems = get_all_problems()
    results = []

    for p in tqdm(all_problems, desc="Fetching details"):
        try:
            detail = get_problem_detail(p["titleSlug"])
            results.append(detail)
            time.sleep(0.3)
        except Exception as e:
            print(f"❌ Error fetching {p['titleSlug']}: {e}")

    # 保存结果
    with open("leetcode_problems.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print("🎉 All problems saved to leetcode_problems.json")

if __name__ == "__main__":
    main()
