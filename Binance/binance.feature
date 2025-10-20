Feature: 打开币安App
  验证在iOS设备上成功启动币安应用

  Scenario: 启动币安App并验证
    Given iOS设备已连接且Appium服务已启动
    When 点击设置-Aplha活动-空投
    And 等待20秒后退出
