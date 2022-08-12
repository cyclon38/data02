'''
Config : UTF-8

Title : 보안 사이트 스켈핑 스크립트 v2

Write : 22.05.19 / Update :22.05.19

'''
# 라이브러리 import
import requests
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parser
import pandas as pd
#
import gspread

#
##1. 보호 나라 웹사이트 게시판 크롤링
#
# url html 변경 >> bs >> html.parser #html_01 = response_01.text
URL_01 = 'https://www.boho.or.kr/data/secNoticeList.do'
response_01 = requests.get(URL_01)
soup_01 = BeautifulSoup(response_01.text, 'html.parser')

# 정상(200번)이면 출력
if response_01.status_code == 200:
    # find("table") 테이블 추출 >> parser 를 이용한 테이블 추출
    table_01 = soup_01.find("table")
    p_table_01 = parser.make2d(table_01)

# 200이 아니면 코드 번호 출력
else :
    print(response_01.status_code)
#
## Pandas 영역
#
# pandas 프레임
df_01 = pd.DataFrame(p_table_01)
# 출력 = 입력.rename(columns=입력.iloc[0]) # 첫번째 행이 첫줄로 변경됨
df_02 = df_01.rename(columns=df_01.iloc[0])
# 출력 = 입력.drop(입력.index[0]) # 첫번째 행 삭제
df_03 = df_02.drop(df_02.index[0])
# 출력 =  입력 [['열제목','열제목','열제목']]
df_04 = df_03[['번호','제목','게시일']]
# 출력 = 입력[~입력['열제목'].isin(['열내용'])]  # ~ 입력 하면 제외 , 빼면 내용만 출력
df_05 = df_04[~df_04['번호'].isin(['[공지]'])]
# 출력 = 제목, 게시일만 추출
df_06 = df_05[['제목','게시일']]
# index 추가 하기
df_06.reset_index(drop = False, inplace = True)
# 출력 = 필요 한 필드만 추출
df_07 = df_06[["제목","게시일"]]

#
##2. 알약 게시판 div 추출 : std_220512.ipynb
#
URL_2 = 'https://blog.alyac.co.kr/category/%EA%B5%AD%EB%82%B4%EC%99%B8%20%EB%B3%B4%EC%95%88%EB%8F%99%ED%96%A5'
response_2 = requests.get(URL_2)
soup_2 = BeautifulSoup(response_2.content, 'html.parser')

# 정상(200번)이면 출력
if response_2.status_code == 200:
    #
    list1 = []
    list2 = []
    #
    for num in range(8) :
        list1.append(soup_2.find_all(["p"],["txt_thumb"])[num].text)
    #
    for num2 in range(8,16) :
        list2.append(soup_2.select("span.date")[num2].text)
# 200이 아니면 코드 번호 출력
else :
    print(response_2.status_code)
#
# PANDAS 영역
#
# 제목 리스트 가져오기
df_11 = pd.DataFrame(list1)
df_f_11 = df_11.reset_index(drop=True)
df_f_11.columns = ['제목']
# 게시일 리스트 가져오기
df_12 = pd.DataFrame(list2)
df_f_12 = df_12.reset_index(drop=True)
df_f_12.columns = ['게시일']
# 프레임 합치기
df_1 = pd.concat([df_f_11,df_f_12],axis=1)
'''
#
##3. 보안뉴스 게시판 크롤링 : std_220518.ipynb
#
url_3 = 'https://www.boannews.com/media/t_list.asp'
response_3 = requests.get(url_3)
soup_3 = BeautifulSoup(response_3.content, 'html.parser')

# 정상(200번)이면 출력
if response_3.status_code == 200:
    #
    list01 = soup_3.find_all("span",attrs={'class':'news_txt'})
    list02 = soup_3.select('span.news_writer')
    #
    list1 = []
    list2 = []
    #
    for list_01 in list01 :
        list1.append(list_01.text)
    #
    for list_02 in list02 :
        list2.append(list_02.text)
# 200이 아니면 코드 번호 출력
else :
    print(response_3.status_code)

#
## Pandas 영역
#
# pandas 프레임 > 제목 추출
df_21 = pd.DataFrame(list1)
df_21.columns = ['제목']
# pandas 프레임 >  추출
df_22 = pd.DataFrame(list2)
df_22.columns = ['게시일']
df_22_1 = df_22['게시일']
df_22_2 = df_22_1.str.split('|')
df_23 = df_22_2.str.get(1)
# 프레임 합치기
df_24 = pd.concat([df_21,df_23],axis=1)
# 10개 게시물만 추출하기
df_24 = df_24.head(10)
'''
#
# json 파일 읽기 >> sheet 선택 하기 >> C:\DEV_OPS\STD_Dev\python_vs\my-project-220331-48561b9c1e32.json
#
gc = gspread.service_account(filename="my-project-220331-48561b9c1e32.json")
sh = gc.open("testsheet").worksheet("시트2")
#
# 출력물 완성
print('== 보호나라 게시물 =======================================================================')
#
# 날짜 별 for 문 추출
for i in range(len(df_07)): #print(df_07.loc[i,"게시일"]+","+df_07.loc[i,"제목"])
    # 결과 변수 저장
    out_01 = df_07.loc[i,"게시일"]
    out_02 = df_07.loc[i,"제목"]
    OUT_03 = "KISA인터넷보호나라"
    # 내용 출력
    print(out_01+","+out_02)
    # 구글시트 추가 등록
    sh.append_row([out_01,out_02,OUT_03])
#
# 출력물 완성
print('== 알약 게시물 =======================================================================')
#
# 날짜 별 for 문 추출
for i in range(len(df_1)): #print(df_07.loc[i,"게시일"]+","+df_07.loc[i,"제목"])
    # 결과 변수 저장
    out_01 = df_1.loc[i,"게시일"]
    out_02 = df_1.loc[i,"제목"]
    OUT_03 = "알약"
    # 내용 출력
    print(out_01+","+out_02)
    # 구글시트 추가 등록
    sh.append_row([out_01,out_02,OUT_03])
'''
#
# 출력물 완성
print('== 보안뉴스 게시물 =======================================================================')
#
# 날짜 별 for 문 추출
for i in range(len(df_24)): #print(df_07.loc[i,"게시일"]+","+df_07.loc[i,"제목"])
    # 결과 변수 저장
    out_01 = df_24.loc[i,"게시일"]
    out_02 = df_24.loc[i,"제목"]
    out_03 = "보안뉴스"
    # 내용 출력
    print(out_01+","+out_02)
    # 구글시트 추가 등록
    sh.append_row([out_01,out_02,out_03])
'''
