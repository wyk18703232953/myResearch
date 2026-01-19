# -*- coding: utf-8 -*-
"""
Fusion LLM Refine Script - Universal Strategy V14

该脚本实现了LLM静态分析与动态运行时拟合结果的融合策略，用于更准确地确定代码的时间复杂度。
核心功能包括：
1. 读取LLM静态分析结果和动态拟合结果
2. 基于拟合质量指标评估拟合结果的可信度
3. 使用通用融合策略，不依赖提前知道代码类型
4. 生成融合分析报告
5. 针对不同类型的特殊保护机制

通用融合策略：
- 不依赖提前知道代码类型0
- 基于拟合质量指标（R²、BIC差距、置信度分数等）判断拟合结果可信度
- 对于高可信度拟合，考虑覆盖LLM结果
- 对于低可信度拟合，主要依赖LLM结果
- 针对constant类型，增强保护机制，显著提高覆盖门槛
- 针对nlogn类型，增强保护机制，进一步降低覆盖概率
- 针对其他类型，优化融合策略，提高拟合结果利用率
- 改进复查逻辑，减少不必要的复查
- 更精细的类型保护策略
"""
import json
import os
import re
from typing import Dict, List, Optional, Tuple

from openai import OpenAI

# 配置文件路径
LLM_RESULTS_PATH = "/home/wuyankai/myResearch/codeComplex/results/LLM/ast_llm_results1_demo_filtered.json"
FIT_RESULTS_ROOT = "/home/wuyankai/myResearch/codeComplex/demo/filteredData/python"
DATA_ROOT = "/home/wuyankai/myResearch/codeComplex/data/filteredData/python"
ONLY_CODE_ROOT = "/home/wuyankai/myResearch/codeComplex/data/onlyCode/python"

# 输出文件路径
OUTPUT_JSON = "/home/wuyankai/myResearch/codeComplex/results/fusion_llm_report_universal_v14.json"
OUTPUT_TXT = "/home/wuyankai/myResearch/codeComplex/results/fusion_llm_report_universal_v14.txt"

# OpenAI API配置
DEFAULT_API_KEY = "sk-3sNQAO5ydpVp29WWoCqvM7Ajqzd1I5WKOpe29cpoT3DoMrZe"
DEFAULT_BASE_URL = "https://yunwu.ai/v1"

EXCLUDED_TYPES = {"np"}

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

DEFAULT_CANDIDATES = ["logn", "linear", "nlogn", "quadratic", "cubic", "constant"]

# 通用融合策略参数
# 拟合质量评估阈值 - 保持较高门槛，确保拟合结果质量
R2_THRESHOLD = 0.95  # R²阈值，高于此值认为拟合质量高
BIC_DIFF_THRESHOLD = 10  # BIC差距阈值，高于此值认为模型区分度大
CONFIDENCE_THRESHOLD = 0.90  # 置信度分数阈值，高于此值认为拟合可信
VALID_POINTS_THRESHOLD = 10  # 有效数据点阈值，高于此值认为数据充分

# 针对不同类型的特殊阈值
# constant类型需要极高的置信度和更大的差异
CONSTANT_CONFIDENCE_THRESHOLD = 0.98  # constant类型需要极高的置信度
CONSTANT_DELTA_LLM_THRESHOLD = 0.40  # constant类型需要非常大的LLM差异
CONSTANT_BIC_DIFF_THRESHOLD = 15  # constant类型需要更大的模型区分度

# nlogn类型需要特殊保护，因为拟合准确率较低
NLOGN_DELTA_LLM_THRESHOLD = 0.40  # nlogn类型需要更大的LLM差异
NLOGN_CONFIDENCE_THRESHOLD = 0.98  # nlogn类型需要更高的置信度
NLOGN_BIC_DIFF_THRESHOLD = 12  # nlogn类型需要更大的模型区分度

# 融合决策阈值
DELTA_LLM_THRESHOLD = 0.20  # LLM与拟合结果的差异阈值，高于此值才考虑覆盖
DELTA_FIT_THRESHOLD = 0.15  # 最佳拟合与次佳拟合的差异阈值

# 复查相关参数
RECHECK_THRESHOLD = 0.80  # 只有当置信度低于此值时才进行复查



