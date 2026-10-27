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
| `ai_studio_code.html` | **AquaFlow BizMail** (v3) — 國際水五金外貿英文書信專家（純前端 Web 工具）。輸入中文草稿，選擇收件人關係、語氣與情境，生成主旨建議、英文正文、商務風險提醒與閱讀體感。 |
| `ai_studio_flowchart.html` | AquaFlow BizMail 系統流程圖（diagram-design 編輯式 SVG）。 |
| `classify_cases.py` | 案件自動分類工具（laya-burger）：讀取案件 CSV，自動分類案件類型、急迫性與衝突程度。 |
| `demo_laya_burger.py` | laya-burger 最小範例腳本。 |

## 使用方式

### AquaFlow BizMail
直接用瀏覽器開啟 `ai_studio_code.html` 即可。可選擇貼入中文草稿、載入產業範例，或在「AI API 設定」填入 OpenAI 相容 API Key 以啟用真實 LLM；未填則使用**內建離線範本**。

**Phase 1 設定（三組獨立選項）：**
- 收件人關係：[A] 國外買家／品牌客戶 · [B] 零件／原料供應商 · [C] 海外代理／經銷商 · [D] 其他特定對象
- 期待語氣：[A] 標準專業禮貌 · [B] 堅定/強硬 · [C] 委婉/軟化 · [D] 簡潔親切（語氣只顯示名稱，情境/語氣解耦）
- 情境：自動判斷（依內容）＋ 8 種手動選擇（樣品追蹤／議價降價／品質客訴／交期出貨／認證索取／OEM 合約／銅價調漲／一般詢問）

**多情境離線範本：** 銅價調漲、交期延誤、議價、客訴、認證、樣品追蹤、OEM、一般詢問，並會擷取 PO / 型號 / 數量等細節帶入信內。語氣會影響正文的**開場、反應態度、請求行動、承諾與收尾**等五個段落措辭，且**每種情境都可套用任一種語氣**。輸出上方會顯示「✅ 已選擇｜收件人 · 語氣 · 情境」確認列。 產出的英文書信會以 **Markdown** 排版呈現（粗體、清單等）。

**上傳佐證：** 中文輸入區下方可上傳圖片／影片佐證。圖片會由 AI（多模態）直接分析並產出佐證；離線模式則列出檔名並提示需填入 API Key。

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
| 離線範本 | 不填任何內容 | 多情境自動分派＋語氣可變，仍屬範本級 |
| 真實 AI 翻譯 | 填入 API Key | 真正「讀懂」中文並精準翻譯 |

### 怎麼申請？
| 服務 | 網址 | Model | Endpoint |
| --- | --- | --- | --- |
| OpenAI (GPT) | https://platform.openai.com | `gpt-4o` | `https://api.openai.com/v1/chat/completions` |
| DeepSeek | https://platform.deepseek.com | `deepseek-chat` | `https://api.deepseek.com/v1/chat/completions` |

申請流程：註冊 → 建立 API Key（格式如 `sk-...`）→ 通常需少量預儲金額（「用多少付多少」，少量書信成本極低）。

### 在工具中怎麼填？
工具右上角「AI API 設定」→ 填入 Endpoint / API Key / Model 即可。未填則使用內建離線範本（已支援多情境自動分派，並依「語氣/收件人關係」調整措辭）。
