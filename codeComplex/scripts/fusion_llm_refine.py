# -*- coding: utf-8 -*-
"""
Fusion LLM Refine Script

该脚本实现了LLM静态分析与动态运行时拟合结果的融合策略，用于更准确地确定代码的时间复杂度。
核心功能包括：
1. 读取LLM静态分析结果和动态拟合结果
2. 基于置信度分数评估拟合证据的强度
3. 当LLM与拟合结果不一致时，使用LLM进行重新检查
4. 生成融合分析报告
"""
import json
import os
import re
from typing import Dict, List, Optional, Tuple

from openai import OpenAI

# 配置文件路径
LLM_RESULTS_PATH = "/home/wuyankai/myResearch/codeComplex/results/LLM/ast_llm_results1_demo_filtered.json"  # LLM分析结果路径
FIT_RESULTS_ROOT = "/home/wuyankai/myResearch/codeComplex/demo/filteredData/python"  # 拟合结果根目录
DATA_ROOT = "/home/wuyankai/myResearch/codeComplex/data/filteredData/python"  # 数据根目录
ONLY_CODE_ROOT = "/home/wuyankai/myResearch/codeComplex/data/onlyCode/python"  # 仅代码数据根目录

# 输出文件路径
OUTPUT_JSON = "/home/wuyankai/myResearch/codeComplex/results/fusion_llm_report.json"  # JSON格式报告
OUTPUT_TXT = "/home/wuyankai/myResearch/codeComplex/results/fusion_llm_report.txt"  # 文本格式报告

# OpenAI API配置
DEFAULT_API_KEY = "sk-3sNQAO5ydpVp29WWoCqvM7Ajqzd1I5WKOpe29cpoT3DoMrZe"  # 默认API密钥
DEFAULT_BASE_URL = "https://yunwu.ai/v1"  # API基础URL

EXCLUDED_TYPES = {"constant", "np"}  # 排除的复杂度类型

# 模型名称到标签的映射
MODEL_NAME_TO_LABEL = {
    "Constant": "constant",
    "Logarithmic": "logn",
    "Linear": "linear",
    "N Log N": "nlogn",
    "Quadratic": "quadratic",
    "Cubic": "cubic",
}

# 复杂度术语等价关系（用于归一化）
EQUIVALENCE = {
    "constant": {"constant", "o(1)", "1"},
    "linear": {"linear", "o(n)", "n"},
    "logn": {"logn", "log n", "o(log n)", "o(logn)"},
    "nlogn": {"nlogn", "n log n", "o(n log n)", "o(n logn)"},
    "quadratic": {"quadratic", "o(n^2)", "n^2"},
    "cubic": {"cubic", "o(n^3)", "n^3"},
    "np": {"np", "o(n^p)", "n^p", "exponential", "o(2^n)", "2^n"},
}

DEFAULT_CANDIDATES = ["logn", "linear", "nlogn", "quadratic", "cubic"]  # 默认的复杂度候选类型

# 融合策略参数
CONFIDENCE_THRESHOLD = 0.8  # 置信度阈值
DELTA_LLM_THRESHOLD = 0.1  # LLM与拟合结果的最小差异阈值
DELTA_FIT_THRESHOLD = 0.1  # 最佳拟合与次佳拟合的最小差异阈值（提高此值使系统更严格）


