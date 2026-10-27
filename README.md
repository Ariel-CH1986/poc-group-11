# poc-group-11

水五金外貿英文書信工具與相關資源。

## 內容

| 檔案 | 說明 |
| --- | --- |
| `ai_studio_code.html` | **AquaFlow BizMail** — 國際水五金外貿英文書信專家（純前端 Web 工具）。輸入中文草稿，設定收件人關係與期待語氣，生成主旨建議、英文正文、商務風險提醒與閱讀體感。 |
| `ai_studio_flowchart.html` | AquaFlow BizMail 系統流程圖（diagram-design 編輯式 SVG）。 |
| `classify_cases.py` | 案件自動分類工具（laya-burger）：讀取案件 CSV，自動分類案件類型、急迫性與衝突程度。 |
| `demo_laya_burger.py` | laya-burger 最小範例腳本。 |

## 使用方式

### AquaFlow BizMail
直接用瀏覽器開啟 `ai_studio_code.html` 即可。可選擇貼入中文草稿、載入產業範例，或在「AI API 設定」填入 OpenAI 相容 API Key 以啟用真實 LLM；未填則使用內建離線範本。

### 案件分類（需要 Python + laya）
```bash
pip install laya
python classify_cases.py --csv "路徑/案件.csv"
```

## 授權與注意事項
- AquaFlow BizMail 為獨立開發工具。
- `demo_laya_burger.py` / `classify_cases.py` 使用 [laya-burger](https://huggingface.co/xamjiang/laya-burger)（Laya 決策模型之台灣繁中微調版），其授權為 TAIDE（Gemma 版次）複合式授權，使用時請遵守其限制。
