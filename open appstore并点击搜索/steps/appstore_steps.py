from behave import given, when, then
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given("iPhone真机已连接且Appium服务正常")
def step_impl(context):
    assert context.appium_service.is_running, "❌ Appium服务未运行"
    assert context.driver is not None, "❌ WebDriver会话未创建"
    print("✅ 设备和服务状态正常")

@when('打开AppStore')
def step_impl(context):
    try:
        app_store_bundle_id = "com.apple.AppStore"
        context.driver.activate_app(app_store_bundle_id)
        print("✅ App Store启动完成")
    except Exception as e:
        print(f"❌ 打开AppStore失败: {str(e)}")
        raise

@when('点击搜索按钮和输入框')
def step_impl(context):
    try:
        search_button = WebDriverWait(context.driver, 1).until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, "AppStore.tabBar.search")
            )
        )
        search_button.click()
        search_button.click()
        print("✅ 已点击底部搜索按钮")
    except Exception as e:
        print(f"❌ 点击搜索按钮和输入框失败: {str(e)}")
        raise

@when('输入王者荣耀并搜索')
def step_impl(context):
    try:
        searchFiled = WebDriverWait(context.driver, 1).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "AppStore.searchField"))
        )
        searchFiled.send_keys("王者荣耀")
        print("✅ 已输入王者荣耀")
        keyBoardSearch = WebDriverWait(context.driver, 1).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Search"))
        )
        keyBoardSearch.click()
        print("✅ 已点击搜索")
    except Exception as e:
        print(f"❌ 输入王者荣耀并搜索失败: {str(e)}")
        raise

@when('等待搜索结果并点击王者荣耀下载按钮')
def step_impl(context):
    try:
        cell = WebDriverWait(context.driver, 5).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "王者荣耀, S41赛季 天元"))
        )
        cell.click()
        print("✅ 已点击王者荣耀应用")
        downloadButton = WebDriverWait(context.driver, 1).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "RedownloadCloudIcon"))
        )
        downloadButton.click()
        print("✅ 已点击下载按钮")
    except Exception as e:
        print(f"❌ 等待搜索结果并点击王者荣耀下载按钮失败: {str(e)}")
        raise

@then("等待20秒后退出")
def step_impl(context):
    time.sleep(20)  # 延长等待时间，便于观察
    print("✅ 测试结束，准备退出")

# @when("启动App Store应用")
# def step_impl(context):
#     try:
#         # App Store的Bundle ID
#         app_store_bundle_id = "com.apple.AppStore"
        
#         # 通过Bundle ID启动App Store
#         context.driver.activate_app(app_store_bundle_id)
#         print(f"✅ 已尝试启动App Store (Bundle ID: {app_store_bundle_id})")
        
#         # 等待App Store启动完成（通过检测特征元素）
#         WebDriverWait(context.driver, 3).until(
#             EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "AppStore.tabBar.search"))
#         )
#         print("✅ App Store启动完成")
        
#     except Exception as e:
#         print(f"❌ 启动App Store失败: {str(e)}")
#         raise

# @when("点击App Store底部的搜索按钮")
# def step_impl(context):
#     try:
#         # 1. 等待搜索按钮可点击（优先使用accessibility ID）
        # search_button = WebDriverWait(context.driver, 3).until(
        #     EC.element_to_be_clickable(
        #         (AppiumBy.ACCESSIBILITY_ID, "AppStore.tabBar.search")
        #     )
        # )
        
#         # 2. 点击搜索按钮
#         search_button.click()
#         print("✅ 已点击底部搜索按钮")
        
#         # 3. 验证是否进入搜索页面（通过搜索框存在性判断）
#         WebDriverWait(context.driver, 3).until(
#             EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "AppStore.searchField"))
#         )
#         print("✅ 已进入搜索页面")
        
#     except Exception as e:
#         print(f"❌ 点击搜索按钮失败：{str(e)}")
#         raise

# @then("验证App Store已成功打开")
# def step_impl(context):
#     try:
#         # 验证App Store的特征元素存在（搜索按钮）
#         search_element = WebDriverWait(context.driver, 5).until(
#             EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "AppStore.tabBar.search"))
#         )
#         assert search_element.is_displayed(), "❌ 未找到App Store的搜索按钮"
#         print("✅ App Store验证成功")
        
#     except Exception as e:
#         print(f"❌ 验证App Store失败: {str(e)}")
        # raise

# @then("等待10秒后退出")
# def step_impl(context):
#     time.sleep(20)  # 延长等待时间，便于观察
#     print("✅ 测试结束，准备退出")
