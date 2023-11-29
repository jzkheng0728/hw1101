import firebase_admin
from firebase_admin import credentials, firestore
import requests
from bs4 import BeautifulSoup
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)


from flask import Flask, render_template, request
from datetime import datetime,timezone,timedelta
app = Flask(__name__)

@app.route("/")
def index():
	X = "作者：邓佳钲1129<br>"
	X += "<a href=/db>课程</a><br>"
	X +="<a href=/khen?nick=khen>个人简介</a><br>"
	X +="<a href=/account>表单传值</a><br>"
	X += "<br><a href=/read5>人選之人─造浪者</a><br>"
	X += "<br><a href=/input>演员姓名关键字</a><br>"
	X += "<br><a href=/search>演员查询</a><br>"
	X += "<br><a href=/lib>圖書精選</a><br>"
	X += "<br><a href=/spider>老师课程</a><br>"
	return X

@app.route("/db")
def db():
	return "<a href='https://www.youtube.com/'>海青班资料库管理课程</a>"

@app.route("/khen", methods=["GET", "POST"])
def khen():
	tz=timezone(timedelta(hours=+8))
	now = str(datetime.now(tz))
	user = request.values.get("nick")
	return render_template("khen.html", datetime=now, name=user)

@app.route("/account", methods=["GET", "POST"])
def account():
	if request.method == "POST":
		user = request.form["user"]
		pwd = request.form["pwd"]
		result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd
		return result
	else:
		return render_template("acc.html")

@app.route("/read5")
def read5():
	Result = ""     
	db = firestore.client()
	collection_ref = db.collection("人選之人─造浪者")    
	docs = collection_ref.get()    
	for doc in docs:         
		Result += "文件內容：{}".format(doc.to_dict()) + "<br>"    
	return Result

@app.route("/input", methods=["GET", "POST"])
def input():
	if request.method == "POST":
		user = request.form["keyword"]
		result = "您輸入的帳號是：" + keyword
		return result
	else:
		return render_template("input.html")

@app.route("/search", methods=["GET", "POST"])
def search():
	if request.method == "POST":
		keyword = request.form["keyword"]
		Result = "您輸入的帳號是：" + keyword
		Result += "<br>"
		db = firestore.client()
		collection_ref = db.collection("人選之人─造浪者")
		docs = collection_ref.order_by("birth").get()
		for doc in docs:
			x = doc.to_dict()
			if keyword in x["name"]:
				Result += "演员：" + x["name"] + ",在剧中扮演" + x["role"] + ",出生于" + str(x["birth"]) + "<br>"
		return Result
	else:
		return render_template("search.html")

@app.route("/lib")
def lib():
	Result = ""
	db = firestore.client()
	collection_ref = db.collection("圖書精選")
	docs = collection_ref.order_by("anniversary").get()
	for doc in docs:
		x = doc.to_dict()
		Result += "书名:<a href=" + x["url"] + ">" + x["title"] + "</a><br>"
		Result += "作者:" + x["author"] + "<br>"
		Result += str(x["anniversary"]) + "周年纪念版" + "<br>" 
		Result += "<img src=" + x["cover"] + "></img><br><br>" 
	return Result


@app.route("/search2", methods=["GET", "POST"])
def search2():
	if request.method == "POST":
		keyword = request.form["keyword"]
		Result = "您輸入的帳號是：" + keyword
		Result += "<br>"
		db = firestore.client()
		collection_ref = db.collection("圖書精選")
		docs = collection_ref.order_by("anniversary").get()
		for doc in docs:
			x = doc.to_dict()
			if keyword in x["name"]:
				Result += "书名:<a href=" + x["url"] + ">" + x["title"] + "</a><br>"
				Result += "作者:" + x["author"] + "<br>"
				Result += str(x["anniversary"]) + "周年纪念版" + "<br>"
				Result += "<img src=" + x["cover"] + "></img><br><br>"
		return Result
	else:
		return render_template("search2.html")

@app.route("/spider")
def spider():

	url = "https://www1.pu.edu.tw/~tcyang/course.html"
	Data = requests.get(url)
	Data.encoding = "utf-8"

	sp = BeautifulSoup(Data.text, "html.parser")
	result=sp.select(".team-box")
	info = ""
	for x in result:
		info += "<a href=" + x.find("a").get("href") + x.text + "</a><br>"
		info += x.find("a").get("href") + "<br>"
		info += "<img src=https://www1.pu.edu.tw/~tcyang/" + x.find("img").get("src") + "></img><br><br>"

	return info


if __name__ == "__main__":
	app.run(debug=True)