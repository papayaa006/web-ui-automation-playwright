import os
import pytest

# 當測試函式執行完畢時，pytest 會自動觸發這個 hook
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # 檢查是否是在測試執行階段（call）發生失敗（failed）
    if rep.when == "call" and rep.failed:
        # 從測試參數中取得 playwright 的 page 物件
        page = item.funcargs.get("page")
        if page:
            os.makedirs("screenshots", exist_ok=True)
            # 以測試函式名稱命名截圖檔案
            screenshot_path = os.path.join("screenshots", f"{item.name}_failed.png")
            page.screenshot(path=screenshot_path)
            print(f"\n[已自動擷取錯誤畫面]: {screenshot_path}")