def normalize_label(raw: Optional[str]) -> Optional[str]:
    """
    将原始复杂度标签归一化为标准标签
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

    # 处理包含常数因子的情况
    if re.search(r"n\s*[·*]\s*\d+", text):
        return "linear"
    # 处理包含多个项的情况
    if re.search(r"n\s*\+", text) or re.search(r"\+\s*n", text):
        return "linear"
    if re.search(r"log\s*\w+", text) and not re.search(r"n", text):
        return "logn"
    
    # 优先检查完整匹配
    sorted_keys = ["nlogn", "logn", "linear", "quadratic", "cubic", "constant", "np"]
    
    for key in sorted_keys:
        if key not in EQUIVALENCE:
            continue
        variants = EQUIVALENCE[key]
        
        if text in variants or text_compact in variants:
            return key
        
        for v in variants:
            if f" {v} " in f" {text} " or f" {v} " in f" {text_compact} ":
                return key
            if text.startswith(f"{v} ") or text.endswith(f" {v}"):
                return key
            if text_compact.startswith(f"{v}") or text_compact.endswith(f"{v}"):
                return key
    
    # 兜底处理
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
    """
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("detailed_records", [])



def resolve_code_path(complexity_id: str) -> Optional[str]:
    """
    解析代码文件路径
    """
    parts = complexity_id.split("_", 2)
    if len(parts) < 3:
        return None
    complexity_type = parts[1]
    filename = f"{complexity_id}.py"
    fallback = os.path.join(ONLY_CODE_ROOT, complexity_type, filename)
    if os.path.exists(fallback):
        return fallback
    return None



def load_fit_report(complexity_id: str) -> Tuple[Optional[Dict], Optional[str]]:
    """
    加载拟合报告
    """
    parts = complexity_id.split("_", 2)
    if len(parts) < 3:
        return None, None
    
    complexity_type = parts[1]
    result_dir = os.path.join(FIT_RESULTS_ROOT, complexity_type, f"results_{complexity_id}")
    report_path = os.path.join(result_dir, "analysis_report.json")
    
    if not os.path.exists(report_path):
        return None, None
    
    with open(report_path, "r", encoding="utf-8") as f:
        report = json.load(f)
    
    return report, report_path



def get_confidence_scores(report: Dict) -> Dict[str, float]:
    """
    从拟合报告中提取各模型的置信度分数
    """
    if not report:
        return {}
    
    models = report.get("models", {})
    conf_scores = {}
    
    for name, data in models.items():
        label = MODEL_NAME_TO_LABEL.get(name)
        if label:
            # 优先使用置信度分数，否则使用R²值
            score = data.get("confidence_score", data.get("r2", 0))
            conf_scores[label] = score
    
    return conf_scores



