import requests
from bs4 import BeautifulSoup

url = "http://www.atmovies.com.tw/movie/next"
Data = requests.get(url)
Data.encoding = "utf-8"
#print(Data.text)
sp = BeautifulSoup(Data.text, "html.parser")
result=sp.select(".filmListAllX li")
for x in result:
	print(x.find("img").get("alt"))
	#print(x.find(class_="filmtitle").text)
	print(x.find("img").get("src").replace("  ","  "))
	print("http://www.atmovies.com.tw" + x.find("a").get("href"))
	print()