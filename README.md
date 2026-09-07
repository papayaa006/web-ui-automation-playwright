# Web UI End-to-End Automation Test Suite

基於 **Python + Playwright + pytest** 建構的現代化 Web 端到端（E2E）自動化測試專案，以電商網站（SauceDemo）為測試標的，涵蓋核心購物流、異常攔截與測試失敗自動截圖除錯機制。

---

## 📌 專案亮點

- **真實使用者情境驗證**：模擬完整使用者旅程（登入 $\rightarrow$ 瀏覽與加入購物車 $\rightarrow$ 結帳填表 $\rightarrow$ 訂單完成確認）。
- **非同步與自動等待機制**：發揮 Playwright 原生 Auto-waiting 特性，大幅降低因網路延遲造成的 UI 測試誤判（Flaky Tests）。
- **測試失敗自動截圖 (Screenshot on Failure)**：透過 `pytest` 的 hook 機制監聽測試生命週期，一旦斷言失敗即自動留存故障現場之全螢幕截圖。

---

## 🛠 技術堆疊

- **測試語言**：Python 3.10+
- **瀏覽器自動化核心**：Playwright (Chromium)
- **測試執行框架**：pytest, pytest-playwright

---

## 🧪 測試涵蓋案例 (Test Cases)

| 測試案例 | 類型 | 說明 |
| :--- | :--- | :--- |
| `test_full_shopping_flow_success` | E2E 功能測試 | 完整購物結帳流程，驗證各頁面跳轉與結帳成功字樣 |
| `test_login_with_invalid_credentials_shows_error` | 負向測試 (Negative) | 帳密錯誤情境，驗證網頁錯誤提示文字與元件可見度 |
| `test_intentional_failure_to_verify_screenshot` | 容錯與除錯驗證 | 故意觸發斷言失敗，驗證自動捕捉錯誤截圖機制 |

---

## 🚀 快速上手

### 1. 安裝套件與瀏覽器核心

```bash
pip install -r requirements.txt
playwright install