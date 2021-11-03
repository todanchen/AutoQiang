from core.auto_base import JinDonBuy

if __name__ == '__main__':
    shop_url = 'https://item.jd.com/100028031368.html'
    start_time = '2021-11-04 20:00:00'
    jdb = JinDonBuy(start_time, shop_url)
    jdb.auto_buy()