def normalize_label(raw: Optional[str]) -> Optional[str]:
    """
    将原始复杂度标签归一化为标准标签
    
    参数:
    raw: 原始复杂度标签字符串
    
    返回:
    归一化后的标准复杂度标签，如"logn"、"linear"等
    """
    if not raw:
        return None
    text = raw.strip().lower()
    
    # 移除时间复杂度前缀
    text = re.sub(r"^时间复杂度[：:]\s*", "", text)
    
    # 提取O()符号中的内容
    o_match = re.search(r"o\s*\(([^)]+)\)", text)
    if o_match:
        text = o_match.group(1).strip()
    
    text_compact = re.sub(r"\s+", "", text)

    # 处理包含常数因子的情况，如O(n · 1000) -> linear
    if re.search(r"n\s*[·*]\s*\d+", text):
        return "linear"
    # 处理包含多个项的情况，如O(n + log X) -> linear（n项主导）
    if re.search(r"n\s*\+", text) or re.search(r"\+\s*n", text):
        return "linear"
    if re.search(r"log\s*\w+", text) and not re.search(r"n", text):
        return "logn"
    
    # 优先检查完整匹配，然后检查包含关系
    # 按照复杂度的特异性排序，避免前缀匹配问题（如logn被误判为linear）
    sorted_keys = ["nlogn", "logn", "linear", "quadratic", "cubic", "constant", "np"]
    
    for key in sorted_keys:
        if key not in EQUIVALENCE:
            continue
        variants = EQUIVALENCE[key]
        
        # 优先检查精确匹配
        if text in variants or text_compact in variants:
            return key
        
        # 然后检查变体是否在文本中（完整单词匹配）
        for v in variants:
            if f" {v} " in f" {text} " or f" {v} " in f" {text_compact} ":
                return key
            # 检查变体是否是文本的开头或结尾
            if text.startswith(f"{v} ") or text.endswith(f" {v}"):
                return key
            if text_compact.startswith(f"{v}") or text_compact.endswith(f"{v}"):
                return key
    
    # 最后的兜底处理，尝试提取主要复杂度项
    if "nlog" in text_compact:
        return "nlogn"
    if "log" in text_compact and "n" in text_compact:
        return "logn"
    if "n" in text_compact and not any(p in text_compact for p in ["^2", "^3", "^p", "2^"]):
        return "linear"
    if "^2" in text_compact:
        return "quadratic"
    if "^3" in text_compact:
        return "cubic"
    if any(p in text_compact for p in ["^p", "2^", "exponential"]):
        return "np"
    if any(p in text_compact for p in ["constant", "o(1)", "1"]):
        return "constant"
    
    return None


def compare_complexity(actual: Optional[str], expected: str) -> bool:
    """
    比较实际复杂度与期望复杂度是否匹配
    
    参数:
    actual: 实际复杂度标签
    expected: 期望复杂度标签
    
    返回:
    实际复杂度与期望复杂度是否匹配的布尔值
    """
    if not actual:
        return False
    expected = expected.strip().lower()
    if expected in EQUIVALENCE:
        return actual in EQUIVALENCE[expected] or actual == expected
    return actual == expected


def load_llm_records(path: str) -> List[Dict]:
    """
    加载LLM分析结果记录
    
    参数:
    path: LLM分析结果文件路径
    
    返回:
    详细记录列表
    """
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("detailed_records", [])


def resolve_code_path(complexity_id: str) -> Optional[str]:
    """
    解析代码文件路径
    
    参数:
    complexity_id: 复杂度ID，格式为 python_<type>_<index>
    
    返回:
    代码文件的绝对路径，如果找不到则返回None
    """
    parts = complexity_id.split("_", 2)
    if len(parts) < 3:
        return None
    complexity_type = parts[1]
    filename = f"{complexity_id}.py"
    # primary = os.path.join(DATA_ROOT, complexity_type, filename)
    # if os.path.exists(primary):
    #     return primary
    fallback = os.path.join(ONLY_CODE_ROOT, complexity_type, filename)
    if os.path.exists(fallback):
        return fallback
    return None


def load_fit_report(complexity_id: str) -> Tuple[Optional[Dict], Optional[str]]:
    """
    加载拟合报告
    
    参数:
    complexity_id: 复杂度ID，格式为 python_<type>_<index>
    
    返回:
    拟合报告字典和报告路径，如果找不到或加载失败则返回None和路径
    """
    parts = complexity_id.split("_", 2)
    if len(parts) < 3:
        return None, None
    complexity_type = parts[1]
    report_path = os.path.join(
        FIT_RESULTS_ROOT, complexity_type, f"results_{complexity_id}", "analysis_report.json"
    )
    if not os.path.exists(report_path):
        return None, report_path
    try:
        with open(report_path, "r", encoding="utf-8") as f:
            return json.load(f), report_path
    except Exception:
        return None, report_path


def get_confidence_scores(report: Dict) -> Dict[str, float]:
    """
    从拟合报告中提取置信度分数
    
    参数:
    report: 拟合报告字典
    
    返回:
    以复杂度标签为键，置信度分数为值的字典
    """
    if not report:
        return {}
    
    conf_scores = {}
    models = report.get("models", {})
    # print(models)
    # import time
    # time.sleep(100)
    for name, data in models.items():
        if not isinstance(data, dict):
            continue
        score = data.get("confidence_score")
        if score is None:
            score = data.get("r2")
        if score is not None:
            label = MODEL_NAME_TO_LABEL.get(name)
            if label:
                conf_scores[label] = score
    
    return conf_scores


