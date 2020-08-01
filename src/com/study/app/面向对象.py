# 定义接口支付
class PayManager:
    def pay(self):
        print('使用默认支付...')
        pass


class LoginManager:
    def login(self):
        print('使用默认登陆...')
        pass


class WeChatApp(PayManager, LoginManager):
    def pay(self):
        print('使用微信支付...')
        pass

    def login(self):
        print('微信登陆...')
        pass


class AliPayApp(PayManager, LoginManager):
    def pay(self):
        print('使用支付宝支付...')
        pass

    def login(self):
        print('支付宝登陆...')
        pass


class BankPayApp(PayManager, LoginManager):
    def pay(self):
        print('使用银行卡支付...')
        pass

    def login(self):
        print('银行账号登陆...')
        pass


def test(payType):
    if payType == 0:
        payManager = WeChatApp()
    elif payType == 1:
        payManager = AliPayApp()
    elif payType == 2:
        payManager = BankPayApp()
    else:
        payManager = PayManager()

    if isinstance(payManager, WeChatApp):
        print('微信')
    elif isinstance(payManager, AliPayApp):
        print('支付宝')
    elif isinstance(payManager, BankPayApp):
        print('银行卡')
    else:
        print('默认的')

    payManager.pay()
    if isinstance(payManager, LoginManager):
        payManager.login()
    print('=================================分割线======================================')

test(0)
test(1)
test(2)
test(3)
