# 🤖 AGENTS.md — 個人財金知識庫 AI 執行規範手冊

## 1. 專案目標與核心定位 (Project Mission)
本專案為一個自動化運作的**個人財金知識庫 (Personal Financial Knowledge Base)**。
核心宗旨是讓 AI Agent 自動讀取每日/週輸入的原始財經資料，並自動整理、歸納、提煉成視覺化網頁報告，最後即時更新至首頁網站。

### 追蹤主題標籤 (Taxonomy)
- `#泰鼎KY` (4927)：營收動態、泰國工廠擴產進度、PCB 產業趨勢、產能利用率。
- `#每日總經`：游庭皓的財經皓角（每日更新總體經濟、央行利率、美股與台股走勢）。
- `#心法`：股癌 Gooaye（每週三、六更新市場觀察、個股心法與投資心態）。
- `#PODCAST`：包含所有 Podcast 節目之摘要與重點時間軸。

---

## 2. 專案目錄結構 (Folder Structure)
AI 必須嚴格遵守以下目錄結構與命名規範：

```text
my-financial-wiki/
├── AGENTS.md               # [靈魂] AI 規範手冊與開發守則
├── index.html              # [核心] 知識庫首頁 (包含泰鼎儀表板 + 今日推播 + 標籤篩選)
├── raw_data/               # 存放輸入的原始文字 (Podcast 逐字稿 / 新聞報導 / 財報)
│   └── YYYY-MM-DD-raw.txt
├── reports/                # AI 自動生成的 HTML 每日報告
│   └── YYYY-MM-DD-report.html
└── assets/                 # 靜態資源 (CSS 樣式、圖示、圖片)
    └── style.css