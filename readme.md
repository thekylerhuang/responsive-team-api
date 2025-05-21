# Team API (FastAPI 專案)

這是一個使用 FastAPI 製作的後端 API，提供團隊成員資料，可供前端顯示於網站中。

## 🔧 功能簡介

- 提供一個 GET API：`/api/members`
- 回傳一組成員資訊（name, title, description, email, image）
- 可搭配前端透過 JavaScript 使用 fetch() 呼叫並渲染成員卡片

## 🌐 部署結果

### 🔸 後端 API（FastAPI）

- 目前已部署於 Render：  
  👉 [https://responsive-team-api.onrender.com/api/members](https://responsive-team-api.onrender.com/api/members)

- 提供資料格式範例（JSON）：

```json
[
  {
    "name": "Kevin Samson",
    "title": "Founder",
    "description": "Turning clean code into beautiful experiences.",
    "email": "kevinsamson@gmail.com",
    "image": "/images/team1.jpg"
  },
  ...
]
```
