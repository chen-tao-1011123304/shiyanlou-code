"""
1   b5  标志位
2   b5  标志位
3   0e  14个字节
4   c3  表示本帧内容温度
5   34  地址低八位
6   04  地址高八位   区分仪器
7   01  不起作用
8   05  校验和
9   00  不起作用
10  18  tm_flag 显示温度相关信息
11  6e  温度低八位
12  01  温度高八位
13  00  不起作用
14  00  不起作用


a = "b5b50ec33404010c001867010000"
c = '3404'
d = '6701'
b1 = a[8:10]
b2 = a[10:12]
e1 = a[20:22]
e2 = a[22:24]
deviceID = '{0}{1}'.format(b2, b1)
temperature_str = '{0}{1}'.format(e2, e1)
temperature_int = int(temperature_str, 16)
print(deviceID)
print(temperature_str)
print(temperature_int)
"""


import serial  # 导入串口包
import binascii    # 导入hex转换包
import time

log = 0  # 设一个log变量用于记录单次接收次数
s = serial.Serial('com4', 9600, timeout=2)  # 打开串口，配置串口

while True:  # 无限循环读取数据
    n = s.readline()  # 读取串口一行数据
    log += 1  # 传输次数记录+1
    data_pre = binascii.b2a_hex(n)[::1]
    if data_pre:
        # 获取当前时间
        time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        # 变成字符串str
        data = data_pre.decode()

        # 设备低八位字符
        deviceID_low = data[8:10]
        # 设备高八位字符
        deviceID_high = data[10:12]
        # 温度低八位字符
        temperature__low = data[20:22]
        # 温度高八位字符
        temperature_high = data[22:24]

        # 设备号 str
        deviceID_str = '{0}{1}'.format(deviceID_high, deviceID_low)
        # 温度 str
        temperature_str = '{0}{1}'.format(temperature_high, temperature__low)

        # 设备号 10进制
        deviceID = int(deviceID_str, 16)
        # 温度 10进制
        temperature = float(int(temperature_str, 16)/10)

        print(data)
        print(deviceID)
        print(temperature)
        print(time_str)
        print(log)


