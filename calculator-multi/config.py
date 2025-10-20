# 多设备配置文件

# iOS设备配置列表
DEVICES = [
    {
        'name': 'device1',
        'platform_name': 'iOS',
        'automation_name': 'XCUITest',
        'device_name': '杨方明的iPhone',
        'udid': '00008120-00146DAE34E0C01E',
        'appium_port': 4723,
        'wda_local_port': 8100,  # WebDriverAgent端口
        'bundle_id': 'com.apple.calculator',
        'element_timeout': 2,    # 元素查找超时时间(秒)
        'implicit_wait': 1       # 隐式等待时间(秒)
    },
    {
        'name': 'device2',
        # 第二个设备的配置
        'platform_name': 'iOS',
        'automation_name': 'XCUITest',
        'device_name': 'ZY-iPhone16 plus',
        'udid': '00008140-00081484222B001C',
        'appium_port': 4724,
        'wda_local_port': 8101,  # 第二个设备使用不同的WebDriverAgent端口
        'bundle_id': 'com.apple.calculator',
        'element_timeout': 2,    # 性能较慢设备可设置更长的超时时间
        'implicit_wait': 1       # 性能较慢设备可设置更长的隐式等待
    }
]