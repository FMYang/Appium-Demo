from behave import given, when, then
import time

@given("iPhone设备已连接且Safari已配置")
def step_impl(context):
    """验证设备连接和Safari初始化"""
    assert context.driver is not None, "Appium会话创建失败"
    print("iPhone设备已连接，Safari初始化完成")

@when("在Safari中打开百度首页")
def step_impl(context):
    """在Safari中导航到百度首页"""
    context.driver.get("https://www.baidu.com")
    print("已在Safari中打开百度首页")

@then("验证页面标题包含\"百度\"")
def step_impl(context):
    """验证页面标题是否正确"""
    page_title = context.driver.title
    assert "百度" in page_title, f"标题验证失败，实际标题: {page_title}"
    print(f"页面标题验证成功: {page_title}")

@then("等待5秒后关闭会话")
def step_impl(context):
    """等待5秒便于观察效果"""
    time.sleep(5)
