# AI Science Inquiry Writer

一個從研究、繁體中文科學探究文章寫作、TXT／HTML 驗證，到 GitHub Pages 部署的 Codex skill。

## 核心用途

這個 skill 適合撰寫連結 AI 素養與下列主題的公開文章：

- 科學探究與課堂實作
- 科展、變因控制與資料分析
- 校園生態、生物多樣性與環境教育
- AI 輔助觀察、辨識、圖表整理與查證
- 教師專業閱讀與教學行動建議

文章以具體的課堂、校園、實驗或戶外觀察問題為主軸，清楚區分 AI 候選答案、現場資料、外部來源與學生結論。寫作不強制加入生活趣事、幽默或延後 AI 登場；AI 應在科學與教學邏輯需要的位置出現。

除了說明「發生了什麼」，文章還要挑戰一個常見假設，提出替代看法，並從案例證據導出一個可以小規模嘗試的教學改變及其可觀察成效。

## 完整工作流程

1. 確認主題、讀者、篇幅與科學問題。
2. 搜尋並核對 5–10 筆官方、研究或第一手來源。
3. 將 AI 輸出視為假設或候選解釋，以現場資料與可信來源查證。
4. 撰寫預設 2,000–3,000 字的臺灣繁體中文文章。
5. 產生相同英文 slug 的 UTF-8 `.txt` 與單檔 RWD `.html`。
6. 執行驗證腳本，檢查篇幅、來源、雙檔內容、HTML 結構與外部連結安全。
7. 只提交本次 HTML 到 GitHub Pages repo。
8. 等待 Pages workflow，驗證公開網址為 HTTP 200 且包含預期內容。
9. 回傳公開網址、本機雙檔連結與可一鍵複製的完整純文字。

## 安裝

將本 repo 複製到 Codex skills 目錄，資料夾名稱保持為 `ai-science-inquiry-writer`：

```bash
git clone https://github.com/prayer168/ai-science-inquiry-writer-deploy-github.git ai-science-inquiry-writer
```

常見安裝位置：

- Windows：`%USERPROFILE%\.codex\skills\ai-science-inquiry-writer`
- macOS／Linux：`~/.codex/skills/ai-science-inquiry-writer`

## 使用方式

在 Codex 中明確呼叫：

```text
使用 $ai-science-inquiry-writer，撰寫一篇探討 AI 植物辨識如何轉化為校園生態探究與教學行動的文章。
```

預設輸出文章至：

```text
D:\我的雲端硬碟\google drive\000000000backup\0000000000數位教材\docs
```

可在當次提示中指定其他絕對路徑、GitHub repo、分支或 Pages 路徑。

## 必要工具

- Python 3：執行雙檔驗證腳本。
- Git：建立提交與推送文章 HTML。
- GitHub CLI `gh`：確認登入、repo 與 Pages 狀態。
- 已啟用 GitHub Pages 的目標 repo。

預設 Pages 目標為：

- Repo：`prayer168/docs`
- Branch：`main`
- Source：分支根目錄

## 驗證文章輸出

```bash
python scripts/validate_article_outputs.py --txt /absolute/path/article.txt --html /absolute/path/article.html
```

驗證內容包括：

- 相同且有效的英文 kebab-case 檔名
- UTF-8 與 2,000–3,000 字正文
- 5–10 筆來源與查閱日期
- TXT 不含 Markdown 或 HTML
- HTML 語言、charset、viewport、RWD 與列印樣式
- 無外部 CDN、按鈕或不安全的新分頁連結
- HTML 可見正文與 TXT 正文一致

## Repo 結構

```text
ai-science-inquiry-writer/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── editorial-standard.md
│   ├── github-deployment.md
│   └── reader-insight-and-teaching-action.md
└── scripts/
    └── validate_article_outputs.py
```

## 部署安全原則

- 工作樹混有其他變更時使用乾淨暫存 checkout。
- 只 stage 本次文章 HTML，不提交 TXT 或其他使用者檔案。
- 不強制推送；遠端前進時先安全同步並重新檢查差異。
- 只有 Pages workflow 成功、公開頁面為 HTTP 200 且內容吻合時，才回報部署完成。
