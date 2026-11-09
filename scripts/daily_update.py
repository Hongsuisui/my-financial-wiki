import os
import datetime
from google import genai

# 1. 取得今日日期與環境變數 API Key
today = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).strftime("%Y-%m-%d")
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise ValueError("未找到 GEMINI_API_KEY 環境變數")

client = genai.Client(api_key=api_key)

# 2. 讀取專案中的 AGENTS.md 規範
with open("AGENTS.md", "r", encoding="utf-8") as f:
    agents_md = f.read()

# 3. 組合 Prompt 提示詞，要求 AI 按照 AGENTS.md 生成今日報告 HTML
prompt = f"""
你是一個嚴格遵循 AGENTS.md 規範的財金 AI Agent。
請參考以下 AGENTS.md 的規範：
{agents_md}

請針對今日 ({today}) 生成一份符合日系雜誌風格的全新 HTML 報告內容，包含今日總經、股癌觀點與泰鼎-KY 最新動態。
請直接輸出完整的 HTML 程式碼，不要包含任何 markdown 標記。
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

report_html = response.text.replace("```html", "").replace("```", "").strip()

# 4. 將生成的 HTML 寫入 reports/YYYY-MM-DD-report.html
os.makedirs("reports", exist_ok=True)
report_filename = f"reports/{today}-report.html"
with open(report_filename, "w", encoding="utf-8") as f:
    f.write(report_html)

print(f"成功生成今日報告：{report_filename}")
