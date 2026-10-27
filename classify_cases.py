#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
案件自動分類工具 (laya-burger)
================================
把 1022 的案件 CSV (標題,客戶,來源,詢問內容,狀態) 透過 laya-burger 自動分類：
  - 案件類型 (choice)：報價議價 / 交期出貨 / 品質客訴 / 認證文件 / 樣品展示 / OEM合約 / 其他
  - 急迫性 (noul)：是否需要在短期內處理
  - 情緒 / 衝突程度 (score)：0-3

用法:
    pip install laya
    python classify_cases.py --csv "路徑/案件.csv"
    python classify_cases.py --csv "路徑/案件.csv" --out "分類結果.csv" --limit 5

若 Agent("xamjiang/laya-burger") 讀不到,請先將模型下載到本機資料夾,
再把底下 AGENT_PATH 改成本機路徑。
"""

import argparse
import csv
import sys

# 改用本機路徑載入的話,把這裡改成資料夾路徑;否則留 None 用 Hub id
AGENT_PATH = None  # 例: r"C:\Users\Eason HS\Downloads\laya-burger"
HUB_ID = "xamjiang/laya-burger"

# 對應你 1022 案件型態的分類條件 (choice)
CATEGORIES = {
    "quote":      "報價、議價、訂單金額或折扣",
    "delivery":   "交期、出貨、庫存或到貨時間",
    "quality":    "品質問題、客訴、測試或維修",
    "cert":       "認證文件、NSF、UPC、CE、WRAS、保固文件",
    "sample":     "樣品、展示機、樣品測試進度",
    "oem":       "OEM、合約、不良率條款、品牌貼牌",
    "other":      "其他",
}

SCORE_LEVELS = ["平靜", "有點困擾", "明顯不滿", "非常生氣"]


def build_questions():
    return {
        "category": {
            "type": "choice",
            "instructions": "這則案件屬於哪一類？",
            "criteria": CATEGORIES,
        },
        "urgent": {
            "type": "noul",
            "instructions": "這則案件需要近期儘快處理嗎？",
        },
        "conflict": {
            "type": "score",
            "instructions": "這則案件的緊張或衝突程度？",
            "criteria": SCORE_LEVELS,
        },
    }


def main():
    ap = argparse.ArgumentParser(description="1022 案件自動分類 (laya-burger)")
    ap.add_argument("--csv", required=True, help="案件 CSV 路徑")
    ap.add_argument("--out", default="分類結果.csv", help="輸出 CSV 路徑")
    ap.add_argument("--limit", type=int, default=0, help="只處理前 N 筆 (0=全部)")
    args = ap.parse_args()

    # 讀入案件 CSV
    with open(args.csv, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        print("CSV 為空或欄位無法解析")
        return

    # 載入模型
    print("載入 laya-burger ...")
    import laya
    agent = laya.Agent(AGENT_PATH or HUB_ID)
    questions = build_questions()

    records = rows[: args.limit] if args.limit else rows
    out_rows = []
    for i, row in enumerate(records, 1):
        # 組 state: 以 詢問內容 為主, 輔以 標題 / 客戶
        text = " / ".join(
            str(row.get(k, "")).strip()
            for k in ("標題", "客戶", "詢問內容")
            if str(row.get(k, "")).strip()
        )
        if not text:
            text = "(無內容)"
        state = {"message": text}

        try:
            out = agent.system_one(state, questions)
            a = out["answers"]
            cat = a["category"]["choice"]
            cat_prob = a["category"]["probabilities"]
            urgent = a["urgent"]["noul"]          # P(true) 0~1
            conflict = a["conflict"]["score"]     # 0~3
            conflict_prob = a["conflict"]["probabilities"]
        except Exception as e:
            print(f"[{i}] 分類失敗: {e}", file=sys.stderr)
            cat, cat_prob, urgent, conflict, conflict_prob = "", {}, 0.0, 0, []

        label = CATEGORIES.get(cat, "未知")
        out_rows.append({
            "標題": row.get("標題", ""),
            "客戶": row.get("客戶", ""),
            "來源": row.get("來源", ""),
            "詢問內容": row.get("詢問內容", ""),
            "狀態": row.get("狀態", ""),
            "案件類型": label,
            "類型機率": round(cat_prob.get(cat, 0.0), 3) if cat_prob else "",
            "需近期處理P": round(urgent, 3),
            "衝突程度0-3": conflict,
            "衝突機率": round(max(conflict_prob) if conflict_prob else 0.0, 3),
        })
        print(f"[{i}/{len(records)}] {row.get('標題', '')[:24]:<26} -> {label} (急{round(urgent,2)})")

    # 寫出結果
    with open(args.out, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)

    print(f"\n完成! 共 {len(out_rows)} 筆,結果已寫入: {args.out}")


if __name__ == "__main__":
    main()
