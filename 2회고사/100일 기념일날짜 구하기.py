from datetime import datetime, timedelta

#함수정의 부분
def getCurrent():
    curDate = datetime.now()
    return curDate

def getAfterDate(now, day):
    retDate = now+timedelta(days=day)
    return retDate


#전역변수 선언 부분
nowDate, afterDate = None, None

#메인코드 부분
nowDate = getCurrent()
print("현재 날짜와 시간==>", nowDate)
afterDate = getAfterDate(nowDate, 100)
print("100일 후 날짜와 시간==>",afterDate)
