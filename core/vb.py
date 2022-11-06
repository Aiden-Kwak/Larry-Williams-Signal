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
def is_weekend(d):
    return d.weekday() > 4
def prev_tradingday(): # 주말만 제외됨. 공휴일 에러
    day = 0
    check_weekend = today
    while (is_weekend(check_weekend) == True):
        day+=1 
        check_weekend = today - datetime.timedelta(days=day)
        
    return today - datetime.timedelta(days=day)

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
        return float(now_price), float(start_price)


data = list()
for i, code in enumerate(code_list):
    print(i, name_list[i])
    try:
        get_price0 = get_price(code) # 통신a_1회
        now_price = get_price0[0]
        start_price = get_price0[1]
        yesterday_df = fdr.DataReader(code, prev_tradingday()) # 통신b_1회
        high = yesterday_df['High']
        low = yesterday_df['Low']
        vb_range = high-low
        formula = start_price + (0.5*int(vb_range))
        if now_price > formula:
            data.append(name_list[i])
        else:
            pass
        
        print('진행도: ['+ str(i+1) +'/'+str(len(code_list))+'], 탐색된종목수: '+str(len(data)))

    except Exception as e:
        print('errror, passed', e)
        time.sleep(2)

print(data)