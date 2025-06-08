# Flask Orders Report App

這是一個簡單的 Flask 專案，具備以下功能：

- 訂單列表查詢（支援條件篩選與排序）
- 匯出報表為 CSV / Excel 格式
- 儀表板頁面顯示統計摘要（總筆數、總金額、平均金額、熱門商品）

---

## 🔧 使用說明

### 1. 安裝套件
請先建立虛擬環境並安裝相依套件：

```bash
python -m venv .venv
source .venv/bin/activate    # Windows 請改用 .venv\Scripts\activate
pip install -r requirements.txt
```

---

### 2. 執行伺服器

```bash
python app.py
```

預設會在 [http://127.0.0.1:5000](http://127.0.0.1:5000) 開啟

---

### 3. 專案結構說明

```
GPT_Day19/
│
├── app.py               # 主入口，啟動 Flask App
├── models.py            # 資料模型（Order / Product / Customer）
├── utils.py             # 工具函式（檔名生成、統計計算）
├── seed.py              # 假資料產生器（可選）
│
├── routes/              # 各個功能的路由模組
│   ├── __init__.py
│   ├── orders.py
│   ├── export.py
│   └── dashboard.py
│
├── templates/           # HTML 模板
│   ├── orders.html
│   └── dashboard.html
│
├── requirements.txt     # 相依套件清單
└── README.md            # 專案說明文件
```

---

## 📌 功能頁面

- `/orders`：查詢訂單（可依顧客名稱、日期範圍、金額排序）
- `/export_csv`：匯出目前查詢結果為 CSV
- `/export_excel`：匯出目前查詢結果為 Excel
- `/dashboard`：統計分析頁面（總金額、平均金額、最熱門商品）

---

## 🧪 測試資料
如需快速建立測試資料，可執行 `seed.py`

---

