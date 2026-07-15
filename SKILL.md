---
name: ai-science-inquiry-writer
description: Research, write, validate, and publish source-backed Traditional Chinese AI-and-science inquiry articles. Use for 2,000–3,000-character educator-facing articles, teaching features, inquiry stories, science-fair narratives, biodiversity or experiment writing that should begin with lively everyday life, introduce AI gradually, preserve scientific evidence and human responsibility, produce matching UTF-8 TXT and standalone HTML, deploy the HTML to GitHub Pages, and return a verified public URL.
---

# AI 科學探究文章：從生活敘事到 GitHub Pages

將 AI 定位為觀察、整理、分析與提出候選解釋的助手；讓學生負責現場資料、查證、推理、限制與科學結論。預設使用臺灣繁體中文與臺灣教育情境。

## 必讀參考

開始撰寫前完整讀取：

- [生活敘事風格](references/narrative-style.md)：控制開場、節奏、文氣、AI 登場時機與結尾餘韻。
- [編輯與查證標準](references/editorial-standard.md)：控制來源品質、科學論證與禁止模式。

開始部署前完整讀取 [GitHub Pages 部署](references/github-deployment.md)。

## 1. 確認任務

擷取主題、讀者、篇幅、語氣、科學概念、AI 用途、延伸情境與指定輸出位置。使用者規格足夠時直接執行，不重複提問。

未指定時採用：

- 2,000–3,000 個中文字，不含資料來源。
- 適合國小高年級至國中教師公開閱讀。
- 溫暖、生活化、帶畫面與輕巧幽默，不寫成論文或教案清單。
- 固定產生 TXT、HTML、GitHub Pages 公開頁面與 Codex 一鍵複製全文。

## 2. 研究與查證

涉及現行工具、政策、研究、資料庫或具體數據時先搜尋。使用 5–10 筆直接相關來源，依序優先：

1. 臺灣中央與地方政府、國家教育研究院及官方資料庫。
2. 博物館、植物園、大學、研究機構與同行評審文獻。
3. 國際組織與工具官方文件。
4. 新聞或部落格只作補充。

核對每筆來源的標題、作者或發布單位、日期與實際網址。找不到指定來源時改用可驗證替代來源並說明，不得虛構。

## 3. 建立探究故事線

先形成一句核心主張：AI 提供候選答案或資料整理，學生以觀察、查證、比較與解釋形成暫時性科學結論。

再把主題轉成一條自然敘事線：

1. 從便當、飲水、書包、運動、天氣、校園角落或家庭小插曲等真實生活現象開場。
2. 讓人物先猜測、爭論或動手嘗試；不要讓 AI 在第一段搶答。
3. 讓第一次嘗試出現可理解的小混亂，從錯誤中長出研究問題。
4. 在學生真的需要整理、比較或找反例時，讓 AI 自然登場。
5. 將 AI 輸出視為候選解釋；安排一次過度肯定、忽略情境或概念混淆，轉化為查證契機。
6. 描寫學生重新拍攝、補測、控制變因、查來源、保留異常值或修正假設。
7. 收束於有範圍與限制的暫時性結論，並留下下一輪尚未完成的小問題。

依主題調整，不必機械套用所有節點。

## 4. 撰寫全文

保持文氣一氣呵成。以一個反覆出現的物件、聲音、疑問或版本號串起全文；用完整段落與少量有意義的小標題推進，不把正文拆成密集條列。

寫入 2–4 個能推動證據思考的教師提問。穿插具體動作、對話與感官細節，但不虛構研究數據。理論與政策只在能解釋故事時短暫出現，先用白話說清楚，再補名稱；避免連續堆疊學者、框架與機構。

明確區分責任：

- AI 可整理資料、產生候選辨識、繪圖、提示缺漏、比較版本、提出反方問題與後續問題。
- 學生負責現場觀察、拍照或測量、原始資料、來源查證、合理性判斷、原因解釋、限制與下一步。
- 教師示範與搭鷹架，再逐步把決定權移交給學生。

不得暗示 AI 能證明因果、取代專家鑑定、代替實驗或為科學結論負責。不要把同時發生或統計相關寫成單一因果。

## 5. 編輯檢查

逐項確認：

- 開頭先有生活事件，AI 稍後才因需求出現。
- 故事中的錯誤確實引發補測、查證或改版，不只被當作笑點。
- 正文有科學問題、證據來源、比較與推理，不只是工具介紹。
- 全文口吻自然、段落銜接順暢，刪除「首先、其次、綜上所述」式報告腔。
- 結尾呼應開場意象，留下餘韻或下一步，不喊口號、不重複摘要。
- 具體事實與來源相符，文末列出 5–10 筆來源及查閱日期。
- 涉及有毒植物、野外採集、過敏、動物干擾或實驗風險時加入適齡安全提醒。

## 6. 產生 TXT 與 HTML

預設輸出資料夾：

`D:\我的雲端硬碟\google drive\000000000backup\0000000000數位教材\docs`

只有使用者明確指定其他資料夾時才更改。先解析並確認絕對路徑；無法建立或寫入時不得靜默改存其他位置。

使用 3–8 個英文關鍵字建立小寫 ASCII kebab-case 主檔名，只使用 `a-z`、`0-9` 與連字號。若同名檔案已存在且不是本次產物，加入 `-YYYYMMDD-HHmmss`，不得覆寫使用者檔案。

建立相同主檔名的：

- `.txt`：UTF-8 純文字，包含標題、正文、完整來源與查閱日期；不得含 Markdown 或 HTML。
- `.html`：與 TXT 內容一致的單檔文章；使用 `lang="zh-Hant"`、UTF-8、viewport、語意化標籤、內嵌 CSS、RWD 與列印樣式。

HTML 不得依賴外部 CDN，不得顯示複製、列印、下載或其他工具列與按鈕。外部來源連結使用 `target="_blank" rel="noopener noreferrer"`。

## 7. 驗證輸出

執行：

```bash
python scripts/validate_article_outputs.py --txt <absolute-txt-path> --html <absolute-html-path>
```

腳本必須通過。另以實際 UTF-8 讀取確認標題、結尾、來源與檔名，必要時在窄螢幕檢查排版。修正所有錯誤後才部署。

## 8. 部署到 GitHub Pages

完成檔案驗證後立即部署，不另行詢問第二次確認。使用者指定 repo、分支或 Pages 路徑時依指定；否則使用：

- Repo：`prayer168/docs`
- Branch：`main`
- Pages source：分支根目錄
- Public URL：`https://prayer168.github.io/docs/{slug}.html`

只部署本次 HTML，不提交 TXT 或無關變更。若目前工作樹混有其他內容，使用乾淨暫存 checkout。提交前 fetch、檢查 diff、只 stage 指定 HTML；推送後等待 Pages workflow，實際請求公開網址。只有 HTTP 200 且頁面含預期標題與正文識別文字時才算成功。

登入、權限、分支保護、衝突或 Pages 失敗時，保留本機成品並明確回報；不得宣稱已部署。

## 9. 最終交付

依序提供：

1. 簡短完成說明。
2. 標示「GitHub Pages 網頁」的公開連結，註明已線上驗證。
3. 「下載純文字檔」與「下載網頁檔」的本機絕對路徑連結。
4. 「一鍵複製純文字」標示。
5. 一個 `text` 或 `plaintext` fenced code block，逐字放入完整 TXT 內容。

程式碼區塊只能放 TXT 全文，不得省略、截斷或加入檔名與註解；交付前逐字比較程式碼區塊與 TXT。
