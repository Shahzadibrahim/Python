
import requests

urls=["https://www.google.com/", "https://www.ynet.co.il/home/0,7340,L-8,00.html", "https://www.imdb.com/"]
times=[]

for url in urls:
    request_time=requests.get(url).elapsed.total_seconds()
    print(request_time)
    times.append(request_time)

request_dict=dict(zip(urls,times))
print(request_dict)