def get_valid_points(report: Dict) -> int:
    """
    从拟合报告中获取有效数据点数量
    
    参数:
    report: 拟合报告字典
    
    返回:
    有效数据点数量
    """
    if not report:
        return 0
    return report.get("valid_points", 0)


def llm_recheck(code: str, y_llm: Optional[str] = None, y_fit: Optional[str] = None, fit_report: Optional[Dict] = None) -> Tuple[Optional[str], Optional[str]]:
    """
    使用LLM重新检查代码的时间复杂度
    
    参数:
    code: 要分析的代码字符串
    
    返回:
    LLM原始输出和归一化后的复杂度标签
    """
    import time
    
    api_key = os.getenv("OPENAI_API_KEY", DEFAULT_API_KEY)
    base_url = os.getenv("OPENAI_BASE_URL", DEFAULT_BASE_URL)
    client = OpenAI(api_key=api_key, base_url=base_url)
    
    # 使用更严格、更规范的提示词
    system_prompt = """你是一名资深的时间复杂度分析专家，专门负责分析给定代码的最坏时间复杂度。

    为了确保输出一致且严格规范，请严格遵守以下规则：

    1. 你必须基于代码的真实结构进行时间复杂度分析。
    2. 你只能从以下术语中选择并输出一个：constant、linear、logn、nlogn、quadratic、cubic、exponential。
    3. 你必须只输出一个复杂度术语，不允许输出其它任何文字、符号、解释、标点或格式。
    4. 不允许出现代码、推导步骤或任何技术性说明。
    5. 如果无法判断，你必须输出"exponential"，不得输出其它信息。
    """
    
    # 构建包含拟合数据的用户提示
    fit_info = ""
    if y_fit and fit_report:
        models = fit_report.get("models", {})
        # 格式化所有拟合模型的分数
        fit_models_info = ""
        for model_name, model_data in models.items():
            conf_score = model_data.get('confidence_score', 'N/A')
            if conf_score != 'N/A':
                conf_score = f"{conf_score:.4f}"
            fit_models_info += f"- {model_name}: {conf_score}\n"
        
        # 使用多行f-string正确格式化
        fit_info = f"""\n\n拟合分析参考信息：
- 原始LLM判断：{y_llm}
- 最佳拟合复杂度：{y_fit}
- 所有模型拟合分数：
{fit_models_info}- 有效数据点：{fit_report.get('valid_points', 'N/A')}"""
    
    user_prompt = f"""请分析以下代码的最坏时间复杂度，并只输出一个复杂度术语（constant、linear、logn、nlogn、quadratic、cubic、exponential），不能输出其他内容：

    ```
    {code}
    ```
    
    {fit_info}
    """
    
    max_retries = 3
    retry_delay = 1
    
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="gpt-5.1",
                temperature=0.0,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                stream=False,
                timeout=30  # 设置30秒超时
            )
            
            if not response.choices:
                print(f"LLM API响应无choices字段，重试 {attempt+1}/{max_retries}")
                time.sleep(retry_delay)
                retry_delay *= 2
                continue
                
            raw_output = response.choices[0].message.content.strip()
            if not raw_output:
                print(f"LLM API返回空内容，重试 {attempt+1}/{max_retries}")
                time.sleep(retry_delay)
                retry_delay *= 2
                continue
                
            normalized = normalize_label(raw_output)
            # 只有在原始输出不为空但归一化失败时才重试
            if not normalized and attempt < max_retries - 1:
                print(f"尝试归一化LLM输出失败: '{raw_output}'，重试 {attempt+1}/{max_retries}")
                time.sleep(retry_delay)
                retry_delay *= 2
                continue
                
            return raw_output, normalized
        except Exception as e:
            print(f"LLM API调用失败 (尝试 {attempt+1}/{max_retries}): {str(e)}")
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
                retry_delay *= 2
            else:
                return None, None
    
    return None, None


