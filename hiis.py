import requests
import time

file = open('debug.txt', 'w+')

hdr = {'Cookie': 'JSESSIONID=0000AbGN_QPRfFpV4xaIxrz51r-:-1; PHAROS_VISITOR=00bbc07c01703d30b28c1879ac10010d',
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}

url = 'https://hiis.uhs.ac.kr/servlets/filter?url='

s = requests.Session()

arr = [str(i) for i in range(0, 10)]
arr = arr[:] + [chr(i) for i in range(ord('A'), ord('Z')+1)]

for i in arr:
    try:
        r = s.get(url + '0' + i, headers = hdr)
        file.write(i + '  ' + r.text + '\n')
        time.sleep(1)
    except:
        pass

for i in arr:
    for j in arr:
        try:
            r = s.get(url + i + j, headers = hdr)
            print(i + j)
            r = s.get(url + i + j, headers = hdr)
            file.write(i + j + ' ' + r.text + '\n')
            time.sleep(2)
        except:
            pass

file.close()
