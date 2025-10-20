from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.appium_service import AppiumService
import time
import os
import sys
from config import DEVICES

def before_all(context):
    # 获取设备索引，如果未指定则使用第一个设备
    device_index = int(os.environ.get('DEVICE_INDEX', 0))
    
    # 确保索引在有效范围内
    if device_index >= len(DEVICES):
        print(f"❌ 设备索引 {device_index} 超出范围，最大索引为 {len(DEVICES) - 1}")
        sys.exit(1)
    
    # 获取当前设备配置
    device_config = DEVICES[device_index]
    context.device_name = device_config['name']
    print(f"📱 开始测试设备: {device_config['device_name']} (UDID: {device_config['udid']})")
    
    # 启动Appium服务（每个设备使用不同端口）
    context.appium_service = AppiumService()
    appium_port = device_config['appium_port']
    context.appium_service.start(
        args=['--address', '127.0.0.1', '--port', str(appium_port)],
        timeout_ms=20000
    )
    time.sleep(2)  # 等待服务稳定

    # 配置iOS设备参数
    options = XCUITestOptions()
    options.platform_name = device_config['platform_name']
    options.automation_name = device_config['automation_name']
    options.device_name = device_config['device_name']
    options.udid = device_config['udid']
    options.new_command_timeout = 300
    options.bundle_id = device_config['bundle_id']
    
    # 设置WebDriverAgent端口，避免多设备测试时端口冲突
    if 'wda_local_port' in device_config:
        options.wda_local_port = device_config['wda_local_port']
        print(f"🔌 已设置WebDriverAgent端口: {device_config['wda_local_port']}")
    
    # 获取设备特定的超时配置
    element_timeout = device_config.get('element_timeout', 2)  # 默认5秒
    implicit_wait = device_config.get('implicit_wait', 1)    # 默认1秒
    
    # 初始化驱动
    try:
        context.driver = webdriver.Remote(
            command_executor=f"http://127.0.0.1:{appium_port}",
            options=options
        )
        
        # 设置隐式等待时间，根据设备性能调整
        context.driver.implicitly_wait(implicit_wait)
        print(f"✅ 成功连接到设备: {device_config['device_name']}")
        print(f"⏱️  设备超时配置 - 元素查找: {element_timeout}秒, 隐式等待: {implicit_wait}秒")
        
        # 将超时配置存储到context中，供step.py使用
        context.element_timeout = element_timeout
    except Exception as e:
        print(f"❌ 创建会话失败: {str(e)}")
        context.appium_service.stop()
        raise

def after_all(context):
    print(f"✅ 设备 {context.device_name} 资源已清理")
    if hasattr(context, 'driver'):
        try:
            context.driver.quit()
        except:
            pass
    if hasattr(context, 'appium_service'):
        try:
            context.appium_service.stop()
        except:
            pass
