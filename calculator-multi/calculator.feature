Feature: 打开计算器App
  验证在iOS设备上计算1+1=2

  Scenario: 启动计算器App并验证
    Given iOS设备已连接且Appium服务已启动
    When 点击1+1=按钮
    Then 验证结果
    Then 等待10秒后退出
