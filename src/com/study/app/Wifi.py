import pywifi
from pywifi import const


# �ж��Ƿ����ӵ�wifi����
def gic():
    wifi = pywifi.PyWiFi()
    # print(str(wifi))
    iface = wifi.interfaces()[0]
    # print(iface.name())
    # print(iface.status())
    if iface.status() == const.IFACE_DISCONNECTED:
        print('wifiδ����')
    else:
        print('wifi������')

def bies():
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    ifaces.scan()
    bessis = ifaces.scan_results()
    # print(bessis)
    for wifi in bessis:
        print(wifi.ssid)
    

# gic()
bies()