from appium import webdriver
from appium.options.ios import XCUITestOptions

def before_all(context):
    # 配置iPhone设备和Safari参数
    options = XCUITestOptions()
    
    # 设备基础信息（必须替换为你的设备信息）
    options.platform_name = "iOS"
    options.device_name = "杨方明的iPhone"  # 在Xcode的Devices and Simulators中查看
    options.udid = "00008120-00146DAE34E0C01E"           # 设备唯一标识符
    options.browser_name = "Safari"         # 指定浏览器为Safari
    options.automation_name = "XCUITest"    # iOS必须使用XCUITest引擎
    
    # 可选配置：解决启动问题
    options.new_command_timeout = 3600      # 命令超时时间（秒）
    options.include_safari_in_webviews = True  # 允许访问Safari的webview
    
    # 连接Appium服务器（默认地址）
    context.driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4723",
        options=options
    )

def after_all(context):
    # 测试结束后关闭会话
    if hasattr(context, 'driver'):
        context.driver.quit()
