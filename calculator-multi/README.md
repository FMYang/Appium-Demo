# 多设备并行测试计算器App

本项目使用Appium和Behave框架实现了iOS设备上计算器App的自动化测试，支持多设备并行测试。

## 项目结构

```
calculator/
├── calculator.feature  # Feature文件，定义测试场景
├── environment.py      # 环境配置文件
├── config.py           # 设备配置文件
├── run_tests.py        # 多设备并行测试启动脚本
└── steps/
    └── step.py         # Step定义文件
```

## 环境要求

- Python 3.7+
- Appium 2.x
- Behave
- Appium-Python-Client
- iOS设备或模拟器
- Xcode（用于iOS测试）

## 安装依赖

```bash
pip install behave appium-python-client
```

## 配置设备

在`config.py`文件中配置要测试的iOS设备信息：

```python
# iOS设备配置列表
DEVICES = [
    {
        'name': 'device1',              # 设备名称（用于标识）
        'platform_name': 'iOS',         # 平台名称
        'automation_name': 'XCUITest',  # 自动化引擎
        'device_name': '设备名称',       # 设备显示名称
        'udid': '设备UDID',             # 设备唯一标识符
        'appium_port': 4723,            # Appium服务端口（每个设备不同）
        'wda_local_port': 8100,         # WebDriverAgent端口（每个设备不同）
        'bundle_id': 'com.apple.calculator'  # 应用Bundle ID
    },
    # 可以添加更多设备配置...
]
```

**重要配置说明：**
- 每个设备必须使用不同的`appium_port`和`wda_local_port`
- `wda_local_port`用于WebDriverAgent通信，默认端口8100可能被占用
- 确保配置的端口未被其他进程占用

## 运行测试

### 运行单个设备测试

可以通过设置环境变量来指定测试设备：

```bash
# 使用第一个设备（索引0）
DEVICE_INDEX=0 behave

# 使用第二个设备（索引1）
DEVICE_INDEX=1 behave
```

### 并行运行多设备测试

使用提供的启动脚本可以同时在所有配置的设备上运行测试：

```bash
python run_tests.py
```

脚本会为每台设备启动一个独立的测试进程，并实时显示每台设备的测试进度和结果。

## 自定义测试用例

可以在`calculator.feature`文件中添加更多的测试场景，并在`steps/step.py`中实现对应的步骤定义。

## 注意事项

1. 确保所有设备都已正确连接并被Xcode识别
2. 每个设备必须使用不同的Appium服务端口
3. 运行前确保没有其他Appium服务占用配置的端口
4. 对于模拟器，确保模拟器已安装并且可以正常启动
5. 在macOS上，可能需要在系统偏好设置中授予自动化控制权限