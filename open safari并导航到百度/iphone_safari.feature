Feature: 在iPhone上打开Safari并访问网页
  测试通过Appium在iPhone设备上启动Safari并验证网页访问

  Scenario: 启动iPhone上的Safari并打开百度
    Given iPhone设备已连接且Safari已配置
    When 在Safari中打开百度首页
    Then 验证页面标题包含"百度"
    And 等待5秒后关闭会话
