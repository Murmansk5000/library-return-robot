# 硬件验证脚本

这里的脚本用于验证单个硬件接口，**不是可在普通电脑上运行的自动化测试**。它们可能直接驱动电机、舵机或 GPIO；执行前请抬空底盘、断开机械臂负载并确认引脚编号。

| 目录 | 用途 |
| --- | --- |
| `hardware/arduino/ultrasonic_sensor` | 验证 HC-SR04 类超声模块的测距逻辑。 |
| `hardware/arduino/servo` | 验证 Arduino 舵机输出。 |
| `hardware/jetson` | 验证 Jetson 的 I2C 总线、PWM 和 PCA9685 舵机控制器。 |
| `hardware/raspberry_pi` | 验证 Raspberry Pi 的红外输入与电机驱动 GPIO。 |
| `hardware/serial` | 向 Arduino 发送 `S` 停车指令，验证串口连通性。 |

脚本里的引脚号、串口路径和波特率都是原型机配置；使用前应按现场设备修改。
