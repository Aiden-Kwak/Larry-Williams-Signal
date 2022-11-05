# Larry-Williams-Signal


### 변동성 돌파전략 (Larry Williams)

> 1. 전일 Range계산: 고점 - 저점<br>
> 2. 매수: 가격 > 시가 + (X*전일 Range), X = 0.5가 일반적<br>
> 3. 다음날 시가 매도

### 목적
> 본 프로그램은 변동성 돌파전략을 바탕으로 코스닥 전 종목을 순회하여 상승 관성을 만들어낸 종목을 판별하고, 이로써 투자참고지표를 제공하는 것을 목표로 한다.

### 실행

```bash
$ python -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
$ cd core
$ python vb.py
```


