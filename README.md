# Appium-Demo
appiun test demo

安装appium3

-> npm install -g appium@beta

安装ios自动化测试插件
-> appium driver install xcuitest


真机测试需要设置webdriverrunner工程证书，命令行打开工程 -> open /Users/yfm/.appium/node_modules/appium-xcuitest-driver/node_modules/appium-webdriveragent/WebDriverAgent.xcodeproj

启动appium
-> appium


Appium inspector下载地址https://github.com/appium/appium-inspector，下载安装好后，配置下面参数启动测试

Appium inspector模拟器配置
{
  "appium:automationName": "XCUITest",
  "platformName": "ios",
  "appium:deviceName": "iPhone 16 Pro",
  "appium:platformVersion": "18.0",
  "appium:bundleId": "com.apple.mobilesafari"
}


真机配置
{
  "platformName": "iOS",
  "appium:automationName": "XCUITest",
  "appium:udid": "00008120-00146DAE34E0C01E",
  "appium:deviceName": "杨方明的iPhone"
}


python测试，启动虚拟环境

-> python3 -m venv path/to/venv  # 创建虚拟环境（path/to/venv 替换为实际路径，如 ./myenv）
-> source path/to/venv/bin/activate  # 激活虚拟环境（Windows 系统用：path/to/venv/Scripts/activate）
-> pip3 install behave  # 在虚拟环境中安装包
