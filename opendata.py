import requests, json

url = "https://datacenter.taichung.gov.tw/swagger/OpenData/db36e286-1d2b-4784-99b9-3b0790dd9652"
Data = requests.get(url)
#print(Data.text)

JsonData = json.loads(Data.text)

Road = input("请输入预查寻的路段关键字:")

for x in JsonData:
	if Road in x():
		print(x["路口名称"] + "共发生了" + x["总件数"] + "次车祸")
		print("事件发生的主要原因是因为" + x["主要肇因"])
		print()