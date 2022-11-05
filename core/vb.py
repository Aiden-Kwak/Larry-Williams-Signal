# volatility breakout

# > 1. 전일 Range계산: 고점 - 저점<br>
# > 2. 매수: 가격 > 시가 + (X*전일 Range), X = 0.5가 일반적<br>
# > 3. 다음날 시가 매도

from kosdaq_list import *
import FinanceDataReader as fdr
import pandas as pd
import requests
from bs4 import BeautifulSoup
import datetime
import time

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

# test = fdr.DataReader('195940', yesterday)['High']
# print(int(test))


def get_bs_obj(com_code):
        url = "https://finance.naver.com/item/main.nhn?code=" + com_code
        result = requests.get(url)
        bs_obj = BeautifulSoup(result.content, "html.parser")
        return bs_obj

def get_price(com_code):
        bs_obj = get_bs_obj(com_code)
        # 현재가
        no_today = bs_obj.find("p", {"class":"no_today"})
        now_price = no_today.find("span", {"class":"blind"}).text.replace(',','')
        # 시가
        start_price = bs_obj.find("table", {"class":"no_info"}).select(".first > em > .blind")[1].text.replace(',','')
        
        # return blind_now.text
        return float(now_price), float(start_price)

print(get_price('006050'))

# for i, code in code_list:
#     try:
#         now_price = Price.get_price(code)
#         yesterday_df = fdr.DataReader(code, yesterday)
#         high = yesterday_df['High']
#         low = yesterday_df['Low']
#         vb_range = high-low
#         formula = 


#     except:
#         print('errror, passed')
