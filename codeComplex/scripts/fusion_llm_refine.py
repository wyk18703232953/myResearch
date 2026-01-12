import json
import os
import re
from typing import Dict, List, Optional, Tuple

from openai import OpenAI

LLM_RESULTS_PATH = "/home/wuyankai/myResearch/codeComplex/results/LLM/ast_llm_results1.json"
FIT_RESULTS_ROOT = "/home/wuyankai/myResearch/codeComplex/demo/filteredData/python"
DATA_ROOT = "/home/wuyankai/myResearch/codeComplex/data/filteredData/python"
ONLY_CODE_ROOT = "/home/wuyankai/myResearch/codeComplex/data/onlyCode/python"

OUTPUT_JSON = "/home/wuyankai/myResearch/codeComplex/results/fusion_llm_report.json"
OUTPUT_TXT = "/home/wuyankai/myResearch/codeComplex/results/fusion_llm_report.txt"

DEFAULT_API_KEY = "sk-3sNQAO5ydpVp29WWoCqvM7Ajqzd1I5WKOpe29cpoT3DoMrZe"
DEFAULT_BASE_URL = "https://yunwu.ai/v1"

EXCLUDED_TYPES = {"constant", "np"}

MODEL_NAME_TO_LABEL = {
    "Constant": "constant",
    "Logarithmic": "logn",
    "Linear": "linear",
    "N Log N": "nlogn",
    "Quadratic": "quadratic",
    "Cubic": "cubic",
}

EQUIVALENCE = {
    "constant": {"constant", "o(1)", "1"},
    "linear": {"linear", "o(n)", "n"},
    "logn": {"logn", "log n", "o(log n)", "o(logn)"},
    "nlogn": {"nlogn", "n log n", "o(n log n)", "o(n logn)"},
    "quadratic": {"quadratic", "o(n^2)", "n^2"},
    "cubic": {"cubic", "o(n^3)", "n^3"},
    "np": {"np", "o(n^p)", "n^p", "exponential", "o(2^n)", "2^n"},
}

DEFAULT_CANDIDATES = ["logn", "linear", "nlogn", "quadratic", "cubic"]

CONFIDENCE_THRESHOLD = 0.5
DELTA_LLM_THRESHOLD = 0.05
DELTA_FIT_THRESHOLD = 0.05
MIN_VALID_POINTS = 5


def normalize_label(raw: Optional[str]) -> Optional[str]:
    if not raw:
        return None
    text = raw.strip().lower()
    text_compact = re.sub(r"\s+", "", text)

    for key, variants in EQUIVALENCE.items():
        for v in variants:
            if v in text or v in text_compact:
                return key
    return None


def compare_complexity(actual: Optional[str], expected: str) -> bool:
    if not actual:
        return False
    expected = expected.strip().lower()
    if expected in EQUIVALENCE:
        return actual in EQUIVALENCE[expected] or actual == expected
    return actual == expected


def load_llm_records(path: str) -> List[Dict]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("detailed_records", [])


def resolve_code_path(complexity_id: str) -> Optional[str]:
    parts = complexity_id.split("_", 2)
    if len(parts) < 3:
        return None
    complexity_type = parts[1]
    filename = f"{complexity_id}.py"
    primary = os.path.join(DATA_ROOT, complexity_type, filename)
    if os.path.exists(primary):
        return primary
    fallback = os.path.join(ONLY_CODE_ROOT, complexity_type, filename)
    if os.path.exists(fallback):
        return fallback
    return None


def load_fit_report(complexity_id: str) -> Tuple[Optional[Dict], Optional[str]]:
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
    if not report:
        return {}
    
    conf_scores = {}
    models = report.get("models", {})
    
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
    if not report:
        return 0
    return report.get("valid_points", 0)


def llm_recheck(code: str) -> Tuple[Optional[str], Optional[str]]:
    api_key = os.getenv("OPENAI_API_KEY", DEFAULT_API_KEY)
    base_url = os.getenv("OPENAI_BASE_URL", DEFAULT_BASE_URL)
    client = OpenAI(api_key=api_key, base_url=base_url)
    
    system_prompt = """你是一位算法分析专家，精通时间复杂度分析。
    你的任务是：
    1. 分析给定代码的时间复杂度
    2. 仅返回复杂度的标准术语，如：constant、linear、logn、nlogn、quadratic、cubic、exponential。
    3. 不要输出任何解释或额外信息，只输出复杂度术语本身"""
    
    user_prompt = f"""请分析以下代码的时间复杂度，并仅返回标准的复杂度术语：
    ```
    {code}
    ```
    
    请严格按照要求，只输出复杂度术语，不要添加任何其他内容！"""
    
    try:
        response = client.chat.completions.create(
            model="gpt-5.1",
            temperature=0.0,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            stream=False
        )
        
        raw_output = response.choices[0].message.content.strip()
        normalized = normalize_label(raw_output)
        return raw_output, normalized
    except Exception as e:
        return None, None


