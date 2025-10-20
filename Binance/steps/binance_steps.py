from behave import given, when, then
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@given("iOS设备已连接且Appium服务已启动")
def step_impl(context):
    assert context.appium_service.is_running, "❌ Appium服务未运行"
    assert context.driver is not None, "❌ WebDriver会话未创建"
    print("✅ 设备和服务状态正常")

@when("点击设置-Aplha活动-空投")
def step_impl(context):
    try:
        wait = WebDriverWait(context.driver, 0.2)
        settings_button = wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH, 
                "//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton"
            ))
        )
        settings_button.click()
        print("✅ 点击了设置按钮")

        alpha_activities_button = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Alpha活动")))
        alpha_activities_button.click()
        print("✅ 点击了Aplha活动按钮")

        airdrop_button = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "空投")))
        airdrop_button.click()
        print("✅ 点击了空投按钮")
    except TimeoutException:
        print("❌ 未能找到某个元素，操作失败")
        raise

@then("等待10秒后退出")
def step_impl(context):
    time.sleep(20)
    print("✅ 测试完成，准备退出")
