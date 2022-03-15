'''
Config : UTF-8

Title : PING 체크 스크립트 v1.0

Write : 22.03.15 / Update :22.03.15

'''

import subprocess
import re
#
p = re.compile('[=]\s(\d+)[m][s]')
num = 0
#
input_f = open('svr_list.txt', 'r')
line_cnt = len(input_f.readlines())
input_f.close
#
with open('svr_list.txt', 'r') as f:
    while num < line_cnt:
        num = num +1
        ip = f.readline()
        #print(num,"번 ",ip)
        ip1 = ip.replace('\n', '')
        cmd = 'ping '+ip1
        try:
            for x in subprocess.check_output(cmd).splitlines():
                p1 = p.findall(str(x))
            print(ip1,'Ping Ok','최소 응답시간: '+p1[0],'최대 응답시간: '+p1[1],'평균 응답시간: '+p1[2])
        except subprocess.CalledProcessError:
            print(ip1,'Ping Check Need !!!...')