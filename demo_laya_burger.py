#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""laya-burger 最小範例：安裝、載入、問三個問題並印出機率。"""

import laya

agent = laya.Agent("xamjiang/laya-burger")   # 讀不到時改成本機資料夾路徑

state = {"message": "你好，我上週在網路上訂的冷氣到現在還沒送來，客服電話一直打不通，再不處理我要退貨了。"}

questions = {
    "category": {"type": "choice", "instructions": "這則訊息屬於哪一類？",
                 "criteria": {"shipping": "出貨或配送問題", "billing": "付款或發票問題",
                              "product": "商品本身的問題", "other": "其他"}},
    "urgent": {"type": "noul", "instructions": "這件事需要今天處理嗎？"},
    "upset": {"type": "score", "instructions": "寄件人有多不滿？",
              "criteria": ["平靜", "有點困擾", "明顯不滿", "非常生氣"]},
}

out = agent.system_one(state, questions)
a = out["answers"]
print("category:", a["category"]["choice"], a["category"]["probabilities"])
print("urgent P(true):", a["urgent"]["noul"])
print("upset (level 0-3):", a["upset"]["score"], a["upset"]["probabilities"])
