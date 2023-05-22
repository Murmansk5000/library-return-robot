import time

from pymycobot import MyCobotSocket, Coord


def pick(location):
    # 初始位置
    '''mc.send_angles([-90, -80, -20, 0, 50, 0], 20)
    time.sleep(5)
    mc.set_gripper_state(0, 50)
    time.sleep(2)'''

    if location == 1:
        print("Picking book 1")
        # 第一个取书前位姿
        '''mc.send_angles([-2.9, 70, -165, -88.59, 52.38, 1.84], 20)
        time.sleep(5)'''
        # 第一个取书位姿
        mc.send_angles([0, 26.89, -96.32, -79.27, 113.2, 19.07], 20)
        time.sleep(4)
        '''# 夹书
        mc.set_gripper_value(60, 20)
        time.sleep(3)
        # 夹书后撤
        mc.send_angles([46.93, 68, -150.46, -136.49, 91.66, 5], 40)
        time.sleep(3)
        # 抬高
        mc.send_angles([46.93, 55, -150.46, -136.49, 0, 5], 40)
        time.sleep(4)'''
    elif location == 2:
        print("Picking book 2")
        # 第二个取书前位姿
        mc.send_angles([-118.3, -30, -22, 60.2, 32, -40], 20)
        time.sleep(5)
        # 第二个取书位姿
        mc.send_angles([-121.9, -33, -13.09, 36, 69.78, -23.64], 20)
        time.sleep(4)
        # 夹书
        mc.set_gripper_value(60, 20)
        time.sleep(3)
        # 夹书后撤
        mc.send_angles([-96.06, -58.97, -12.74, 8.96, 75.05, -3.07], 40)
        time.sleep(3)
        # 抬高
        mc.send_angles([-96.06, -64.77, -12.74, 23.2, 12.65, -19.68], 40)
        time.sleep(4)
    elif location == 3:
        print("Picking book 3")
        # 第三个取书前位姿
        mc.send_angles([0, -43.59, -21.7, -103.88, 56.68, 26.36], 20)
        time.sleep(5)
        # # 第三个取书位姿
        mc.send_angles([0, -43.59, -21.7, -85.6, 99.4, 24.52], 20)
        time.sleep(4)
        # 夹书
        mc.set_gripper_value(60, 20)
        time.sleep(2)
        # 夹书后撤
        mc.send_angles([-80, -50, -35, -15, 86.83, 0], 40)
        time.sleep(3)
        # 抬高
        mc.send_angles([-80, -50, -35, -15, 10, 0], 40)
        time.sleep(4)
    elif location == 4:
        print("Picking book 4")
        # 第四个取书前位姿
        mc.send_angles([5, -57, -25, -88.85, 45, 0], 20)
        time.sleep(5)
        # # 第四个取书位姿
        mc.send_angles([5, -57, -25, -90, 88, 0], 20)
        time.sleep(4)
        # 夹书
        mc.set_gripper_value(60, 20)
        time.sleep(2)
        # 夹书后撤
        mc.send_angles([-29.97, -60, -25, -59.5, 90, -0.17], 40)
        time.sleep(3)
        # 抬高
        mc.send_angles([-29.53, -50, -35, -61.43, 0, 0.7], 40)
        time.sleep(4)
    elif location == 5:
        print("Picking book 5")
        # 第五个取书前位姿
        mc.send_angles([0, -65, -63, -45, 59.76, -58.18], 40)
        time.sleep(5)
        # 第五个取书位姿
        mc.send_angles([0, -63.19, -45, -88.59, 88.68, -30], 20)
        time.sleep(4)
        # 夹书
        mc.set_gripper_value(60, 20)
        time.sleep(2)
        # 夹书后撤
        mc.send_angles([-23.46, -55, -65.91, -68, 99.58, -43], 20)
        time.sleep(4)
        # 抬高
        mc.send_angles([-22.85, -66.62, -60, -2.19, 49.65, -68.37], 40)
        time.sleep(4)
    else:
        print("Book location is wrong!")

    # 抬高后操作
    '''mc.send_angles([0, -20, -50, 0, -5, 0], 40)
    time.sleep(4)
    mc.send_angles([0, -80, -20, 0, 80, 0], 20)
    time.sleep(4)
    mc.send_angles([0, 25, 15.46, -1.31, -65, 0], 40)
    time.sleep(4)'''
    mc.set_gripper_state(0, 50)
    time.sleep(2)
    '''mc.send_angles([0, -80, -20, 0, 50, 0], 40)
    time.sleep(3)'''


if __name__ == "__main__":
    # 默认使用9000端口
    # 其中"192.168.11.15"为机械臂IP，请自行输入你的机械臂IP
    # mc = MyCobotSocket("10.149.1.137",9000)
    mc = MyCobotSocket("10.142.223.177", 9000)

    # 树莓派版本需要输入connect函数，默认值为("/dev/ttyAMA0","1000000")
    mc.connect("/dev/ttyAMA0", "1000000")

    print("Arm has been connected!")

    book_location = 1  # (1-5)

    pick(book_location)

# 旋转角度-160————150

# 调试
    #mc.release_all_servos()
    #print(mc.get_angles())
# mc.set_gripper_state(1, 50)
# mc.send_angles([0, 9.31, 15.46, -1.31, -30.58, 0],40)
