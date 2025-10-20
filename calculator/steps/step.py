from behave import given, when, then
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

@given("iOS设备已连接且Appium服务已启动")
def step_impl(context):
    assert context.appium_service.is_running, "❌ Appium服务未运行"
    assert context.driver is not None, "❌ WebDriver会话未创建"
    print("✅ 设备和服务状态正常")

@when("点击1+1=按钮")
def step_impl(context):
    try:
        wait = WebDriverWait(context.driver, 0.2)
        button1 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "One")))
        button1.click()
        print("✅ 点击了1")

        buttonPlus = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Add")))
        buttonPlus.click()
        print("✅ 点击了+")

        button1.click()
        print("✅ 点击了1")

        buttonEqual = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Equals")))
        buttonEqual.click()
        print("✅ 点击了=")
    except TimeoutException:
        print("❌ 未能找到某个元素，操作失败")
        raise

@then("验证结果")
def step_impl(context):
    try:
        wait = WebDriverWait(context.driver, 2)
        all_static_texts = wait.until(
            EC.presence_of_all_elements_located((
                AppiumBy.CLASS_NAME, 
                "XCUIElementTypeStaticText"
            ))
        )
        
        # 验证元素数量至少为2个
        assert len(all_static_texts) >= 2, f"❌ 符合条件的元素不足2个，实际数量：{len(all_static_texts)}"
        
        # 取第二个元素（索引为1）
        second_element = all_static_texts[1]
        
        # 输出第二个元素的信息（验证是否为目标元素）
        element_value = second_element.get_attribute("value") or "无value属性"
        # 替换掉左-to-right标记（\u200e）
        cleaned_value = element_value.replace("\u200e", "")
        
        # （可选）验证第二个元素的value是否为"2"
        assert cleaned_value == "2", f"❌ 第二个元素的value不是预期的2'，实际为：{cleaned_value}"
        print("✅ 结果验证通过，计算结果为2")

    except TimeoutException:
        error_msg = "❌ 验证失败：未找到结果显示元素（超时）"
        print(error_msg)
        raise AssertionError(error_msg)  # 抛出断言错误，标记测试失败
    except Exception as e:
        error_msg = f"❌ 验证失败：发生未知错误 - {str(e)}"
        print(error_msg)
        raise AssertionError(error_msg)

@then("等待20秒后退出")
def step_impl(context):
    time.sleep(20)
    print("✅ 测试完成，准备退出")
