from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.appium_service import AppiumService
import time

def before_all(context):
    # 启动Appium服务
    context.appium_service = AppiumService()
    context.appium_service.start(
        args=['--address', '127.0.0.1', '--port', '4723'],
        timeout_ms=20000
    )
    time.sleep(2)  # 等待服务稳定

    # 配置iOS设备参数（替换为你的设备信息）
    options = XCUITestOptions()
    options.platform_name = "iOS"
    options.automation_name = "XCUITest"
    options.device_name = "杨方明的iPhone"  # 如"iPhone 14"
    options.udid = "00008120-00146DAE34E0C01E"        # 如"00008120-00146DAE34E0C01E"
    options.new_command_timeout = 300
    
    # 币安App的Bundle ID（iOS）
    options.bundle_id = "com.czzhao.binance"  # 正式版可能为"com.binance"
    
    # 配置开发者证书（必要时填写）
    # options.set_capability("xcodeOrgId", "你的团队ID")
    # options.set_capability("xcodeSigningId", "iPhone Developer")

    # 初始化驱动
    try:
        context.driver = webdriver.Remote(
            command_executor="http://127.0.0.1:4723",
            options=options
        )
    except Exception as e:
        print(f"❌ 创建会话失败: {str(e)}")
        context.appium_service.stop()
        raise

def after_all(context):
    # 清理资源
    # if hasattr(context, 'driver'):
    #     context.driver.quit()
    # if hasattr(context, 'appium_service') and context.appium_service.is_running:
    #     context.appium_service.stop()
    print("✅ 资源已清理")
