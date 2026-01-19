#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Compute CodeComplex-style evaluation metrics:
- Accuracy
- Macro-F1
- HC-Score (Hierarchy Complexity Score)
- Windowed HC-Score: HCw with w=2 (HC2) and w=3 (HC3) by default

Expected JSON format: list[dict]
Required columns (default):
  - expected_complexity : ground truth label
  - y_llm, y_fit, y_final : predictions (can be None/missing)

Default hierarchy order (7 classes):
  constant -> logn -> linear -> nlogn -> quadratic -> cubic -> exponential

Usage:
  python3 compute_codecomplex_metrics.py \
    --input fusion_llm_summary_v14.json \
    --outdir metrics_codecomplex \
    --ytrue expected_complexity \
    --pred-cols y_llm y_fit y_final \
    --windows 2 3

Outputs:
  metrics_codecomplex/summary.json
  metrics_codecomplex/summary.csv
"""

import argparse
import json
import os
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score


DEFAULT_HIERARCHY = [
    "constant", "logn", "linear", "nlogn", "quadratic", "cubic", "exponential"
]


def load_json_as_df(path: str) -> pd.DataFrame:
    with open(path, "r", encoding="utf-8") as f:
        obj = json.load(f)
    if not isinstance(obj, list):
        raise ValueError("Input JSON must be a list of records (list[dict]).")
    return pd.DataFrame(obj)


def normalize_label(x) -> str:
    """Map None/NaN/empty to 'missing'. Keep strings as-is."""
    if x is None:
        return "missing"
    if isinstance(x, float) and np.isnan(x):
        return "missing"
    if isinstance(x, str) and x.strip() == "":
        return "missing"
    return x


def hc_score(
    y_true: List[str],
    y_pred: List[str],
    hierarchy: List[str],
    w: Optional[int] = None,
) -> float:
    """
    HC-Score from the paper:
      HC = (1/N) * sum_i ( 1 - |p_i - r_i| / Number_of_class )

    Windowed HCw from the paper:
      HCw = (1/N) * sum_i max(0, 1 - |p_i - r_i| / w)

    Notes:
    - We treat predictions outside the hierarchy (including 'missing') as score 0 for that sample.
    - Ground-truth labels should be within hierarchy; if not, those samples are skipped.
    """
    pos: Dict[str, int] = {c: i for i, c in enumerate(hierarchy)}
    C = len(hierarchy)

    scores = []
    for t, p in zip(y_true, y_pred):
        if t not in pos:
            # skip weird ground truth
            continue
        if p not in pos:
            scores.append(0.0)
            continue

        d = abs(pos[p] - pos[t])
        if w is None:
            scores.append(1.0 - d / C)
        else:
            scores.append(max(0.0, 1.0 - d / float(w)))

    if not scores:
        return float("nan")
    return float(np.mean(scores))


def compute_one(
    df: pd.DataFrame,
    ytrue_col: str,
    ypred_col: str,
    hierarchy: List[str],
    windows: List[int],
) -> Dict[str, float]:
    y_true = df[ytrue_col].astype(str).tolist()
    y_pred = df[ypred_col].tolist()

    # Accuracy / Macro-F1:
    # For fair comparison, only evaluate on samples whose pred is in hierarchy;
    # missing/outside are treated as wrong.
    # (This matches typical "classification with abstains" handling.)
    y_pred_norm = [normalize_label(x) for x in y_pred]

    # Any label not in hierarchy becomes 'other' (still wrong for acc/f1)
    y_pred_acc = [p if p in hierarchy else "other" for p in y_pred_norm]
    y_true_acc = [t if t in hierarchy else "other" for t in y_true]

    acc = float(accuracy_score(y_true_acc, y_pred_acc))

    # Macro-F1 over hierarchy labels only (ignore 'other' in averaging)
    macro_f1 = float(
        f1_score(
            y_true_acc,
            y_pred_acc,
            labels=hierarchy,
            average="macro",
            zero_division=0,
        )
    )

    out = {
        "accuracy": acc,
        "macro_f1": macro_f1,
        "HC": hc_score(y_true, y_pred_norm, hierarchy, w=None),
    }
    for w in windows:
        out[f"HC{w}"] = hc_score(y_true, y_pred_norm, hierarchy, w=w)

    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default="./results/fusion_llm_summary_v14.json", help="Path to input JSON (list[dict]).")
    ap.add_argument("--outdir", default="metrics_codecomplex", help="Output directory.")
    ap.add_argument("--ytrue", default="expected_complexity", help="Ground-truth column.")
    ap.add_argument(
        "--pred-cols",
        nargs="+",
        default=["y_llm", "y_fit", "y_final"],
        help="Prediction columns to evaluate.",
    )
    ap.add_argument(
        "--hierarchy",
        nargs="+",
        default=DEFAULT_HIERARCHY,
        help="Ordered class hierarchy for HC distance.",
    )
    ap.add_argument(
        "--windows",
        nargs="*",
        type=int,
        default=[2, 3],
        help="Window sizes for HCw (e.g., 2 3 => HC2 HC3).",
    )
    args = ap.parse_args()

    os.makedirs(args.outdir, exist_ok=True)

    df = load_json_as_df(args.input)

    missing_cols = [c for c in [args.ytrue] + args.pred_cols if c not in df.columns]
    if missing_cols:
        raise KeyError(f"Missing columns in JSON: {missing_cols}")

    # Normalize prediction columns (keep gt as string)
    for c in args.pred_cols:
        df[c] = df[c].map(normalize_label)

    summary = {
        "input": os.path.abspath(args.input),
        "n_records": int(len(df)),
        "ytrue": args.ytrue,
        "pred_cols": args.pred_cols,
        "hierarchy": args.hierarchy,
        "windows": args.windows,
        "results": {},
    }

    rows = []
    for col in args.pred_cols:
        metrics = compute_one(df, args.ytrue, col, args.hierarchy, args.windows)
        summary["results"][col] = metrics
        rows.append({"pred_col": col, **metrics})

    # Save outputs
    with open(os.path.join(args.outdir, "summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    pd.DataFrame(rows).to_csv(os.path.join(args.outdir, "summary.csv"), index=False)

    # Print a compact view
    print(pd.DataFrame(rows).to_string(index=False))


if __name__ == "__main__":
    main()
