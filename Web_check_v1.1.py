import requests
from bs4 import BeautifulSoup

#1. request
resp3 = requests.get('http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?searchType=1&bidSearchType=1&taskClCds=&bidNm=%BA%F2%B5%A5%C0%CC%C5%CD+%C4%B7%C6%DB%BD%BA&searchDtType=1&fromBidDt=2020%2F11%2F02&toBidDt=2021%2F03%2F31&fromOpenBidDt=&toOpenBidDt=&radOrgan=1&instNm=%BC%AD%BF%EF%C6%AF%BA%B0%BD%C3&instSearchRangeType=&refNo=&area=&areaNm=&industry=&industryCd=&budget=&budgetCompare=UP&detailPrdnmNo=&detailPrdnm=&procmntReqNo=&intbidYn=&regYn=Y&recordCountPerPage=10') #html3 = resp3.text


#2-1. BeautifulSoup
soup = BeautifulSoup(resp1.text,'html.parser') #html.parser를 사용해서 soup에 넣겠다
f_div = soup.find("p") #print(str1,f_div)

soup2 = BeautifulSoup(resp2.text,'html.parser') 
f_div2 = soup2.find("p") #print(str2,f_div2)

soup3 = BeautifulSoup(resp3.content,'html.parser') 
soup4 = BeautifulSoup(resp4.content,'html.parser') 
soup5 = BeautifulSoup(resp5.content,'html.parser') 


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