def main() -> None:
    """
    主函数，执行LLM静态分析与动态拟合结果的融合分析
    """
    # 加载LLM分析记录
    records = load_llm_records(LLM_RESULTS_PATH)

    # 初始化统计摘要
    summary = {
        "total_records": len(records),
        "processed": 0,
        "skipped": 0,
        "llm_correct": 0,
        "fit_correct": 0,
        "fusion_correct": 0,
        "rechecked": 0,
        "fit_strong_count": 0,
        "llm_fit_agree": 0,
        "llm_fit_disagree": 0,
    }

    # 详细结果列表
    detailed = []

    # 遍历每个记录进行处理
    for idx, record in enumerate(records, 1):
        complexity_id = record.get("complexity_id")
        expected = (record.get("expected_complexity") or "").strip().lower()

        # 打印进度信息
        if idx == 1 or idx % 100 == 0:
            print(f"[进度] {idx}/{len(records)} 已处理: {summary['processed']} 跳过: {summary['skipped']} 复查: {summary['rechecked']}")

        # 检查是否需要跳过当前记录（排除类型）
        if not complexity_id or expected in EXCLUDED_TYPES:
            summary["skipped"] += 1
            continue

        parts = complexity_id.split("_", 2)
        if len(parts) >= 2 and parts[1] in EXCLUDED_TYPES:
            summary["skipped"] += 1
            continue

        # 处理LLM结果
        llm_raw = record.get("model_raw_output")
        y_llm = normalize_label(llm_raw)

        # 加载拟合结果
        fit_report, fit_path = load_fit_report(complexity_id)
        conf_scores = get_confidence_scores(fit_report) if fit_report else {}
        # valid_points = get_valid_points(fit_report) if fit_report else 0

        # 获取最佳拟合结果
        if conf_scores:
            y_fit = max(conf_scores, key=conf_scores.get)
            conf_best = conf_scores[y_fit]
            # 计算次佳拟合分数
            second_best_conf = sorted(conf_scores.values(), reverse=True)[1] if len(conf_scores) > 1 else 0
        else:
            y_fit = None
            conf_best = 0
            second_best_conf = 0

        # 计算分数差异
        llm_score = conf_scores.get(y_llm, -float('inf')) if y_llm else -float('inf')
        delta_llm = conf_best - llm_score if y_llm else 0
        delta_fit = conf_best - second_best_conf

        # 高置信度拟合条件
        has_high_r2 = False
        has_large_model_diff = False
        has_wide_n_range = False
        
        # 获取拟合报告中的详细指标
        if fit_report and y_fit:
            models = fit_report.get("models", {})
            if models:
                # 检查R²值（高拟合优度）
                best_model_data = models.get(y_fit.capitalize(), {})
                r2 = best_model_data.get("r2", 0)
                has_high_r2 = r2 >= 0.95
                
                # 检查模型区分度（BIC差距）
                if len(models) > 1:
                    # 获取所有模型的BIC值
                    bic_values = [(model_name, data.get("bic", float('inf'))) 
                                 for model_name, data in models.items()]
                    # 按BIC排序（BIC越小越好）
                    bic_values.sort(key=lambda x: x[1])
                    if len(bic_values) >= 2:
                        best_bic = bic_values[0][1]
                        second_bic = bic_values[1][1]
                        # 计算BIC差距（绝对值，因为BIC越小越好）
                        bic_diff = abs(second_bic - best_bic)
                        has_large_model_diff = bic_diff >= 10
                
                # 检查数据覆盖范围（n跨至少1-2个数量级）
                valid_points = fit_report.get("valid_points", 0)
                has_wide_n_range = valid_points >= 10  # 这里暂时用有效点数作为替代，实际需要n的范围
        
        # 评估拟合证据的强度 - 只在高置信度时使用拟合结果
        fit_strong = (
            has_high_r2 and  # 高拟合优度 (R² ≥ 0.95)
            has_large_model_diff and  # 模型区分度大 (ΔBIC ≥ 10)
            has_wide_n_range and  # 数据覆盖范围广
            conf_best >= 0.95  # 高置信度分数
        )

        if fit_strong:
            summary["fit_strong_count"] += 1

        # 统计LLM与拟合结果的一致性
        if y_llm == y_fit:
            summary["llm_fit_agree"] += 1
        else:
            summary["llm_fit_disagree"] += 1
            print(f"LLM与拟合结果不一致: {complexity_id} LLM={y_llm} Fit={y_fit}")

        # 融合逻辑 - 只有在高置信度时才覆盖LLM结果
        y_final = y_llm  # 默认使用LLM结果
        rechecked = False
        recheck_raw = None
        recheck_norm = None

        if y_llm == y_fit:
            # LLM与拟合结果一致，直接使用
            y_final = y_llm
        elif fit_strong:
            # 拟合证据充分（高置信度）且与LLM结果不一致，使用拟合结果覆盖
            print(f"使用高置信度拟合结果覆盖LLM: {complexity_id}, LLM={y_llm} → Fit={y_fit}")
            y_final = y_fit
        # 否则保持LLM原始结果不变
        
        # 注意：我们已经移除了LLM重新检查的逻辑，因为根据新策略，
        # 只有在拟合高度可信时才会覆盖LLM，否则保持LLM的判断不变

        # 计算准确率
        llm_correct = compare_complexity(y_llm, expected)
        fit_correct = compare_complexity(y_fit, expected) if y_fit else False
        fusion_correct = compare_complexity(y_final, expected)

        # 更新统计信息
        summary["processed"] += 1
        if llm_correct:
            summary["llm_correct"] += 1
        if fit_correct:
            summary["fit_correct"] += 1
        if fusion_correct:
            summary["fusion_correct"] += 1

        # 保存详细结果
        detailed.append(
            {
                "complexity_id": complexity_id,
                "expected_complexity": expected,
                "y_llm": y_llm,
                "y_fit": y_fit,
                "y_final": y_final,
                "conf_scores": conf_scores,
                # "valid_points": valid_points,
                "conf_best": conf_best,
                "delta_llm": delta_llm,
                "delta_fit": delta_fit,
                "fit_strong": fit_strong,
                "rechecked": rechecked,
                "recheck_raw_output": recheck_raw,
                "recheck_normalized": recheck_norm,
                "llm_correct": llm_correct,
                "fit_correct": fit_correct,
                "fusion_correct": fusion_correct,
                "fit_report_path": fit_path,
            }
        )

    # 生成报告
    report = {
        "summary": summary,
        "input_file": LLM_RESULTS_PATH,
        "fit_results_root": FIT_RESULTS_ROOT,
        "output_json": OUTPUT_JSON,
        "output_txt": OUTPUT_TXT,
        "detailed_records": detailed,
    }

    # 保存JSON格式报告
    os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    # 保存文本格式报告
    with open(OUTPUT_TXT, "w", encoding="utf-8") as f:
        f.write("Fusion LLM Refinement Report\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Total records: {summary['total_records']}\n")
        f.write(f"Processed: {summary['processed']}\n")
        f.write(f"Skipped: {summary['skipped']}\n")
        f.write(f"\nLLM-only accuracy: {summary['llm_correct']}/{summary['processed']} ({summary['llm_correct']/summary['processed']*100:.2f}%)\n")
        f.write(f"Fit-only accuracy: {summary['fit_correct']}/{summary['processed']} ({summary['fit_correct']/summary['processed']*100:.2f}%)\n")
        f.write(f"Fusion accuracy: {summary['fusion_correct']}/{summary['processed']} ({summary['fusion_correct']/summary['processed']*100:.2f}%)\n")
        f.write(f"\nLLM-Fit agreement: {summary['llm_fit_agree']}\n")
        f.write(f"LLM-Fit disagreement: {summary['llm_fit_disagree']}\n")
        f.write(f"Strong fitting evidence: {summary['fit_strong_count']}\n")
        f.write(f"Rechecked by LLM: {summary['rechecked']}\n")

    # 打印最终结果
    print(f"\nReport saved: {OUTPUT_JSON}")
    print(f"Text summary saved: {OUTPUT_TXT}")
    print(f"\nSummary:")
    print(f"LLM-only accuracy: {summary['llm_correct']}/{summary['processed']} ({summary['llm_correct']/summary['processed']*100:.2f}%)")
    print(f"Fit-only accuracy: {summary['fit_correct']}/{summary['processed']} ({summary['fit_correct']/summary['processed']*100:.2f}%)")
    print(f"Fusion accuracy: {summary['fusion_correct']}/{summary['processed']} ({summary['fusion_correct']/summary['processed']*100:.2f}%)")


if __name__ == "__main__":
    main()
