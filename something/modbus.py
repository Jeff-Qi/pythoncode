# -*- coding: utf-8 -*-
# @Time :2020/3/27 16:30
# @Author   :jerry qi
# @Email    :270352195@qq.com
import modbus_tk.modbus_tcp as mt
import modbus_tk.defines as md

master = mt.TcpMaster("127.0.0.1", 502)  # 远程连接到服务器端
master.set_timeout(5.0)  # 超时时间

hold_value = master.execute(slave=1, function_code=md.READ_HOLDING_REGISTERS, starting_address=0, quantity_of_x=3,
                            output_value=5)
print(hold_value)


def crc16(x, invert):
    a = 0xFFFF
    b = 0xA001
    for byte in x:
        a ^= ord(byte)
        for i in range(8):
            last = a % 2
            a >>= 1
            if last == 1:
                a ^= b
    s = hex(a).upper()

    return s[4:6] + s[2:4] if invert == True else s[2:4] + s[4:6]


print(crc16(str(hold_value), False))
