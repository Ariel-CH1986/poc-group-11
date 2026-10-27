# poc-group-11

水五金外貿英文書信工具與相關資源。

## 🚀 線上使用連結（GitHub Pages）

| 內容 | 網址 |
| --- | --- |
| 簡報（首頁，自動跳轉） | https://ariel-ch1986.github.io/poc-group-11/ |
| **AquaFlow BizMail 小工具** | https://ariel-ch1986.github.io/poc-group-11/ai_studio_code.html |
| 系統流程圖 | https://ariel-ch1986.github.io/poc-group-11/ai_studio_flowchart.html |

## 內容

| 檔案 | 說明 |
| --- | --- |
| `ai_studio_code.html` | **AquaFlow BizMail** — 國際水五金外貿英文書信專家（純前端 Web 工具）。輸入中文草稿，設定收件人關係與期待語氣，生成主旨建議、英文正文、商務風險提醒與閱讀體感。 |
| `ai_studio_flowchart.html` | AquaFlow BizMail 系統流程圖（diagram-design 編輯式 SVG）。 |
| `classify_cases.py` | 案件自動分類工具（laya-burger）：讀取案件 CSV，自動分類案件類型、急迫性與衝突程度。 |
| `demo_laya_burger.py` | laya-burger 最小範例腳本。 |

## 使用方式

### AquaFlow BizMail
直接用瀏覽器開啟 `ai_studio_code.html` 即可。可選擇貼入中文草稿、載入產業範例，或在「AI API 設定」填入 OpenAI 相容 API Key 以啟用真實 LLM；未填則使用**內建離線範本**（已支援多情境自動分派：銅價調漲、交期延誤、議價、客訴、認證、樣品追蹤、OEM、一般詢問，並會擷取 PO / 型號 / 數量等細節帶入信內）。

### 案件分類（需要 Python + laya）
```bash
pip install laya
python classify_cases.py --csv "路徑/案件.csv"
```

## 授權與注意事項
- AquaFlow BizMail 為獨立開發工具。
- `demo_laya_burger.py` / `classify_cases.py` 使用 [laya-burger](https://huggingface.co/xamjiang/laya-burger)（Laya 決策模型之台灣繁中微調版），其授權為 TAIDE（Gemma 版次）複合式授權，使用時請遵守其限制。

## ❓ FAQ：API Key 是什麼？

**API Key（API 金鑰）** 是一個「通行密碼」，用來證明你是某個 AI 服務的合法使用者，並讓該服務幫你生成內容。AquaFlow BizMail 有兩種模式：

| 模式 | 條件 | 品質 |
| --- | --- | --- |
| 離線範本 | 不填任何內容 | 固定範本，僅幾種情境 |
| 真實 AI 翻譯 | 填入 API Key | 真正「讀懂」中文並精準翻譯 |

### 怎麼申請？
| 服務 | 網址 | Model | Endpoint |
| --- | --- | --- | --- |
| OpenAI (GPT) | https://platform.openai.com | `gpt-4o` | `https://api.openai.com/v1/chat/completions` |
| DeepSeek | https://platform.deepseek.com | `deepseek-chat` | `https://api.deepseek.com/v1/chat/completions` |

申請流程：註冊 → 建立 API Key（格式如 `sk-...`）→ 通常需少量預儲金額（「用多少付多少」，少量書信成本極低）。

### 在工具中怎麼填？
工具右上角「AI API 設定」→ 填入 Endpoint / API Key / Model 即可。未填則使用內建離線範本（已支援多情境自動分派，並依「語氣/收件人關係」調整措辭）。