def evaluate_fit_quality(fit_report: Dict, y_fit: str, conf_scores: Dict[str, float], 
                        y_llm: Optional[str] = None) -> Dict[str, bool]:
    """
    评估拟合结果的质量，返回各项质量指标的布尔值
    
    参数:
    fit_report: 拟合报告字典
    y_fit: 最佳拟合复杂度
    conf_scores: 各模型的置信度分数
    y_llm: LLM预测的复杂度（用于类型特定评估）
    
    返回:
    包含各项质量指标的字典
    """
    quality_metrics = {
        "has_high_r2": False,
        "has_large_model_diff": False,
        "has_wide_n_range": False,
        "has_high_confidence": False,
        "is_trustworthy": False,
        "is_extremely_trustworthy": False,
        "confidence_score": 0.0,
    }
    
    if not fit_report or not y_fit:
        return quality_metrics
    
    models = fit_report.get("models", {})
    if not models:
        return quality_metrics
    
    # 1. 检查R²值（拟合优度）
    best_model_data = models.get(y_fit.capitalize(), {})
    r2 = best_model_data.get("r2", 0)
    quality_metrics["has_high_r2"] = r2 >= R2_THRESHOLD
    
    # 2. 检查模型区分度（BIC差距）
    bic_diff = 0
    if len(models) > 1:
        bic_values = [(model_name, data.get("bic", float('inf'))) 
                     for model_name, data in models.items()]
        bic_values.sort(key=lambda x: x[1])
        if len(bic_values) >= 2:
            best_bic = bic_values[0][1]
            second_bic = bic_values[1][1]
            bic_diff = abs(second_bic - best_bic)
            
            # 针对不同类型使用不同的BIC差距阈值
            if y_fit == "constant" or y_llm == "constant":
                quality_metrics["has_large_model_diff"] = bic_diff >= CONSTANT_BIC_DIFF_THRESHOLD
            elif y_fit == "nlogn" or y_llm == "nlogn":
                quality_metrics["has_large_model_diff"] = bic_diff >= NLOGN_BIC_DIFF_THRESHOLD
            else:
                quality_metrics["has_large_model_diff"] = bic_diff >= BIC_DIFF_THRESHOLD
    
    # 3. 检查数据覆盖范围
    valid_points = fit_report.get("valid_points", 0)
    quality_metrics["has_wide_n_range"] = valid_points >= VALID_POINTS_THRESHOLD
    
    # 4. 检查置信度分数
    conf_best = conf_scores.get(y_fit, 0)
    quality_metrics["has_high_confidence"] = conf_best >= CONFIDENCE_THRESHOLD
    quality_metrics["confidence_score"] = conf_best
    
    # 5. 综合评估拟合结果是否可信
    quality_metrics["is_trustworthy"] = (
        quality_metrics["has_high_r2"] and
        quality_metrics["has_large_model_diff"] and
        quality_metrics["has_wide_n_range"] and
        quality_metrics["has_high_confidence"]
    )
    
    # 6. 评估是否为极高可信度（用于constant和nlogn类型的特殊保护）
    extremely_trustworthy = False
    
    if y_llm == "constant" and y_fit != "constant":
        # 当LLM预测为constant，拟合结果不是constant时，需要极高的可信度才考虑覆盖
        extremely_trustworthy = (
            quality_metrics["is_trustworthy"] and
            conf_best >= CONSTANT_CONFIDENCE_THRESHOLD and
            bic_diff >= CONSTANT_BIC_DIFF_THRESHOLD
        )
    elif y_llm == "nlogn" and y_fit != "nlogn":
        # 当LLM预测为nlogn，拟合结果不是nlogn时，需要极高的可信度才考虑覆盖
        extremely_trustworthy = (
            quality_metrics["is_trustworthy"] and
            conf_best >= NLOGN_CONFIDENCE_THRESHOLD and
            bic_diff >= NLOGN_BIC_DIFF_THRESHOLD
        )
    elif y_llm and y_fit and y_llm != y_fit:
        # 其他类型的差异情况，保持标准可信度即可
        extremely_trustworthy = quality_metrics["is_trustworthy"]
    else:
        # 结果一致时，可信度足够
        extremely_trustworthy = quality_metrics["is_trustworthy"]
    
    quality_metrics["is_extremely_trustworthy"] = extremely_trustworthy
    
    return quality_metrics



