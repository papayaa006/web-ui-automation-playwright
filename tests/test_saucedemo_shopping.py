import pytest
from playwright.sync_api import Page, expect

# ==========================================
# 案例 1：正常購買流程 (E2E Happy Path)
# 登入 -> 加入購物車 -> 結帳 -> 驗證訂單完成
# ==========================================
def test_full_shopping_flow_success(page: Page):
    # 1. 前往測試網站
    page.goto("https://www.saucedemo.com/")

    # 2. 模擬使用者輸入帳號與密碼
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()

    # 斷言：登入後網址是否正確跳轉到商品列表頁
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    
    # 3. 將商品加入購物車
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    
    # 斷言：右上角購物車圖示是否顯示數字 1
    cart_badge = page.locator('[data-test="shopping-cart-badge"]')
    expect(cart_badge).to_have_text("1")

    # 4. 點擊購物車並進入結帳流程
    page.locator('[data-test="shopping-cart-link"]').click()
    page.locator('[data-test="checkout"]').click()

    # 5. 填寫結帳資料
    page.locator('[data-test="firstName"]').fill("Ming")
    page.locator('[data-test="lastName"]').fill("Chen")
    page.locator('[data-test="postalCode"]').fill("100")
    page.locator('[data-test="continue"]').click()

    # 6. 確認訂單總結並點擊完成
    page.locator('[data-test="finish"]').click()

    # 斷言：畫面是否成功出現感謝購買字樣
    complete_header = page.locator('[data-test="complete-header"]')
    expect(complete_header).to_have_text("Thank you for your order!")


# ==========================================
# 案例 2：異常登入攔截 (Negative Test)
# 輸入錯誤密碼時，畫面必須出現對應警告提示
# ==========================================
def test_login_with_invalid_credentials_shows_error(page: Page):
    page.goto("https://www.saucedemo.com/")

    # 輸入錯誤密碼
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("wrong_password")
    page.locator('[data-test="login-button"]').click()

    # 斷言：是否出現特定的錯誤提示訊息
    error_message = page.locator('[data-test="error"]')
    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text("Username and password do not match")


# ==========================================
# 案例 3：故意失敗的測試（用來驗證自動截圖機制）
# ==========================================
def test_intentional_failure_to_verify_screenshot(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()

    # 故意斷言錯誤的文字，觸發失敗截圖
    header = page.locator('[data-test="title"]')
    expect(header).to_have_text("This Header Does Not Exist")