from core.auto_base import LenovoBuy

if __name__ == '__main__':
    shop_url = 'https://item.lenovo.com.cn/product/1018763.html'
    start_time = '2021-11-04 20:00:00'
    buy_obj = LenovoBuy(start_time, shop_url)
    buy_obj.auto_buy()