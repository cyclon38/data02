'''
Config : UTF-8

Title : 외부 서비스 체크 스크립트 v1.1

Write : 22.03.07 / Update :22.03.11

'''
import requests
from datetime import datetime
import time

# result_list.csv파일 쓰기모드(w)로 열기 및 헤더 추가하기
f = open("result_list.csv","w",encoding="UTF-8")
f.write("구분,URL,시간,체크유무"+ "\n")

while True: 
    # 체크 URL 및 requests 라이브러리 사용하기
    url1 ="https://bigdata.seoul.go.kr/"
    url2 ="https://cran.seoul.go.kr/"
    response1 = requests.get(url1)
    response2 = requests.get(url2)
    # 현재 시간 체크 불러오기
    dt1 = datetime.now()
    dt10 = dt1.strftime('%Y-%m-%d %I:%M:%S')
    dt11 = dt1.strftime('%Y-%m-%d')
    dt12 = dt1.strftime('%I:%M:%S')
    # 변수 리스트
    title1 = "빅데이터 누리집 체크"
    title2 = "R-Cran 체크"
    check1 = "정상입니다"
    check2 = "실패입니다"
    # 제어 구간 01
    if response1.status_code == 200:
        print(dt11+","+dt12+","+title1+","+url1+ ","+check1)
        f.write(dt11+","+dt12+","+title1+","+url1+","+check1+"\n")
    else:
        print(dt11+","+dt12+","+title1+","+url1+","+check2)
        f.write(dt11+","+dt12+","+title1+","+url1+","+check2+"\n")
    # 제어 구간 02
    if response2.status_code == 200:
        print(dt11+","+dt12+","+title2+","+url1+ ","+check1)
        f.write(dt11+","+dt12+","+title2+","+url1+","+check1+"\n")
    else:
        print(title2+","+url2+","+dt10+","+check2)
        f.write(dt11+","+dt12+","+title2+","+url1+","+check2+"\n")
    # 파일 닫기 수행
    f.close()
    # 10초간 쉬기
    print()
    print ("....10 seconds After processing....")
    time.sleep(10)
    print()
    # result_list.csv파일 증분쓰기모드(a)로 열기
    f = open("result_list.csv","a",encoding="UTF-8")