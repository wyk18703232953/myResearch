"""
Quick checker: list files whose best-fit model scores R2>=0.98 but
does not match the expected complexity type implied by the folder.
Best model is picked by confidence_score (fallback r2 if missing).
"""
import glob
import json
import os
from typing import Dict, Tuple

import config


TYPE_CONFIG = {
    # "constant": (config.constant_results_base_dir, "Constant"),
    "linear": (config.linear_results_base_dir, "Linear"),
    "logn": (config.logn_results_base_dir, "Logarithmic"),
    # "nlogn": (config.nlogn_results_base_dir, "N Log N"),
    "quadratic": (config.quadratic_results_base_dir, "Quadratic"),
    "cubic": (config.cubic_results_base_dir, "Cubic"),
    # "np": (config.np_results_base_dir, "NP"),  # 模型未覆盖可按需开启
}


def canon(name: str) -> str:
    return name.replace(" ", "").replace("_", "").lower()


def pick_best_model(models: Dict[str, Dict]) -> Tuple[str, float]:
    best_name = ""
    best_score = float("-inf")
    for name, info in models.items():
        score = info.get("confidence_score")
        if score is None:
            score = info.get("r2", float("-inf"))
        if score > best_score:
            best_score = score
            best_name = name
    return best_name, best_score


def main() -> None:
    mismatches = []

    for type_name, (base_dir, expected_model) in TYPE_CONFIG.items():
        if not os.path.isdir(base_dir):
            continue
        pattern = os.path.join(base_dir, "**", "analysis_report.json")
        for report_path in glob.iglob(pattern, recursive=True):
            try:
                with open(report_path, "r", encoding="utf-8") as f:
                    report = json.load(f)
            except Exception:
                continue

            models = report.get("models", {})
            if not models:
                continue

            best_name, _ = pick_best_model(models)
            if not best_name:
                continue

            best_r2 = models.get(best_name, {}).get("r2", float("-inf"))
            if best_r2 < 0.98:
                continue

            if canon(best_name) != canon(expected_model):
                mismatches.append(
                    {
                        "type": type_name,
                        "expected": expected_model,
                        "best": best_name,
                        "r2": best_r2,
                        "report": report_path,
                    }
                )

    print(f"发现 R2>=0.98 且不匹配的文件数: {len(mismatches)}")
    for item in mismatches:
        print(
            f"[{item['type']}] expected={item['expected']} best={item['best']} "
            f"r2=  {item['r2']:.4f} report= {item['report']}"
        )

    print(f"发现 R2>=0.98 且不匹配的文件数: {len(mismatches)}")

if __name__ == "__main__":
    main()
