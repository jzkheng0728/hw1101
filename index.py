import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)


from flask import Flask, render_template, request
from datetime import datetime,timezone,timedelta
app = Flask(__name__)

@app.route("/")
def index():
	X = "作者：邓佳钲1108<br>"
	X += "<a href=/db>课程</a><br>"
	X +="<a href=/khen?nick=khen>个人简介</a><br>"
	X +="<a href=/account>表单传值</a><br>"
	X += "<br><a href=/read>讀取Firestore資料</a><br>"
	X += "<br><a href=/read5>人選之人─造浪者</a><br>"
	X += "<br><a href=/read5>演员关键字查询</a><br>"
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
def read():
    Result = ""     
    db = firestore.client()
    collection_ref = db.collection("邓佳钲")    
    docs = collection_ref.get()    
    for doc in docs:         
        Result += "文件內容：{}".format(doc.to_dict()) + "<br>"    
    return Result

@app.route("/read5")
def read5():
    Result = ""     
    db = firestore.client()
    collection_ref = db.collection("人選之人─造浪者")    
    docs = collection_ref.get()    
    for doc in docs:         
        Result += "文件內容：{}".format(doc.to_dict()) + "<br>"    
    return Result

@app.route("/account", methods=["GET", "POST"])
def account():
	if request.method == "POST":
		user = request.form["keyword"]
		result = "您輸入的帳號是：" + keyword
		return result
	else:
		return render_template("acc.html")

#if __name__ == "__main__":
	#app.run()