#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
多设备并行测试启动脚本
"""

import os
import sys
import subprocess
import time
import signal
from multiprocessing import Process
from config import DEVICES

def run_test_on_device(device_index):
    """在指定设备上运行测试"""
    print(f"🚀 启动设备 {DEVICES[device_index]['name']} 的测试进程")
    
    # 设置环境变量
    env = os.environ.copy()
    env['DEVICE_INDEX'] = str(device_index)
    
    try:
        # 运行behave测试
        process = subprocess.Popen(
            ['behave', '-f', 'pretty'],
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # 实时输出
        for line in process.stdout:
            print(f"[{DEVICES[device_index]['name']}] {line.strip()}")
        
        # 等待进程完成
        stdout, stderr = process.communicate()
        
        # 输出剩余内容
        if stdout:
            print(f"[{DEVICES[device_index]['name']}] {stdout.strip()}")
        if stderr:
            print(f"[{DEVICES[device_index]['name']}] ERROR: {stderr.strip()}")
        
        return process.returncode
    except Exception as e:
        print(f"❌ 设备 {DEVICES[device_index]['name']} 测试失败: {str(e)}")
        return 1

def main():
    """主函数"""
    print("📋 开始多设备并行测试")
    print(f"📱 共 {len(DEVICES)} 台设备需要测试")
    
    # 创建并启动进程
    processes = []
    for i in range(len(DEVICES)):
        p = Process(target=run_test_on_device, args=(i,))
        processes.append(p)
        p.start()
        # 避免同时启动多个进程造成资源竞争
        time.sleep(1)
    
    # 等待所有进程完成
    exit_codes = []
    for p in processes:
        p.join()
        exit_codes.append(p.exitcode)
    
    # 汇总结果
    success_count = exit_codes.count(0)
    print("\n📊 测试结果汇总")
    print(f"✅ 成功: {success_count} 台设备")
    print(f"❌ 失败: {len(exit_codes) - success_count} 台设备")
    
    # 设置退出码
    sys.exit(0 if all(code == 0 for code in exit_codes) else 1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⚠️  用户中断测试")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 测试启动失败: {str(e)}")
        sys.exit(1)