def llm_recheck(code: str, y_llm: Optional[str] = None, y_fit: Optional[str] = None, 
                fit_report: Optional[Dict] = None, conf_scores: Optional[Dict[str, float]] = None) -> Tuple[Optional[str], Optional[str]]:
    """
    使用LLM重新检查代码的时间复杂度
    """
    import time
    
    api_key = os.getenv("OPENAI_API_KEY", DEFAULT_API_KEY)
    base_url = os.getenv("OPENAI_BASE_URL", DEFAULT_BASE_URL)
    client = OpenAI(api_key=api_key, base_url=base_url)
    
    # 改进system_prompt，更明确的指令
    system_prompt = """你是一位资深的时间复杂度分析专家，专门负责分析给定代码的最坏时间复杂度。

请严格遵守以下规则：
1. 你只能从以下术语中选择并输出一个：constant、linear、logn、nlogn、quadratic、cubic、exponential
2. 你必须只输出一个复杂度术语，不允许输出其它任何文字、符号、解释、标点或格式
3. 请仔细分析代码的嵌套循环、递归调用、数据结构操作等关键部分
4. 考虑最坏情况下的执行次数
5. 忽略常数因子，关注主导项
6. 如果无法判断，你必须输出"exponential"，不得输出其它信息
"""
    
    # 构建更优化的用户提示词
    user_prompt = f"""请分析以下代码的最坏时间复杂度，并只输出一个复杂度术语（constant、linear、logn、nlogn、quadratic、cubic、exponential）：

```
{code}
```
"""
    
    # 只在可信时提供拟合信息，并优化提示
    if y_fit and fit_report and conf_scores:
        conf_best = conf_scores.get(y_fit, 0)
        if conf_best >= CONFIDENCE_THRESHOLD:
            user_prompt += f"""

参考信息：动态运行时拟合分析建议复杂度为 {y_fit}，拟合置信度分数为 {conf_best:.4f}。
拟合结果显示该复杂度模型与实际运行数据匹配度较高。
请结合代码结构和拟合结果，综合判断代码的时间复杂度。
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
                timeout=30
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



def load_fit_stats() -> Dict[str, Dict[str, int]]:
    """
    加载各复杂度类型的拟合统计数据
    """
    fit_stats = {}
    complexity_types = ["logn", "linear", "nlogn", "quadratic", "cubic", "constant"]
    
    for type_name in complexity_types:
        stats_path = os.path.join(FIT_RESULTS_ROOT, type_name, f"stats_{type_name}.json")
        if os.path.exists(stats_path):
            try:
                with open(stats_path, "r", encoding="utf-8") as f:
                    stats = json.load(f)
                fit_stats[type_name] = {
                    "total": stats.get("total", 0),
                    "success": stats.get("success", 0),
                    "failed": stats.get("failed", 0)
                }
            except Exception as e:
                print(f"加载{type_name}拟合统计数据失败: {e}")
                fit_stats[type_name] = {
                    "total": 0,
                    "success": 0,
                    "failed": 0
                }
    
    return fit_stats



def main() -> None:
    """
    主函数，执行LLM静态分析与动态运行时拟合结果的融合分析
    """
    # 加载LLM分析记录
    records = load_llm_records(LLM_RESULTS_PATH)
    
    # 加载拟合统计数据
    fit_stats = load_fit_stats()

    # 初始化统计摘要
    summary = {
        "total_records": len(records),
        "processed": 0,
        "skipped": 0,
        "llm_correct": 0,
        "fit_correct": 0,
        "fusion_correct": 0,
        "rechecked": 0,
        "fit_trustworthy_count": 0,
        "fit_extremely_trustworthy_count": 0,
        "fit_untrustworthy_count": 0,
        "llm_fit_agree": 0,
        "llm_fit_disagree": 0,
        "types": {}
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

        # 检查是否需要跳过当前记录
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

        # 评估拟合质量（考虑LLM预测类型）
        quality_metrics = evaluate_fit_quality(fit_report, y_fit, conf_scores, y_llm) if y_fit else {"confidence_score": 0}
        is_fit_trustworthy = quality_metrics.get("is_trustworthy", False)
        is_fit_extremely_trustworthy = quality_metrics.get("is_extremely_trustworthy", False)
        confidence_score = quality_metrics.get("confidence_score", 0.0)

        # 统计拟合质量
        if is_fit_extremely_trustworthy:
            summary["fit_extremely_trustworthy_count"] += 1
            summary["fit_trustworthy_count"] += 1
        elif is_fit_trustworthy:
            summary["fit_trustworthy_count"] += 1
        else:
            summary["fit_untrustworthy_count"] += 1

        # 统计LLM与拟合结果的一致性
        if y_llm == y_fit:
            summary["llm_fit_agree"] += 1
        else:
            summary["llm_fit_disagree"] += 1

        # 融合策略 - 优化版
        y_final = y_llm
        rechecked = False
        recheck_raw = None
        recheck_norm = None

        if y_llm == y_fit:
            # 1. LLM与拟合结果一致，直接使用
            y_final = y_llm

        elif not y_fit or confidence_score < CONFIDENCE_THRESHOLD:
            # 2. 没有拟合结果或拟合结果不可信，使用LLM结果
            y_final = y_llm
        else:
            # 3. 融合决策逻辑 - 精细化类型保护策略
            use_fit = False
            
            # 3.1 针对constant类型的特殊保护
            if y_llm == "constant" and y_fit != "constant":
                # 当LLM预测为constant，拟合结果不是constant时，需要极高的可信度才考虑覆盖
                use_fit = (
                    is_fit_extremely_trustworthy and
                    delta_llm >= CONSTANT_DELTA_LLM_THRESHOLD and
                    delta_fit >= DELTA_FIT_THRESHOLD
                )
            # 3.2 针对nlogn类型的特殊保护
            elif y_llm == "nlogn" and y_fit != "nlogn":
                # 当LLM预测为nlogn，拟合结果不是nlogn时，需要极高的可信度才考虑覆盖
                use_fit = (
                    is_fit_extremely_trustworthy and
                    delta_llm >= NLOGN_DELTA_LLM_THRESHOLD and
                    delta_fit >= DELTA_FIT_THRESHOLD
                )
            # 3.3 针对其他类型，优化融合策略
            elif delta_llm >= DELTA_LLM_THRESHOLD and delta_fit >= DELTA_FIT_THRESHOLD:
                # 差异足够大时，信任拟合结果
                use_fit = True
            elif confidence_score >= 0.95:
                # 置信度极高时，信任拟合结果
                use_fit = True
            elif confidence_score >= 0.85 and is_fit_trustworthy:
                # 置信度较高且拟合可信时，信任拟合结果
                use_fit = True
            
            if use_fit:
                # 直接使用拟合结果
                y_final = y_fit
            else:
                # 只有当置信度非常低时才进行复查
                if confidence_score < RECHECK_THRESHOLD:
                    # 4. LLM复查
                    code_path = resolve_code_path(complexity_id)
                    if code_path:
                        try:
                            with open(code_path, "r", encoding="utf-8") as f:
                                code = f.read()
                            recheck_raw, recheck_norm = llm_recheck(code, y_llm, y_fit, fit_report, conf_scores)
                            rechecked = True
                            summary["rechecked"] += 1
                            
                            # 处理复查结果
                            if recheck_norm == y_fit:
                                y_final = y_fit
                            elif recheck_norm == y_llm:
                                y_final = y_llm
                            elif recheck_norm:
                                y_final = recheck_norm
                            else:
                                y_final = y_llm
                        except Exception as e:
                            # 复查失败，使用LLM结果
                            y_final = y_llm
                    else:
                        # 无法获取代码，使用LLM结果
                        y_final = y_llm
                else:
                    # 不复查，使用LLM结果
                    y_final = y_llm

        # 计算准确率
        llm_correct = compare_complexity(y_llm, expected)
        fit_correct = compare_complexity(y_fit, expected) if y_fit else False
        fusion_correct = compare_complexity(y_final, expected)

        # 更新统计信息
        summary["processed"] += 1
        if llm_correct:
            summary["llm_correct"] += 1
        if fusion_correct:
            summary["fusion_correct"] += 1
        
        # 更新类型统计
        if expected not in EXCLUDED_TYPES:
            type_key = expected
            
            if type_key not in summary["types"]:
                summary["types"][type_key] = {
                    "total": 0,
                    "llm_correct": 0,
                    "fit_correct": 0,
                    "fusion_correct": 0
                }
            
            summary["types"][type_key]["total"] += 1
            if llm_correct:
                summary["types"][type_key]["llm_correct"] += 1
            if fusion_correct:
                summary["types"][type_key]["fusion_correct"] += 1

        # 保存详细结果
        detailed.append(
            {
                "complexity_id": complexity_id,
                "expected_complexity": expected,
                "y_llm": y_llm,
                "y_fit": y_fit,
                "y_final": y_final,
                "conf_scores": conf_scores,
                "conf_best": conf_best,
                "delta_llm": delta_llm,
                "delta_fit": delta_fit,
                "fit_quality": quality_metrics,
                "rechecked": rechecked,
                "recheck_raw_output": recheck_raw,
                "recheck_normalized": recheck_norm,
                "llm_correct": llm_correct,
                "fit_correct": fit_correct,
                "fusion_correct": fusion_correct,
            }
        )

    # 使用fit_stats数据更新各类型的fit_correct计数
    total_fit_correct = 0
    for type_name, stats in summary["types"].items():
        if type_name in fit_stats:
            summary["types"][type_name]["fit_correct"] = fit_stats[type_name]["success"]
            total_fit_correct += fit_stats[type_name]["success"]
    
    # 更新总体的fit_correct计数
    summary["fit_correct"] = total_fit_correct
    
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
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    # 保存文本格式报告
    with open(OUTPUT_TXT, "w", encoding="utf-8") as f:
        f.write("Fusion LLM Refinement Report (Universal Strategy V14)\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Total records: {summary['total_records']}\n")
        f.write(f"Processed: {summary['processed']}\n")
        f.write(f"Skipped: {summary['skipped']}\n")
        f.write(f"\nLLM-only accuracy: {summary['llm_correct']}/{summary['processed']} ({summary['llm_correct']/summary['processed']*100:.2f}%)\n")
        f.write(f"Fit-only accuracy: {summary['fit_correct']}/{summary['processed']} ({summary['fit_correct']/summary['processed']*100:.2f}%)\n")
        f.write(f"Fusion accuracy: {summary['fusion_correct']}/{summary['processed']} ({summary['fusion_correct']/summary['processed']*100:.2f}%)\n")
        f.write(f"\nLLM-Fit agreement: {summary['llm_fit_agree']}\n")
        f.write(f"LLM-Fit disagreement: {summary['llm_fit_disagree']}\n")
        f.write(f"Trustworthy fitting evidence: {summary['fit_trustworthy_count']}\n")
        f.write(f"Extremely trustworthy fitting evidence: {summary['fit_extremely_trustworthy_count']}\n")
        f.write(f"Untrustworthy fitting evidence: {summary['fit_untrustworthy_count']}\n")
        f.write(f"Rechecked by LLM: {summary['rechecked']}\n")
        
        # 添加各类型准确率统计
        f.write("\n" + "=" * 50 + "\n")
        f.write("类型准确率统计\n")
        f.write("=" * 50 + "\n")
        
        sorted_types = sorted(summary["types"].items())
        
        for type_name, stats in sorted_types:
            total = stats["total"]
            llm_acc = (stats["llm_correct"] / total * 100) if total > 0 else 0
            fit_acc = (stats["fit_correct"] / total * 100) if total > 0 else 0
            fusion_acc = (stats["fusion_correct"] / total * 100) if total > 0 else 0
            
            f.write(f"{type_name.ljust(15)} 总: {total:4d} LLM: {stats['llm_correct']:4d} ({llm_acc:6.2f}%) " + \
                   f"Fit: {stats['fit_correct']:4d} ({fit_acc:6.2f}%) " + \
                   f"Fusion: {stats['fusion_correct']:4d} ({fusion_acc:6.2f}%)\n")

    # 打印最终结果
    print(f"\nReport saved: {OUTPUT_JSON}")
    print(f"Text summary saved: {OUTPUT_TXT}")
    print(f"\nSummary:")
    print(f"LLM-only accuracy: {summary['llm_correct']}/{summary['processed']} ({summary['llm_correct']/summary['processed']*100:.2f}%)")
    print(f"Fit-only accuracy: {summary['fit_correct']}/{summary['processed']} ({summary['fit_correct']/summary['processed']*100:.2f}%)")
    print(f"Fusion accuracy: {summary['fusion_correct']}/{summary['processed']} ({summary['fusion_correct']/summary['processed']*100:.2f}%)")
    
    # 打印各类型准确率
    print(f"\n{'-'*60}")
    print("各类型准确率统计：")
    print(f"{'-'*60}")
    
    for type_name, stats in sorted_types:
        total = stats["total"]
        llm_acc = (stats["llm_correct"] / total * 100) if total > 0 else 0
        fit_acc = (stats["fit_correct"] / total * 100) if total > 0 else 0
        fusion_acc = (stats["fusion_correct"] / total * 100) if total > 0 else 0
        
        print(f"{type_name.ljust(12)} 总: {total:4d} LLM: {stats['llm_correct']:4d} ({llm_acc:6.2f}%) " + \
              f"Fit: {stats['fit_correct']:4d} ({fit_acc:6.2f}%) " + \
              f"Fusion: {stats['fusion_correct']:4d} ({fusion_acc:6.2f}%)")
    
    print(f"{'-'*60}")
    
    # 生成用户要求的JSON格式总结文件
    summary_json = []
    for record in detailed:
        summary_entry = {
            "expected_complexity": record.get("expected_complexity", ""),
            "y_llm": record.get("y_llm", ""),
            "y_fit": record.get("y_fit", ""),
            "y_final": record.get("y_final", "")
        }
        summary_json.append(summary_entry)
    
    # 保存总结文件
    SUMMARY_OUTPUT_JSON = "/home/wuyankai/myResearch/codeComplex/results/fusion_llm_summary_v14.json"
    with open(SUMMARY_OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(summary_json, f, ensure_ascii=False, indent=2)
    
    print(f"\n总结文件已生成: {SUMMARY_OUTPUT_JSON}")



if __name__ == "__main__":
    main()