Feature: 打开iPhone上的App Store
  验证通过Appium在iPhone真机上打开App Store应用

  Scenario: 启动App Store并验证
    Given iPhone真机已连接且Appium服务正常
    When 打开AppStore
    When 点击搜索按钮和输入框
    When 输入王者荣耀并搜索
    When 等待搜索结果并点击王者荣耀下载按钮
    And 等待20秒后退出
