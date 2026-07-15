# GitHub Pages 部署

## 目標範圍

部署前確認來源 HTML、目標 repo、分支、Pages 路徑、公開檔名與是否需要首頁入口。使用者指定值優先；未指定時使用 `prayer168/docs`、`main`、分支根目錄，且不修改首頁。

## 存取檢查

1. 執行 `gh --version` 與 `gh auth status`。
2. 執行 `gh repo view owner/repo --json nameWithOwner,defaultBranchRef,url,homepageUrl`。
3. 執行 `gh api repos/owner/repo/pages`，確認 Pages 已啟用且來源正確。
4. 使用者明確要求上線而 Pages 尚未啟用時，才依指定分支與路徑啟用。

## 安全 checkout

- 已位於正確 repo 且工作樹乾淨或變更完全可理解時，才能直接操作。
- 工作樹混有其他變更、目前 repo 不符或本機落後難以安全同步時，使用唯一命名的乾淨暫存 clone。
- 複製 HTML 到 Pages 來源路徑後，執行 `git diff --check` 並確認 `<title>`、預期正文、來源連結與無按鈕要求。

## 提交與推送

1. 先 fetch 遠端分支。
2. 使用明確路徑只 stage 本次 HTML；不得 stage TXT、其他文章或使用者既有變更。
3. 檢查 `git diff --cached --check`、`git diff --cached --name-only` 與 `git status --short`。
4. 使用簡短、描述文章內容的 commit message。
5. 推送指定分支。若遠端前進，安全 rebase、重新檢查差異再推送；不得強制推送。

## 線上驗證

1. 找出該 commit 觸發的 Pages workflow，等待成功完成。
2. 以含 commit 或時間戳查詢參數的公開 URL 發出實際 HTTP 請求，降低快取誤判。
3. 同時確認 HTTP 200、預期 `<title>` 與至少一段正文識別文字。
4. 只有三項都通過才回報部署成功。

## 失敗處理

登入、權限、repo 不存在、分支保護、衝突、workflow 失敗或頁面驗證錯誤時停止宣稱完成。保留已驗證的本機 TXT 與 HTML，說明卡在哪一步以及使用者需採取的最小動作。
