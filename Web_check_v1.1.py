import requests
from bs4 import BeautifulSoup

#1. request
resp1 = requests.get('https://cran.r-project.org/web/packages/') #html1 = resp1.text
resp2 = requests.get('http://cran.seoul.go.kr/web/packages') #html2 = resp2.text
#resp3 = requests.get('https://cran.r-project.org/mirrors.html') #html3 = resp3.text
resp4 = requests.get('https://cran.r-project.org/mirmon_report_release.html') #html4 = resp4.text
resp5 = requests.get('https://cran.r-project.org/mirmon_report_old_release.html') #html5 = resp5.text

resp3 = requests.get('http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?searchType=1&bidSearchType=1&taskClCds=&bidNm=%BA%F2%B5%A5%C0%CC%C5%CD+%C4%B7%C6%DB%BD%BA&searchDtType=1&fromBidDt=2020%2F11%2F02&toBidDt=2021%2F03%2F31&fromOpenBidDt=&toOpenBidDt=&radOrgan=1&instNm=%BC%AD%BF%EF%C6%AF%BA%B0%BD%C3&instSearchRangeType=&refNo=&area=&areaNm=&industry=&industryCd=&budget=&budgetCompare=UP&detailPrdnmNo=&detailPrdnm=&procmntReqNo=&intbidYn=&regYn=Y&recordCountPerPage=10') #html3 = resp3.text


#2-1. BeautifulSoup
soup = BeautifulSoup(resp1.text,'html.parser') #html.parser를 사용해서 soup에 넣겠다
f_div = soup.find("p") #print(str1,f_div)

soup2 = BeautifulSoup(resp2.text,'html.parser') 
f_div2 = soup2.find("p") #print(str2,f_div2)

soup3 = BeautifulSoup(resp3.content,'html.parser') 
soup4 = BeautifulSoup(resp4.content,'html.parser') 
soup5 = BeautifulSoup(resp5.content,'html.parser') 

#2-2. BeautifulSoup 추출내용 print
'''
s1 = str(f_div)     #print(a.split(' '))
s2 = str(f_div2)    #print(b.split(' '))

count1 = s1[52:57]
count2 = s2[52:57]

str1="메인(네덜란드) : "
str2="서울 빅데이터 캠퍼스(한국) : "

print()
print("--"*40)
print(str1,count1+" | "+str2,count2)
print("--"*40)

#3-1. datetime

from datetime import datetime
count3 = datetime.today().strftime("%Y-%m-%d")
data = [[count3,count1,count2]]
#print(data) # data 값 출력
print() 
'''
#3-2. URL Check
print()
print("==="*5," 입창공고 ","==="*5)
print()
#out3_1 = soup3.find_all(['td','a'])
out3_1 = soup3.find_all(['td'])

#print(out3_1)

count = 1
for link in out3_1:
    #print("[",count,"]",link)
    #if count==199:
    print(link)
    count += 1
print()

'''
print("==="*5," mirmon_report_release ","==="*5)
print()

out4_1 = soup4.find_all(['td','a'])

count = 1
for link in out4_1:
    if count==546:
     out5 = link.get('href')
     print("[Check --> ] "+out5)
     print()
    elif count==551:
     print("[OK Check --> ]",link)
     print()
    else:
      pass
    
    count += 1

print("==="*5," mirmon_report_old_releas ","==="*5)
print()
out5_1 = soup5.find_all(['td','a'])

count = 1
for link in out5_1:
    if count==546:
     out5 = link.get('href')
     print("[Check --> ] "+out5)
     print()
    elif count==551:
     print("[OK Check --> ]",link)
     print()
    else:
      pass

    count += 1

print("--"*40)
'''
'''
#4. csv file write 단계

import csv
with open('./R_Day_check.csv','a',newline='') as f:
    mw = csv.writer(f)

    for value in data:
        mw.writerow(value)

#5. 체크 URL 다이얼창 띄우기

import wx
import webbrowser

class Frame(wx.Frame):
    #def: 창 디지인 함수
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(280, 90))
        self.panel = wx.Panel(self)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        
        #버튼 코드
        self.btn1 = wx.Button(self.panel, -1, "예") 
        self.btn2 = wx.Button(self.panel, -1, "아니오") 

        #버튼 클릭 이벤트에 함수(메쏘드) 연결하는 코드
        self.Bind(wx.EVT_BUTTON, self.Getlink, self.btn1)
        self.Bind(wx.EVT_BUTTON, self.OnCloseWindow, self.btn2)

        #창 디자인 출력 코드
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.btn1)
        sizer.Add(self.btn2)
        self.panel.SetSizer(sizer)
        self.Show()
        
    #def: diaglog 박스 실행 함수
    def Getlink(self, e):
        webbrowser.open_new_tab("https://cran.r-project.org/mirmon_report.html#kr")
        self.Destroy()
    
    #def: 패널 메뉴의 창 닫기 함수
    def OnCloseWindow(self, e):
        self.Destroy()

#마무리 코드
app = wx.App()
frame = Frame(None, 'R CRAN 바로가기')
app.MainLoop()
'''