def main() -> None:
    records = load_llm_records(LLM_RESULTS_PATH)

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

    detailed = []

    for idx, record in enumerate(records, 1):
        complexity_id = record.get("complexity_id")
        expected = (record.get("expected_complexity") or "").strip().lower()

        if idx == 1 or idx % 100 == 0:
            print(f"[进度] {idx}/{len(records)} 已处理: {summary['processed']} 跳过: {summary['skipped']} 复查: {summary['rechecked']}")

        if not complexity_id or expected in EXCLUDED_TYPES:
            summary["skipped"] += 1
            continue

        parts = complexity_id.split("_", 2)
        if len(parts) >= 2 and parts[1] in EXCLUDED_TYPES:
            summary["skipped"] += 1
            continue

        llm_raw = record.get("model_raw_output")
        y_llm = normalize_label(llm_raw)

        fit_report, fit_path = load_fit_report(complexity_id)
        conf_scores = get_confidence_scores(fit_report) if fit_report else {}
        valid_points = get_valid_points(fit_report) if fit_report else 0

        if conf_scores:
            y_fit = max(conf_scores, key=conf_scores.get)
            conf_best = conf_scores[y_fit]
            second_best_conf = sorted(conf_scores.values(), reverse=True)[1] if len(conf_scores) > 1 else 0
        else:
            y_fit = None
            conf_best = 0
            second_best_conf = 0

        llm_score = conf_scores.get(y_llm, -float('inf')) if y_llm else -float('inf')
        delta_llm = conf_best - llm_score if y_llm else 0
        delta_fit = conf_best - second_best_conf

        fit_strong = (
            valid_points >= MIN_VALID_POINTS and
            conf_best >= CONFIDENCE_THRESHOLD and
            delta_llm >= DELTA_LLM_THRESHOLD and
            delta_fit >= DELTA_FIT_THRESHOLD
        )

        if fit_strong:
            summary["fit_strong_count"] += 1

        if y_llm == y_fit:
            summary["llm_fit_agree"] += 1
        else:
            summary["llm_fit_disagree"] += 1

        y_final = y_llm
        rechecked = False
        recheck_raw = None
        recheck_norm = None

        if y_llm == y_fit:
            y_final = y_llm
        elif not fit_strong:
            y_final = y_llm
        else:
            code_path = resolve_code_path(complexity_id)
            if code_path:
                try:
                    with open(code_path, "r", encoding="utf-8") as f:
                        code = f.read()
                    recheck_raw, recheck_norm = llm_recheck(code)
                    rechecked = True
                    summary["rechecked"] += 1
                    
                    if recheck_norm == y_fit:
                        y_final = y_fit
                    else:
                        y_final = y_llm
                except Exception as e:
                    y_final = y_llm

        llm_correct = compare_complexity(y_llm, expected)
        fit_correct = compare_complexity(y_fit, expected) if y_fit else False
        fusion_correct = compare_complexity(y_final, expected)

        summary["processed"] += 1
        if llm_correct:
            summary["llm_correct"] += 1
        if fit_correct:
            summary["fit_correct"] += 1
        if fusion_correct:
            summary["fusion_correct"] += 1

        detailed.append(
            {
                "complexity_id": complexity_id,
                "expected_complexity": expected,
                "y_llm": y_llm,
                "y_fit": y_fit,
                "y_final": y_final,
                "conf_scores": conf_scores,
                "valid_points": valid_points,
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

    report = {
        "summary": summary,
        "input_file": LLM_RESULTS_PATH,
        "fit_results_root": FIT_RESULTS_ROOT,
        "output_json": OUTPUT_JSON,
        "output_txt": OUTPUT_TXT,
        "detailed_records": detailed,
    }

    os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

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

    print(f"\nReport saved: {OUTPUT_JSON}")
    print(f"Text summary saved: {OUTPUT_TXT}")
    print(f"\nSummary:")
    print(f"LLM-only accuracy: {summary['llm_correct']}/{summary['processed']} ({summary['llm_correct']/summary['processed']*100:.2f}%)")
    print(f"Fit-only accuracy: {summary['fit_correct']}/{summary['processed']} ({summary['fit_correct']/summary['processed']*100:.2f}%)")
    print(f"Fusion accuracy: {summary['fusion_correct']}/{summary['processed']} ({summary['fusion_correct']/summary['processed']*100:.2f}%)")


if __name__ == "__main__":
    main()
